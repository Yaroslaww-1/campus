using System;
using System.Collections.Generic;
using Users.Infrastructure.EventBus.Integration;

namespace Users.Services.Users.IntegrationEvents
{
    public class UserCreatedIntegrationEvent : IntegrationEvent
    {
        public Guid UserId { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
        public List<string> Roles { get; set; }

        public UserCreatedIntegrationEvent(Guid userId, string name, string email, List<string> roles)
            :base(Guid.NewGuid(), DateTime.Now)
        {
            UserId = userId;
            Name = name;
            Email = email;
            Roles = roles;
        }
    }
}
