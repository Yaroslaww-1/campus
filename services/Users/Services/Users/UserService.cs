using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Users.BuildingBlocks.Security;
using Users.Entities;
using Users.Infrastructure.EntityFramework.Repositories.Users;
using Users.Services.Users.IntegrationEvents;

namespace Users.Services.Users
{
    public class UserService
    {
        private readonly IUserRepository _userRepository;
        private readonly ISecurityService _securityService;
        private readonly UsersIntegrationEventsPublisher _usersIntegrationEventsPublisher;

        public UserService(IUserRepository userRepository, ISecurityService securityService, UsersIntegrationEventsPublisher usersIntegrationEventsPublisher)
        {
            _userRepository = userRepository;
            _securityService = securityService;
            _usersIntegrationEventsPublisher = usersIntegrationEventsPublisher;
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

        public async Task CreateUser(
            Guid id,
            string email,
            string name,
            string password,
            List<Role> roles)
        {
            var user = User.CreateNew(
                email,
                name,
                password,
                roles,
                _securityService);

            user.Id = id;

            await _userRepository.CreateUser(user);

            _usersIntegrationEventsPublisher.PublishUserCreatedEvent(new UserCreatedIntegrationEvent(user.Id, user.Name, user.Email, roles.Select(r => r.Name).ToList()));
        }
    }
}
