using System.Collections.Generic;
using System.Threading.Tasks;
using Users.Entities;

namespace Users.Infrastructure.EntityFramework.Repositories.Users
{
    public interface IUserRepository
    {
        Task<IList<User>> GetAll();
    }
}
