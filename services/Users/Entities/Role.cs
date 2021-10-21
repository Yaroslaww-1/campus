using System;
using System.Collections.Generic;

namespace Users.Entities
{
    public class Role
    {
        public Guid Id { get; set; }
        public string Name { get; set; }
        public IList<User> Users { get; set; }
    }
}
