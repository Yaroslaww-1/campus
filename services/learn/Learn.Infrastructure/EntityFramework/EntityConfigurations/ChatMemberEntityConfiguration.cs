using Learn.Domain.Chats;
using Learn.Domain.Users;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace Learn.Infrastructure.EntityFramework.EntityConfigurations
{
    public class ChatMemberEntityConfiguration : IEntityTypeConfiguration<ChatMember>
    {
        public void Configure(EntityTypeBuilder<ChatMember> entity)
        {
            entity.ToTable("chat_member");

            entity
                .Property(cm => cm.Id)
                .HasColumnType("uuid")
                .IsRequired();

            entity.HasKey(cm => cm.Id);

            entity
                .HasOne(cm => cm.User);
        }
    }
}
