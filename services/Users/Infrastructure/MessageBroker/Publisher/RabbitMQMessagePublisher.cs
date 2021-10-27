using Newtonsoft.Json;
using System.Text;

namespace Users.Infrastructure.MessageBroker.Sender
{
    public class RabbitMqMessagePublisher : IMessagePublisher
    {
        private readonly RabbitMQConnectionFactory _connectionFactory;

        public RabbitMqMessagePublisher(RabbitMQConnectionFactory connectionFactory)
        {
            _connectionFactory = connectionFactory;
        }

        public void Publish(Message message)
        {
            _connectionFactory.GetChannel().BasicPublish(
                exchange: "",
                routingKey: _connectionFactory.GetQueueName(),
                basicProperties: null,
                body: GetMessageBytes(message),
                mandatory: true);
        }

        private byte[] GetMessageBytes(Message message)
        {
            string messageString = JsonConvert.SerializeObject(message);
            return Encoding.UTF8.GetBytes(messageString);
        }
    }
}
