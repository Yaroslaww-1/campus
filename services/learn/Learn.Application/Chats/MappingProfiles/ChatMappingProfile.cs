using AutoMapper;
using Learn.Application.Chats.Dtos;
using Learn.Domain.Chats;
using Learn.Domain.Users;

namespace Learn.Application.Chats.MappingProfiles
{
    public class ChatMappingProfile : Profile
    {
        public ChatMappingProfile()
        {
            CreateMap<ChatMember, ChatMemberDto>();
            CreateMap<Chat, ChatDto>()
                .ForMember(dest => dest.Id, opt => opt.MapFrom(src => src.Id.Value));
        }
    }
}
