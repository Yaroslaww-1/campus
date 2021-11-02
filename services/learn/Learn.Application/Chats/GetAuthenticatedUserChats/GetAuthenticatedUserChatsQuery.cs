using Ardalis.Specification.EntityFrameworkCore;
using AutoMapper;
using Learn.Application.Chats.Dtos;
using Learn.Application.Chats.Specifications;
using Learn.Application.Users.Specifications;
using Learn.BuildingBlocks.Application.ExecutionContext;
using Learn.Infrastructure.EntityFramework;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Learn.Application.Chats.GetChats
{
    public class GetAuthenticatedUserChatsQuery : IRequest<IEnumerable<ChatDto>>
    {
    }

    internal class GetAuthenticatedUserChatsQueryHandler : IRequestHandler<GetAuthenticatedUserChatsQuery, IEnumerable<ChatDto>>
    {
        private readonly LearnDbContext _dbContext;
        private readonly IMapper _mapper;
        private readonly IUserContext _userContext;

        public GetAuthenticatedUserChatsQueryHandler(LearnDbContext context, IMapper mapper, IUserContext userContext)
        {
            _dbContext = context;
            _mapper = mapper;
            _userContext = userContext;
        }

        public async Task<IEnumerable<ChatDto>> Handle(GetAuthenticatedUserChatsQuery request, CancellationToken cancellationToken)
        {
            var createdBy = await _dbContext.Users
                .WithSpecification(new UserByEmailSpecification(_userContext.Email))
                .AsNoTracking()
                .FirstAsync();

            var chats = await _dbContext.Chats
                .WithSpecification(new ChatAggregateSpecification())
                .WithSpecification(new ChatByCreatorIdSpecification(createdBy.Id))
                .AsNoTracking()
                .ToListAsync();

            return _mapper.Map<IEnumerable<ChatDto>>(chats);
        }
    }
}
