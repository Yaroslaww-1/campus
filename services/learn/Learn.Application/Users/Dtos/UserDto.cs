using System;
using System.Collections.Generic;

namespace Learn.Application.Users.Dtos
{
    public class UserDto
    {
        public Guid Id { get; set; }
        public string Name { get; set; }
        public List<RoleDto> Roles { get; set; }
    }
}
