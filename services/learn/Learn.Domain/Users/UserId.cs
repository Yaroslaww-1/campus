using Learn.BuildingBlocks.Domain;
using System;

namespace Learn.Domain.Users
{
    public class UserId : TypedIdValueBase
    {
        public UserId(Guid value)
            : base(value)
        {
        }
    }
}
