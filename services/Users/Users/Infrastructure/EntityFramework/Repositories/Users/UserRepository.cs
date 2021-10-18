using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Threading.Tasks;
using Users.Entities;

namespace Users.Infrastructure.EntityFramework.Repositories.Users
{
    public class UserRepository : IUserRepository
    {
        private readonly UsersDbContext _dbContext;

        public UserRepository(UsersDbContext dbContext)
        {
            _dbContext = dbContext;
        }

        public async Task<IList<User>> GetAll()
        {
            var users = await _dbContext.Users
                .Include(u => u.Roles)
                .ToListAsync();

            return users;
        }
    }
}
