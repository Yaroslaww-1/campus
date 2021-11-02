using Ardalis.Specification.EntityFrameworkCore;
using AutoMapper;
using Learn.Application.Chats.Dtos;
using Learn.Application.Users.Dtos;
using Learn.Application.Users.Specifications;
using Learn.BuildingBlocks.Application.ExecutionContext;
using Learn.Domain.Chats;
using Learn.Domain.Users;
using Learn.Infrastructure.EntityFramework;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Learn.Application.Chats.CreateChat
{
    public class CreateChatCommand : IRequest<ChatDto>
    {
        public string Name { get; set; }

        public CreateChatCommand(string name)
        {
            Name = name;
        }
    }

    internal class CreateChatCommandHandler : IRequestHandler<CreateChatCommand, ChatDto>
    {
        private readonly LearnDbContext _dbContext;
        private readonly IChatRepository _chatRepository;
        private readonly IMapper _mapper;
        private readonly IUserContext _userContext;

        public CreateChatCommandHandler(LearnDbContext dbContext, IChatRepository chatRepository, IMapper mapper, IUserContext userContext)
        {
            _dbContext = dbContext;
            _chatRepository = chatRepository;
            _mapper = mapper;
            _userContext = userContext;
        }

        public async Task<ChatDto> Handle(CreateChatCommand request, CancellationToken cancellationToken)
        {
            var createdBy = await _dbContext.Users
                .WithSpecification(new UserAggregateSpecification())
                .WithSpecification(new UserByEmailSpecification(_userContext.Email))
                .FirstAsync();

            var chat = Chat.CreateNew(request.Name, createdBy);

            await _chatRepository.AddAsync(chat);

            return _mapper.Map<ChatDto>(chat);
        }
    }
}
