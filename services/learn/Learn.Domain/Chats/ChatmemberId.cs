using Learn.BuildingBlocks.Domain;
using System;

namespace Learn.Domain.Chats
{
    public class ChatMemberId : TypedIdValueBase
    {
        public ChatMemberId(Guid value)
            : base(value)
        {
        }
    }
}
