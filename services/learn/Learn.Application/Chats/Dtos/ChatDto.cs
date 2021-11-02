using System;
using System.Collections.Generic;

namespace Learn.Application.Chats.Dtos
{
    public class ChatDto
    {
        public Guid Id { get; set; }
        public string Name { get; set; }
        public List<ChatMemberDto> Members { get; set; }
    }
}
