using Learn.Application.Chats.CreateChat;
using Learn.Application.Chats.Dtos;
using Learn.Application.Chats.GetChats;
using MediatR;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Learn.API.Controllers.Chats
{
    [ApiController]
    [Route("chats")]
    public class ChatsController : ControllerBase
    {
        private readonly ISender _mediator;

        public ChatsController(ISender mediator)
        {
            _mediator = mediator;
        }

        [HttpGet("my")]
        [ProducesResponseType(typeof(IEnumerable<ChatDto>), StatusCodes.Status200OK)]
        public async Task<IEnumerable<ChatDto>> Create()
        {
            var result = await _mediator.Send(new GetAuthenticatedUserChatsQuery());
            return result;
        }

        [HttpPost]
        [ProducesResponseType(typeof(ChatDto), StatusCodes.Status200OK)]
        public async Task<ChatDto> Create([FromBody] CreateChatRequest request)
        {
            var result = await _mediator.Send(new CreateChatCommand(request.Name));
            return result;
        }
    }
}
