using Users.Infrastructure.MessageBroker;
using Users.Infrastructure.MessageBroker.Sender;

namespace Users.Services.Users.IntegrationEvents
{
    public class UsersIntegrationEventsPublisher
    {
        private readonly IMessagePublisher _messagePublisher;

        public UsersIntegrationEventsPublisher(IMessagePublisher messagePublisher)
        {
            _messagePublisher = messagePublisher;
        }

        public void PublishUserCreatedEvent(UserCreatedIntegrationEvent @event)
        {
            var message = new Message(nameof(UserCreatedIntegrationEvent), @event);
            _messagePublisher.Publish(message);
        }
    }
}
