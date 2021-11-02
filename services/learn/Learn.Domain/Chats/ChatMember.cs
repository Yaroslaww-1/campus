using Learn.Domain.Users;
using System;
using System.Collections.Generic;

namespace Learn.Domain.Chats
{
    public class ChatMember
    {
        public ChatMemberId Id { get; private set; }
        public ChatId ChatId { get; private set; }
        public User User { get; private set; }
        public string Name { get => User.Name; }

        private ChatMember()
        {
            // Only for EF
        }

        private ChatMember(User user, ChatId chatId)
        {
            Id = new ChatMemberId(Guid.NewGuid());
            User = user;
            ChatId = chatId;
        }

        public static ChatMember CreateNew(User user, ChatId chatId)
        {
            return new ChatMember(user, chatId);
        }
    }
}
