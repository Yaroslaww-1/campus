using System.Threading.Tasks;

namespace Users.Infrastructure.MessageBroker.Sender
{
    public interface IMessagePublisher
    {
        public void Publish(Message message);
    }
}
