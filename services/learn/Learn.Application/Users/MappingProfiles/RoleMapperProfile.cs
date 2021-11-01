﻿using AutoMapper;
using Learn.Application.Users.Dtos;
using Learn.Domain.Users;

namespace Learn.Application.Users.MappingProfiles
{
    public class RoleMapperProfile : Profile
    {
        public RoleMapperProfile()
        {
            CreateMap<Role, RoleDto>();
        }
    }
}