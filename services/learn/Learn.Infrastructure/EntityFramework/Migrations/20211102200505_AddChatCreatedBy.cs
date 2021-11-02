using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace Learn.Infrastructure.EntityFramework.Migrations
{
    public partial class AddChatCreatedBy : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<Guid>(
                name: "created_by_id",
                table: "chat",
                type: "uuid",
                nullable: true);

            migrationBuilder.CreateIndex(
                name: "ix_chat_created_by_id",
                table: "chat",
                column: "created_by_id");

            migrationBuilder.AddForeignKey(
                name: "fk_chat_users_created_by_id",
                table: "chat",
                column: "created_by_id",
                principalTable: "user",
                principalColumn: "id",
                onDelete: ReferentialAction.Restrict);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "fk_chat_users_created_by_id",
                table: "chat");

            migrationBuilder.DropIndex(
                name: "ix_chat_created_by_id",
                table: "chat");

            migrationBuilder.DropColumn(
                name: "created_by_id",
                table: "chat");
        }
    }
}
