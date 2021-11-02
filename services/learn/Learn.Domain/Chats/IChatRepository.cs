using System.Threading.Tasks;

namespace Learn.Domain.Chats
{
    public interface IChatRepository
    {
        public Task AddAsync(Chat chat);
    }
}
