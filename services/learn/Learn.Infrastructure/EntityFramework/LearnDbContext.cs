using Microsoft.EntityFrameworkCore;
using Learn.Infrastructure.EntityFramework.EntityConfigurations;
using Learn.Domain.Users;

namespace Learn.Infrastructure.EntityFramework
{
    public class LearnDbContext : DbContext
    {
        public DbSet<User> Users { get; set; }

        public DbSet<Role> Roles { get; set; }

        public LearnDbContext() : base() { }

        public LearnDbContext(DbContextOptions<LearnDbContext> options) : base(options) { }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.ApplyConfigurationsFromAssembly(typeof(RoleEntityConfiguration).Assembly);
        }
    }
}
