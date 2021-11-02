using Learn.Domain.Users;
using System;
using System.Collections.Generic;

namespace Learn.Domain.Chats
{
    public class Chat
    {
        public ChatId Id { get; private set; }
        public string Name { get; private set; }
        public User CreatedBy { get; private set; }
        public List<ChatMember> Members { get; private set; }

        private Chat()
        {
            // Only for EF
        }

        private Chat(ChatId chatId, string name, User createdBy, List<ChatMember> members)
        {
            Id = chatId;
            Name = name;
            CreatedBy = createdBy;
            Members = members;
        }

        public static Chat CreateNew(string name, User createdBy)
        {
            var chatId = new ChatId(Guid.NewGuid());

            var firstChatMember = ChatMember.CreateNew(createdBy, chatId);

            return new Chat(chatId, name, createdBy, new List<ChatMember>() { firstChatMember });
        }
    }
}
