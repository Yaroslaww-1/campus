using System;
using System.Collections.Generic;

namespace Learn.Domain.Users
{
    public class Role
    {
        public Guid Id { get; private set; }
        public string Name { get; private set; }
        public IList<User> Users { get; private set; }

        private Role()
        {
            // Only for EF
        }

        private Role(string name)
        {
            Id = Guid.NewGuid();
            Name = name;
            Users = new List<User>();
        }

        public static Role CreateNew(string name)
        {
            return new Role(name);
        }
    }
}
