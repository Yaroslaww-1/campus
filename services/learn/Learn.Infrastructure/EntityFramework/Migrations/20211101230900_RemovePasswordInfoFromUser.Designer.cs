﻿// <auto-generated />
using System;
using Learn.Infrastructure.EntityFramework;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

namespace Learn.Infrastructure.EntityFramework.Migrations
{
    [DbContext(typeof(LearnDbContext))]
    [Migration("20211101230900_RemovePasswordInfoFromUser")]
    partial class RemovePasswordInfoFromUser
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("Relational:MaxIdentifierLength", 63)
                .HasAnnotation("ProductVersion", "5.0.11")
                .HasAnnotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn);

            modelBuilder.Entity("Learn.Domain.Users.Role", b =>
                {
                    b.Property<Guid>("Id")
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

            modelBuilder.Entity("Learn.Domain.Users.User", b =>
                {
                    b.Property<Guid>("Id")
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
                    b.HasOne("Learn.Domain.Users.Role", null)
                        .WithMany()
                        .HasForeignKey("role_id")
                        .HasConstraintName("fk_user_role_role_role_id")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("Learn.Domain.Users.User", null)
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