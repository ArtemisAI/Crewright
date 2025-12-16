# DSL Integration

The CrewAI DSL (Domain Specific Language) provides a powerful way to integrate MCP (Model Context Protocol) servers directly into your agent configurations. This allows agents to leverage external tools and services through a standardized protocol.

## Overview

MCP integration in CrewAI allows you to:

- Connect agents to external MCP servers
- Use standardized tool calling protocols
- Extend agent capabilities with third-party services
- Maintain security through isolated server processes

## Basic MCP Configuration

### Adding MCP Servers to Agents

You can configure MCP servers directly in your agent YAML configuration:

**agents.yaml**
```yaml
research_agent:
  role: "Research Analyst"
  goal: "Conduct comprehensive research using various tools"
  backstory: "Expert researcher with access to multiple data sources and analysis tools"
  llm: "gpt-4"
  mcps:
    - name: "web_search"
      transport: "stdio"
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-brave-search"]
      env:
        BRAVE_API_KEY: "${BRAVE_API_KEY}"
    - name: "file_system"
      transport: "stdio"
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
```

### MCP Server Definition

Each MCP server in the `mcps` array requires:

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `name` | string | Unique identifier for the server | Yes |
| `transport` | string | Transport type (`stdio`, `sse`, `http`) | Yes |
| `command` | string | Executable command to start the server | Yes (for stdio) |
| `args` | array | Command arguments | No |
| `env` | object | Environment variables | No |
| `url` | string | Server URL for HTTP/SSE transports | Yes (for http/sse) |
| `headers` | object | HTTP headers for requests | No |

## Transport Types

### Stdio Transport

The most common transport for MCP servers. The server communicates via standard input/output streams.

```yaml
mcps:
  - name: "filesystem"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
```

### SSE Transport

Server-Sent Events transport for real-time communication.

```yaml
mcps:
  - name: "realtime_data"
    transport: "sse"
    url: "https://api.example.com/mcp/sse"
    headers:
      Authorization: "Bearer ${API_TOKEN}"
```

### HTTP Transport (Streamable)

HTTP-based transport with streaming capabilities.

```yaml
mcps:
  - name: "api_service"
    transport: "http"
    url: "https://api.example.com/mcp"
    headers:
      Authorization: "Bearer ${API_TOKEN}"
      Content-Type: "application/json"
```

## MCP Server Examples

### Brave Search Server

```yaml
mcps:
  - name: "brave_search"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-brave-search"]
    env:
      BRAVE_API_KEY: "${BRAVE_API_KEY}"
```

### File System Server

```yaml
mcps:
  - name: "filesystem"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp", "/home/user/docs"]
```

### GitHub Server

```yaml
mcps:
  - name: "github"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
```

### SQLite Server

```yaml
mcps:
  - name: "sqlite"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "/path/to/database.db"]
```

### Slack Server

```yaml
mcps:
  - name: "slack"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-slack"]
    env:
      SLACK_BOT_TOKEN: "${SLACK_BOT_TOKEN}"
```

## Advanced MCP Configuration

### Multiple Servers

Agents can use multiple MCP servers simultaneously:

```yaml
data_analyst:
  role: "Data Analyst"
  goal: "Analyze data from multiple sources"
  backstory: "Expert analyst with access to various data tools and services"
  mcps:
    - name: "database"
      transport: "stdio"
      command: "python"
      args: ["-m", "my_mcp_server", "--db", "production.db"]
    - name: "api_client"
      transport: "http"
      url: "https://data-api.company.com/mcp"
      headers:
        Authorization: "Bearer ${API_KEY}"
    - name: "filesystem"
      transport: "stdio"
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-filesystem", "/data"]
```

### Environment Variable Interpolation

Use environment variables in MCP configurations:

```yaml
mcps:
  - name: "secure_api"
    transport: "http"
    url: "${API_BASE_URL}/mcp"
    headers:
      Authorization: "Bearer ${API_TOKEN}"
      X-API-Key: "${API_KEY}"
    env:
      DEBUG: "${DEBUG_MODE}"
```

### Conditional MCP Loading

