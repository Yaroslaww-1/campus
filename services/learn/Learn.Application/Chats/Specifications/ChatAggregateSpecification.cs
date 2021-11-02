using Ardalis.Specification;
using Learn.Domain.Chats;

namespace Learn.Application.Chats.Specifications
{
    public class ChatAggregateSpecification : Specification<Chat>
    {
        public ChatAggregateSpecification()
        {
            base.Query
                .Include(c => c.Members)
                .ThenInclude(m => m.User);
        }
    }
}
