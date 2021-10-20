using Microsoft.EntityFrameworkCore;
using Users.Entities;
using Users.Infrastructure.EntityFramework.EntityConfigurations;

namespace Users.Infrastructure.EntityFramework
{
    public class UsersDbContext : DbContext
    {
        public DbSet<User> Users { get; set; }

        public DbSet<Role> Roles { get; set; }

        public UsersDbContext(DbContextOptions<UsersDbContext> options) : base(options) { }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.ApplyConfigurationsFromAssembly(typeof(RoleEntityConfiguration).Assembly);
        }
    }
}
