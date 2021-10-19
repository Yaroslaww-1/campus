using System;

namespace Users.BuildingBlocks.ExecutionContext
{
    public interface IExecutionContextAccessor
    {
        Guid UserId { get; }
    }
}
