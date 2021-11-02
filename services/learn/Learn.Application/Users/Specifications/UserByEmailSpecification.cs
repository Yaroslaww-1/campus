using Ardalis.Specification;
using Learn.Domain.Users;

namespace Learn.Application.Users.Specifications
{
    public class UserByEmailSpecification : Specification<User>, ISingleResultSpecification
    {
        public UserByEmailSpecification(string email)
        {
            base.Query.Where(u => u.Email == email);
        }
    }
}
