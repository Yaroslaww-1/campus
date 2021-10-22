﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;
using Users.Infrastructure.EntityFramework;

namespace Users.Infrastructure.EntityFramework.Migrations
{
    [DbContext(typeof(UsersDbContext))]
    partial class UsersDbContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("Relational:MaxIdentifierLength", 63)
                .HasAnnotation("ProductVersion", "5.0.11")
                .HasAnnotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn);

            modelBuilder.Entity("Users.Entities.Role", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid")
                        .HasColumnName("id");

                    b.Property<string>("Name")
                        .IsRequired()
                        .HasColumnType("text")
                        .HasColumnName("name");

                    b.HasKey("Id")
                        .HasName("pk_role");

                    b.HasIndex("Name")
                        .IsUnique()
                        .HasDatabaseName("ix_role_name");

                    b.ToTable("role");
                });

            modelBuilder.Entity("Users.Entities.User", b =>
                {
                    b.Property<Guid>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("uuid")
                        .HasColumnName("id");

                    b.Property<string>("Email")
                        .IsRequired()
                        .HasColumnType("text")
                        .HasColumnName("email");

                    b.Property<string>("Name")
                        .IsRequired()
                        .HasColumnType("text")
                        .HasColumnName("name");

                    b.Property<string>("PasswordHash")
                        .HasColumnType("text")
                        .HasColumnName("password_hash");

                    b.Property<string>("PasswordHashSalt")
                        .HasColumnType("text")
                        .HasColumnName("password_hash_salt");

                    b.HasKey("Id")
                        .HasName("pk_user");

                    b.HasIndex("Email")
                        .IsUnique()
                        .HasDatabaseName("ix_user_email");

                    b.ToTable("user");
                });

            modelBuilder.Entity("user_role", b =>
                {
                    b.Property<Guid>("role_id")
                        .HasColumnType("uuid")
                        .HasColumnName("role_id");

                    b.Property<Guid>("user_id")
                        .HasColumnType("uuid")
                        .HasColumnName("user_id");

                    b.HasKey("role_id", "user_id")
                        .HasName("pk_user_role");

                    b.HasIndex("user_id")
                        .HasDatabaseName("ix_user_role_user_id");

                    b.ToTable("user_role");
                });

            modelBuilder.Entity("user_role", b =>
                {
                    b.HasOne("Users.Entities.Role", null)
                        .WithMany()
                        .HasForeignKey("role_id")
                        .HasConstraintName("fk_user_role_role_role_id")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("Users.Entities.User", null)
                        .WithMany()
                        .HasForeignKey("user_id")
                        .HasConstraintName("fk_user_role_user_user_id")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();
                });
#pragma warning restore 612, 618
        }
    }
}