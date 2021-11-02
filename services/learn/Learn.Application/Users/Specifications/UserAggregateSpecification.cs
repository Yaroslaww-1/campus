using Ardalis.Specification;
using Learn.Domain.Users;

namespace Learn.Application.Users.Specifications
{
    public class UserAggregateSpecification : Specification<User>
    {
        public UserAggregateSpecification()
        {
            base.Query.Include(u => u.Roles);
        }
    }
}
