using Learn.BuildingBlocks.Domain;
using System;

namespace Learn.Domain.Chats
{
    public class ChatId : TypedIdValueBase
    {
        public ChatId(Guid value)
            : base(value)
        {
        }
    }
}
