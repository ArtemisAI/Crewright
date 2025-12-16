# PydanticAI Documentation

## Overview
PydanticAI is a Python agent framework designed for building production-grade applications with Generative AI. It leverages Pydantic for validation and type safety.

## Why use PydanticAI?
1. **Built by Pydantic Team**: Uses Pydantic Validation, the standard for many SDKs.
2. **Model-agnostic**: Supports OpenAI, Anthropic, Gemini, DeepSeek, and many others.
3. **Seamless Observability**: Integrates with Pydantic Logfire.
4. **Fully Type-safe**: Designed for IDE autocompletion and type checking.
5. **Powerful Evals**: Systematically test and evaluate performance.
6. **MCP, A2A, and UI**: Integrates with Model Context Protocol and Agent2Agent standards.
7. **Human-in-the-Loop**: Supports tool approval workflows.
8. **Durable Execution**: Handles long-running workflows and failures.
9. **Streamed Outputs**: Supports continuous structured output.
10. **Graph Support**: Define graphs using type hints.

## Hello World Example
```python
from pydantic_ai import Agent

agent = Agent(
    'anthropic:claude-sonnet-4-0',
    instructions='Be concise, reply with one sentence.',
)

result = agent.run_sync('Where does "hello world" come from?')
print(result.output)
```

## Tools & Dependency Injection
PydanticAI supports defining tools and injecting dependencies.

```python
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

@dataclass
class SupportDependencies:
    customer_id: int
    db: DatabaseConn

class SupportOutput(BaseModel):
    support_advice: str
    block_card: bool
    risk: int

support_agent = Agent(
    'openai:gpt-4o',
    deps_type=SupportDependencies,
    output_type=SupportOutput,
    instructions='You are a support agent...',
)

@support_agent.tool
async def customer_balance(ctx: RunContext[SupportDependencies], include_pending: bool) -> float:
    return await ctx.deps.db.customer_balance(
        id=ctx.deps.customer_id,
        include_pending=include_pending,
    )
```

[Source: https://ai.pydantic.dev/]
