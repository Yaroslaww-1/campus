using Learn.BuildingBlocks.Application.ExecutionContext;
using Learn.BuildingBlocks.ExecutionContext;
using Learn.BuildingBlocks.Infrastructure;
using Learn.BuildingBlocks.Infrastructure.Options;
using Learn.Domain.Chats;
using Learn.Infrastructure.EntityFramework;
using Learn.Infrastructure.EntityFramework.Repositories.Users;
using Learn.Infrastructure.EntityFramework.Seeding;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

namespace Learn.Infrastructure
{
    public static class InfrastructureDependencyInjection
    {
        public static IServiceCollection AddInfrastructure(this IServiceCollection services, IConfiguration configuration)
        {
            services.AddOptions(configuration);
            services.AddDatabaseContext(configuration);

            services.AddRepositories();
            services.AddUserContext();

            return services;
        }

        public static IApplicationBuilder ConfigureInfrastructure(this IApplicationBuilder app, bool migrate = true, bool seed = true)
        {
            if (migrate)
            {
                MigrateDatabase(app);
            }

            if (seed)
            {
                SeedDatabase(app);
            }

            return app;
        }

        private static IServiceCollection AddOptions(this IServiceCollection services, IConfiguration configuration)
        {
            services.Configure<DatabaseOptions>(configuration.GetSection(DatabaseOptions.Location));
            services.Configure<UrlsOptions>(configuration.GetSection(UrlsOptions.Location));

            return services;
        }

        private static IServiceCollection AddRepositories(this IServiceCollection services)
        {
            services.AddTransient<IChatRepository, ChatRepository>();

            return services;
        }

        private static IServiceCollection AddUserContext(this IServiceCollection services)
        {
            services.AddSingleton<IHttpContextAccessor, HttpContextAccessor>();
            services.AddSingleton<IExecutionContextAccessor, ExecutionContextAccessor>();
            services.AddSingleton<IUserContext, UserContext>();

            return services;
        }

        private static IServiceCollection AddDatabaseContext(this IServiceCollection services, IConfiguration configuration)
        {
            var databaseOptions = configuration.GetSection(DatabaseOptions.Location).Get<DatabaseOptions>();

			var migrationAssembly = typeof(LearnDbContext).Assembly.GetName().Name;

			services.AddDbContext<LearnDbContext>(options =>
            {
                options
                    .UseNpgsql(
                        databaseOptions.ConnectionString,
                        opt => opt.MigrationsAssembly(migrationAssembly))
                    .UseSnakeCaseNamingConvention();

                options.ReplaceService<IValueConverterSelector, StronglyTypedIdValueConverterSelector>();
            });

            return services;
        }

		public static void MigrateDatabase(IApplicationBuilder app)
		{
			using (var scope = app.ApplicationServices.GetService<IServiceScopeFactory>().CreateScope())
			{
				using var context = scope.ServiceProvider.GetRequiredService<LearnDbContext>();
				context.Database.Migrate();
			};
		}

        public static void SeedDatabase(IApplicationBuilder app)
        {
            var databaseSeeder = new DatabaseSeeder(app);
            databaseSeeder.SeedDatabase();
        }
    }
}