Load MCP servers based on environment or configuration:

```python
# In your crew configuration
import os

def get_mcp_config():
    mcps = []
    
    # Always load filesystem
    mcps.append({
        "name": "filesystem",
        "transport": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
    })
    
    # Load search only in development
    if os.getenv("ENVIRONMENT") == "development":
        mcps.append({
            "name": "brave_search",
            "transport": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search"],
            "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
        })
    
    # Load production APIs only in production
    if os.getenv("ENVIRONMENT") == "production":
        mcps.append({
            "name": "prod_api",
            "transport": "http",
            "url": os.getenv("PROD_API_URL"),
            "headers": {"Authorization": f"Bearer {os.getenv('PROD_API_TOKEN')}"}
        })
    
    return mcps
```

## MCP Server Development

### Creating Custom MCP Servers

You can create custom MCP servers to extend CrewAI capabilities:

```python
# custom_mcp_server.py
import asyncio
import json
import sys
from mcp import Tool, types
from mcp.server import Server
from mcp.types import TextContent, PromptMessage

server = Server("custom-server")

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        Tool(
            name="custom_calculator",
            description="Perform custom calculations",
            inputSchema={
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "custom_calculator":
        expression = arguments["expression"]
        try:
            result = eval(expression)
            return [TextContent(type="text", text=str(result))]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {str(e)}")]
    else:
        raise ValueError(f"Unknown tool: {name}")

async def main():
    async with server.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Integrating Custom Servers

```yaml
mcps:
  - name: "custom_calculator"
    transport: "stdio"
    command: "python"
    args: ["custom_mcp_server.py"]
```

## MCP Tool Discovery

### Automatic Tool Registration

When you add MCP servers to an agent, their tools are automatically discovered and made available:

```python
from crewai import Agent

agent = Agent(
    config=agent_config,  # Contains MCP server definitions
    verbose=True
)

# The agent now has access to all tools from configured MCP servers
# Tools are called automatically when the agent determines they're needed
```

### Tool Listing

You can inspect available MCP tools programmatically:

```python
# Get all available tools for an agent
all_tools = agent.tools

# Filter MCP tools
mcp_tools = [tool for tool in all_tools if hasattr(tool, 'mcp_server')]

for tool in mcp_tools:
    print(f"MCP Tool: {tool.name} from server: {tool.mcp_server}")
```

## Security Considerations

### Server Isolation

MCP servers run in separate processes, providing isolation:

- Each server runs in its own process
- Stdio transport prevents direct memory access
- HTTP/SSE transports can use network isolation

### Access Control

Implement access controls in your MCP configurations:

```yaml
# Restrict filesystem access
mcps:
  - name: "secure_filesystem"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/read/path"]
    # Note: The server itself should enforce read-only access
```

### Environment Variable Security

Use secure environment variable handling:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

# Validate required environment variables
required_env_vars = ['BRAVE_API_KEY', 'GITHUB_TOKEN']
for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"Required environment variable {var} not set")

mcps_config = [
    {
        "name": "brave_search",
        "transport": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-brave-search"],
        "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
    }
]
```

## Performance Optimization

### Connection Pooling

For HTTP-based MCP servers, consider connection pooling:

```yaml
mcps:
  - name: "api_service"
    transport: "http"
    url: "https://api.example.com/mcp"
    headers:
      Authorization: "Bearer ${API_TOKEN}"
      Connection: "keep-alive"
    # The underlying HTTP client will handle connection pooling
```

### Caching

Implement caching for expensive MCP operations:

```python
# In your custom MCP server
from functools import lru_cache
import time

@server.call_tool()
@lru_cache(maxsize=100)
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    # Expensive operation with caching
    result = expensive_computation(arguments)
    return [TextContent(type="text", text=result)]
```

### Async Operations

Use async operations for better performance:

```python
@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    # Async database query
    result = await database_query(arguments["query"])
    return [TextContent(type="text", text=result)]
```

## Error Handling

### MCP Server Failures

Handle MCP server failures gracefully:

