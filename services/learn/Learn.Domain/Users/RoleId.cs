using Learn.BuildingBlocks.Domain;
using System;

namespace Learn.Domain.Users
{
    public class RoleId : TypedIdValueBase
    {
        public RoleId(Guid value)
            : base(value)
        {
        }
    }
}
