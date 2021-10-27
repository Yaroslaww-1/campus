using System;
using RabbitMQ.Client;
using Microsoft.Extensions.Configuration;
using Users.Options;

namespace Users.Infrastructure.MessageBroker
{
    public class RabbitMQConnectionFactory : IDisposable
    {
        private readonly ConnectionFactory _connectionFactory;
        private string _queueName;
        private IConnection _connection;
        private IModel _channel;

        public RabbitMQConnectionFactory(IConfiguration configuration)
        {
            var rabbitMQOptions = configuration.GetSection(RabbitMQOptions.Location).Get<RabbitMQOptions>();

            _queueName = rabbitMQOptions.QueueName;

            _connectionFactory = new ConnectionFactory() { HostName = rabbitMQOptions.HostName, Port = Int32.Parse(rabbitMQOptions.Port) };

            _connection = _connectionFactory.CreateConnection();

            _channel = _connection.CreateModel();

            _channel.QueueDeclare(
                queue: rabbitMQOptions.QueueName,
                durable: true,
                exclusive: false,
                autoDelete: false,
                arguments: null);
        }

        public void Dispose()
        {
            _channel.Dispose();
            _connection.Dispose();
        }

        public IConnection GetConnection()
        {
            return _connection;
        }

        public IModel GetChannel()
        {
            return _channel;
        }

        public string GetQueueName()
        {
            return _queueName;
        }
    }
}
