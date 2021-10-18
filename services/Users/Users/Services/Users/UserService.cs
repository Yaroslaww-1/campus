using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Users.Infrastructure.EntityFramework.Repositories.Users;

namespace Users.Services.Users
{
    public class UserService
    {
        private readonly IUserRepository _userRepository;

        public UserService(IUserRepository userRepository)
        {
            _userRepository = userRepository;
        }

        public async Task<IList<UserDto>> GetAllUsers()
        {
            return (await _userRepository.GetAll())
                .Select(u => new UserDto()
                {
                    Id = u.Id,
                    Name = u.Name,
                    Email = u.Email,
                    Roles = u.Roles
                        .Select(r => new RoleDto() { Id = r.Id, Name = r.Name })
                        .ToList()
                })
                .ToList();
        }
    }
}
