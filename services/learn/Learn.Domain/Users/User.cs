using System;
using System.Collections.Generic;

namespace Learn.Domain.Users
{
    public class User
    {
        public Guid Id { get; private set; }
        public string Email { get; private set; }
        public string Name { get; private set; }
        public string PasswordHash { get; private set; }
        public string PasswordHashSalt { get; private set; }
        public IList<Role> Roles { get; private set; }

        private User()
        {
            // Only for EF
        }

        private User(
            string email,
            string name,
            string passwordHash,
            string passwordHashSalt,
            List<Role> roles)
        {
            Id = Guid.NewGuid();
            Email = email;
            Name = name;
            PasswordHash = passwordHash;
            PasswordHashSalt = passwordHashSalt;
            Roles = roles;
        }
    }
}
