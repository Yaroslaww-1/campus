using System;
using System.Collections.Generic;

namespace Users.Services.Users.IntegrationEvents
{
    public class UserCreatedIntegrationEvent
    {
        public Guid Id { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
        public List<string> Roles { get; set; }

        public UserCreatedIntegrationEvent(Guid id, string name, string email, List<string> roles)
        {
            Id = id;
            Name = name;
            Email = email;
            Roles = roles;
        }
    }
}
