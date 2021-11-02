using AutoMapper;
using Learn.Application.Users.Dtos;
using Learn.Domain.Users;

namespace Learn.Application.Users.MappingProfiles
{
    public class UserMapperProfile : Profile
    {
        public UserMapperProfile()
        {
            CreateMap<User, UserDto>()
                .ForMember(dest => dest.Id, opt => opt.MapFrom(src => src.Id.Value));
        }
    }
}
