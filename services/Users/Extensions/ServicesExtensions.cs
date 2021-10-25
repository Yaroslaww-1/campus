using IdentityServer4.AccessTokenValidation;
using IdentityServer4.Services;
using IdentityServer4.Validation;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.IdentityModel.Logging;
using Microsoft.IdentityModel.Tokens;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Users.BuildingBlocks.ExecutionContext;
using Users.BuildingBlocks.Security;
using Users.Infrastructure.EntityFramework;
using Users.Infrastructure.EntityFramework.Repositories.Users;
using Users.Infrastructure.IdentityServer;
using Users.Options;
using Users.Services.Auth;
using Users.Services.Users;

namespace Users.Extensions
{
    public static class ServicesExtensions
    {
		public static void RegisterOptions(this IServiceCollection services, IConfiguration configuration)
		{
			services.Configure<DatabaseOptions>(configuration.GetSection(DatabaseOptions.Location));
		}

		public static void RegisterDatabase(this IServiceCollection services, IConfiguration configuration)
        {
			var databaseOptions = configuration.GetSection(DatabaseOptions.Location).Get<DatabaseOptions>();

			var migrationAssembly = typeof(UsersDbContext).Assembly.GetName().Name;

			services.AddDbContext<UsersDbContext>(options =>
				options
					.UseNpgsql(
						databaseOptions.ConnectionString,
						opt => opt.MigrationsAssembly(migrationAssembly))
					.UseSnakeCaseNamingConvention()
			);
		}

		public static void RegisterRepositories(this IServiceCollection services, IConfiguration configuration)
		{
			services.AddTransient<IUserRepository, UserRepository>();
		}

		public static void RegisterServices(this IServiceCollection services, IConfiguration configuration)
		{
			services.AddTransient<ISecurityService, SecurityService>();

			services.AddTransient<UserService>();
			services.AddTransient<IAuthenticationService, AuthenticationService>();
		}

		public static IServiceCollection RegisterIdentityServer(this IServiceCollection services, IConfiguration configuration)
		{
			services.AddIdentityServer()
				.AddInMemoryIdentityResources(IdentityServerConfig.GetIdentityResources())
				.AddInMemoryApiResources(IdentityServerConfig.GetApis())
				.AddInMemoryClients(IdentityServerConfig.GetClients())
				.AddInMemoryPersistedGrants()
				.AddProfileService<ProfileService>()
				.AddDeveloperSigningCredential();

			var urlsOptions = configuration.GetSection(UrlsOptions.Location).Get<UrlsOptions>();

			services.AddTransient<IResourceOwnerPasswordValidator, ResourceOwnerPasswordValidator>();

			services.AddAuthentication(IdentityServerAuthenticationDefaults.AuthenticationScheme)
				.AddJwtBearer(IdentityServerAuthenticationDefaults.AuthenticationScheme, options =>
				{
					options.Authority = urlsOptions.GatewayApiUrl;
					options.RequireHttpsMetadata = false;


					options.TokenValidationParameters = new TokenValidationParameters
					{
						ValidateAudience = false
					};

					options.Events = new JwtBearerEvents
					{
						OnMessageReceived = context =>
						{
							var accessToken = context.Request.Query["access_token"];

							// If the request is for our hub...
							var path = context.HttpContext.Request.Path;
							if (!string.IsNullOrEmpty(accessToken) &&
								(path.StartsWithSegments("/hubs")))
							{
								// Read the token out of the query string
								context.Token = accessToken;
							}
							return Task.CompletedTask;
						}
					};
				});

			services.AddSingleton<ICorsPolicyService>((container) =>
			{
				var logger = container.GetRequiredService<Microsoft.Extensions.Logging.ILogger<DefaultCorsPolicyService>>();
				return new DefaultCorsPolicyService(logger)
				{
					AllowedOrigins = { urlsOptions.GatewayApiUrl }
				};
			});

			IdentityModelEventSource.ShowPII = true;

			services.AddSingleton<IHttpContextAccessor, HttpContextAccessor>();
			services.AddSingleton<IExecutionContextAccessor, ExecutionContextAccessor>();

			return services;
		}

		public static void InitializeDatabase(this IApplicationBuilder app)
		{
			using (var scope = app.ApplicationServices.GetService<IServiceScopeFactory>().CreateScope())
			{
				using var context = scope.ServiceProvider.GetRequiredService<UsersDbContext>();
				context.Database.Migrate();
			};
		}

		public static void ApplyDatabaseSeeding(this IApplicationBuilder app)
		{
			ApplyRolesSeeding(app);
			ApplyUsersSeeding(app);
		}

		public static void ApplyRolesSeeding(this IApplicationBuilder app)
		{
			using (var scope = app.ApplicationServices.GetService<IServiceScopeFactory>().CreateScope())
			{
				using var context = scope.ServiceProvider.GetRequiredService<UsersDbContext>();

				var existingRoles = context.Roles.ToList();

				if (!existingRoles.Any())
                {
					context.Roles.Add(new Entities.Role()
					{
						Id = Guid.NewGuid(),
						Name = "Student"
					});

					context.Roles.Add(new Entities.Role()
					{
						Id = Guid.NewGuid(),
						Name = "Teacher"
					});

					context.Roles.Add(new Entities.Role()
					{
						Id = Guid.NewGuid(),
						Name = "Admin"
					});

					context.SaveChanges();
				}
			};
		}

		public static void ApplyUsersSeeding(this IApplicationBuilder app)
		{
			using (var scope = app.ApplicationServices.GetService<IServiceScopeFactory>().CreateScope())
			{
				using var context = scope.ServiceProvider.GetRequiredService<UsersDbContext>();

				var securityService = scope.ServiceProvider.GetRequiredService<ISecurityService>();

				var existingUsers = context.Users.ToList();

				var existingRoles = context.Roles.ToList();

				if (!existingUsers.Any())
				{
					var salt = securityService.GetRandomSalt();
					context.Users.Add(new Entities.User()
					{
						Id = new Guid("33333333-3333-3333-3333-333333333333"),
						Email = "student@gmail.com",
						Name = "Student",
						PasswordHash = securityService.HashPassword("studentPass", salt),
						PasswordHashSalt = Convert.ToBase64String(salt),
						Roles = existingRoles.Where(r => r.Name == "Student").ToList()
					});

					salt = securityService.GetRandomSalt();
					context.Users.Add(new Entities.User()
					{
						Id = new Guid("22222222-2222-2222-2222-222222222222"),
						Email = "teacher@gmail.com",
						Name = "Teacher",
						PasswordHash = securityService.HashPassword("teacherPass", salt),
						PasswordHashSalt = Convert.ToBase64String(salt),
						Roles = existingRoles.Where(r => r.Name == "Teacher").ToList()
					});

					salt = securityService.GetRandomSalt();
					context.Users.Add(new Entities.User()
					{			
						Id = new Guid("11111111-1111-1111-1111-111111111111"),
						Email = "admin@gmail.com",
						Name = "Admin",
						PasswordHash = securityService.HashPassword("adminPass", salt),
						PasswordHashSalt = Convert.ToBase64String(salt),
						Roles = existingRoles.Where(r => r.Name == "Admin").ToList()
					});

					context.SaveChanges();
				}
			};
		}
    }
}