```python
try:
    result = await agent.execute_task(task)
except MCPConnectionError as e:
    print(f"MCP server connection failed: {e}")
    # Fallback to alternative tools or manual processing
except MCPToolError as e:
    print(f"MCP tool execution failed: {e}")
    # Retry or use alternative approach
```

### Timeout Configuration

Configure timeouts for MCP operations:

```yaml
mcps:
  - name: "slow_api"
    transport: "http"
    url: "https://slow-api.example.com/mcp"
    timeout: 30  # 30 second timeout
```

## Monitoring and Logging

### MCP Activity Logging

Enable logging for MCP server activities:

```python
import logging

logging.basicConfig(level=logging.INFO)

# MCP server logs will be captured
agent = Agent(
    config=agent_config,
    verbose=True  # Enable detailed logging
)
```

### Performance Monitoring

Monitor MCP server performance:

```python
import time

class MonitoredAgent(Agent):
    async def execute_tool(self, tool_name, **kwargs):
        start_time = time.time()
        try:
            result = await super().execute_tool(tool_name, **kwargs)
            duration = time.time() - start_time
            print(f"MCP Tool {tool_name} executed in {duration:.2f}s")
            return result
        except Exception as e:
            duration = time.time() - start_time
            print(f"MCP Tool {tool_name} failed after {duration:.2f}s: {e}")
            raise
```

## Best Practices

### 1. Server Selection

Choose appropriate MCP servers for your use case:

```yaml
# Good: Focused servers for specific domains
research_agent_mcps:
  - name: "web_search"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-brave-search"]
  - name: "academic_search"
    transport: "http"
    url: "https://academic-search-api.com/mcp"

# Avoid: Too many servers overwhelming the agent
overloaded_agent_mcps:
  - name: "search1"
  - name: "search2"
  - name: "api1"
  - name: "api2"
  - name: "filesystem"
  - name: "database"
  # ... many more
```

### 2. Error Boundaries

Implement error boundaries around MCP operations:

```python
class RobustAgent(Agent):
    async def safe_execute_mcp_tool(self, tool_name, **kwargs):
        try:
            return await self.execute_tool(tool_name, **kwargs)
        except Exception as e:
            # Log error
            logger.error(f"MCP tool {tool_name} failed: {e}")
            # Return fallback result or raise specific error
            return self.get_fallback_result(tool_name, **kwargs)
```

### 3. Resource Management

Manage MCP server resources appropriately:

```python
# Cleanup MCP servers when done
async def cleanup_mcp_servers(agent):
    for mcp_config in agent.mcps:
        if mcp_config.get("transport") == "stdio":
            # Terminate stdio processes
            await terminate_process(mcp_config["process"])
```

### 4. Testing

Test MCP integrations thoroughly:

```python
def test_mcp_integration():
    agent = Agent(config=test_agent_config)
    
    # Test tool discovery
    assert len(agent.tools) > 0
    
    # Test tool execution
    result = agent.execute_tool("test_tool", param="value")
    assert result is not None
    
    # Test error handling
    with pytest.raises(MCPError):
        agent.execute_tool("nonexistent_tool")
```

## Troubleshooting

### Common Issues

1. **Server won't start**: Check command, arguments, and environment variables
2. **Connection failures**: Verify URLs, headers, and network connectivity
3. **Tool not found**: Ensure server is properly configured and tools are registered
4. **Performance issues**: Monitor server logs and optimize configurations

### Debugging MCP

Enable debug logging for MCP operations:

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Enable MCP-specific debug logging
logger = logging.getLogger("mcp")
logger.setLevel(logging.DEBUG)
```

## Next Steps

- Learn about [Stdio Transport](https://docs.crewai.com/en/mcp/stdio-transport) for local MCP servers
- Explore [SSE Transport](https://docs.crewai.com/en/mcp/sse-transport) for real-time communication
- Check out [HTTP Transport](https://docs.crewai.com/en/mcp/streamable-http-transport) for web-based MCP servers
- Read about [Multiple Servers](https://docs.crewai.com/en/mcp/multiple-servers) for complex integrations
- Review [Security Considerations](https://docs.crewai.com/en/mcp/security) for secure MCP usage