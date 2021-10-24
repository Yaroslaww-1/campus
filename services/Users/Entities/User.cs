using System;
using System.Collections.Generic;

namespace Users.Entities
{
    public class User
    {
        public Guid Id { get; set; }
        public string Email { get; set; }
        public string Name { get; set; }
        public string PasswordHash { get; set; }
        public string PasswordHashSalt { get; set; }
        public IList<Role> Roles { get; set; }
    }
}
