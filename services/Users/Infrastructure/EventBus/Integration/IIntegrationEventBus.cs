using System;
using System.Threading.Tasks;

namespace Users.Infrastructure.EventBus.Integration
{
    public interface IIntegrationEventBus
    {
        Task Publish<T>(T @event)
            where T : IntegrationEvent;
    }
}
