using IdentityServer4.Services;
using IdentityServer4.Validation;
using Microsoft.AspNetCore.Builder;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Threading.Tasks;
using Users.Infrastructure.EntityFramework;
using Users.Infrastructure.EntityFramework.Repositories.Users;
using Users.Options;
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
			services.AddTransient<UserService>();
		}

		public static void InitializeDatabase(this IApplicationBuilder app)
		{
			using (var scope = app.ApplicationServices.GetService<IServiceScopeFactory>().CreateScope())
			{
				using var context = scope.ServiceProvider.GetRequiredService<UsersDbContext>();
				context.Database.Migrate();
			};
		}

		//public static IServiceCollection ConfigureIdentityServer(this IServiceCollection services)
  //      {
		//	services.AddIdentityServer()
		//		.AddInMemoryIdentityResources(IdentityServerConfig.GetIdentityResources())
		//		.AddInMemoryApiResources(IdentityServerConfig.GetApis())
		//		.AddInMemoryClients(IdentityServerConfig.GetClients())
		//		.AddInMemoryPersistedGrants()
		//		.AddProfileService<ProfileService>()
		//		.AddDeveloperSigningCredential();

		//	services.AddTransient<IResourceOwnerPasswordValidator, ResourceOwnerPasswordValidator>();

		//	services.AddAuthentication(IdentityServerAuthenticationDefaults.AuthenticationScheme)
		//		.AddJwtBearer(IdentityServerAuthenticationDefaults.AuthenticationScheme, options =>
		//		{
		//			options.Authority = _resourcesUrls.GatewayApi;
		//			options.RequireHttpsMetadata = false;


		//			options.TokenValidationParameters = new TokenValidationParameters
		//			{
		//				ValidateAudience = false
		//			};

		//			options.Events = new JwtBearerEvents
		//			{
		//				OnMessageReceived = context =>
		//				{
		//					var accessToken = context.Request.Query["access_token"];

		//				// If the request is for our hub...
		//				var path = context.HttpContext.Request.Path;
		//					if (!string.IsNullOrEmpty(accessToken) &&
		//						(path.StartsWithSegments("/hubs")))
		//					{
		//					// Read the token out of the query string
		//					context.Token = accessToken;
		//					}
		//					return Task.CompletedTask;
		//				}
		//			};
		//		});

		//	services.AddSingleton<ICorsPolicyService>((container) =>
		//	{
		//		var logger = container.GetRequiredService<Microsoft.Extensions.Logging.ILogger<DefaultCorsPolicyService>>();
		//		return new DefaultCorsPolicyService(logger)
		//		{
		//			AllowedOrigins = { _resourcesUrls.FrontEnd, _resourcesUrls.GatewayApi }
		//		};
		//	});

		//	IdentityModelEventSource.ShowPII = true;

		//	return services;
  //      }
    }
}
