using Learn.Domain.Chats;
using System.Threading.Tasks;

namespace Learn.Infrastructure.EntityFramework.Repositories.Users
{
    public class ChatRepository : IChatRepository
    {
        private readonly LearnDbContext _dbContext;

        public ChatRepository(LearnDbContext dbContext)
        {
            _dbContext = dbContext;
        }

        public async Task AddAsync(Chat chat)
        {
            await _dbContext.Chats.AddAsync(chat);
            await _dbContext.SaveChangesAsync();
        }
    }
}
