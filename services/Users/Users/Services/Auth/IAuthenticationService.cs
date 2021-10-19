using System.Threading.Tasks;
using Users.Services.Auth.Dtos;
using Users.Services.Users;

namespace Users.Services.Auth
{
    public interface IAuthenticationService
    {
        Task<AuthenticationResultDto> Authenticate(string login, string password);
        Task<UserDto> GetAuthenticatedUser();
    }
}
