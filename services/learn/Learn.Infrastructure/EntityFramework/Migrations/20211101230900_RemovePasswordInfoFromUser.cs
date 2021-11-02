using Microsoft.EntityFrameworkCore.Migrations;

namespace Learn.Infrastructure.EntityFramework.Migrations
{
    public partial class RemovePasswordInfoFromUser : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "password_hash",
                table: "user");

            migrationBuilder.DropColumn(
                name: "password_hash_salt",
                table: "user");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "password_hash",
                table: "user",
                type: "text",
                nullable: true);

            migrationBuilder.AddColumn<string>(
                name: "password_hash_salt",
                table: "user",
                type: "text",
                nullable: true);
        }
    }
}
