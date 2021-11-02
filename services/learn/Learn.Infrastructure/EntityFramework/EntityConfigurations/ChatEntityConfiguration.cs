using Learn.Domain.Chats;
using Learn.Domain.Users;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using System.Collections.Generic;

namespace Learn.Infrastructure.EntityFramework.EntityConfigurations
{
    public class ChatEntityConfiguration : IEntityTypeConfiguration<Chat>
    {
        public void Configure(EntityTypeBuilder<Chat> entity)
        {
            entity.ToTable("chat");

            entity
                .Property(c => c.Id)
                .HasColumnType("uuid")
                .IsRequired();

            entity.HasKey(c => c.Id);

            entity
                .Property(c => c.Name)
                .IsRequired();

            entity
                .HasOne(c => c.CreatedBy);

            entity
                .HasMany(c => c.Members)
                .WithOne()
                .HasForeignKey("ChatId");
        }
    }
}
