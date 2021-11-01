using Learn.BuildingBlocks.Infrastructure.Options;
using Learn.Infrastructure.EntityFramework;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System;

namespace Learn.Infrastructure
{
    public static class InfrastructureDependencyInjection
    {
        public static IServiceCollection AddInfrastructure(this IServiceCollection services, IConfiguration configuration)
        {
            services.AddOptions(configuration);
            services.AddDatabaseContext(configuration);

            return services;
        }

        private static IServiceCollection AddOptions(this IServiceCollection services, IConfiguration configuration)
        {
            services.Configure<DatabaseOptions>(configuration.GetSection(DatabaseOptions.Location));
            services.Configure<UrlsOptions>(configuration.GetSection(UrlsOptions.Location));

            return services;
        }

        private static IServiceCollection AddDatabaseContext(this IServiceCollection services, IConfiguration configuration)
        {
            var databaseOptions = configuration.GetSection(DatabaseOptions.Location).Get<DatabaseOptions>();

			var migrationAssembly = typeof(LearnDbContext).Assembly.GetName().Name;

			services.AddDbContext<LearnDbContext>(options =>
				options
					.UseNpgsql(
						databaseOptions.ConnectionString,
						opt => opt.MigrationsAssembly(migrationAssembly))
					.UseSnakeCaseNamingConvention()
			);

            return services;
        }
	}
}