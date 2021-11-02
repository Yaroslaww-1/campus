using Ardalis.Specification;
using Learn.Domain.Chats;
using Learn.Domain.Users;

namespace Learn.Application.Chats.Specifications
{
    public class ChatByCreatorIdSpecification : Specification<Chat>
    {
        public ChatByCreatorIdSpecification(UserId userId)
        {
            base.Query.Where(u => u.CreatedBy.Id == userId);
        }
    }
}
