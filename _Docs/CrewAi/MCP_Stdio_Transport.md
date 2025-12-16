# Stdio Transport

The Stdio (Standard Input/Output) transport is the most common and secure way to connect MCP (Model Context Protocol) servers to CrewAI agents. It uses standard input and output streams for communication between the agent process and MCP server processes.

## Overview

Stdio transport provides:

- **Process isolation**: Each MCP server runs in its own process
- **Security**: No direct memory access between processes
- **Simplicity**: Easy to configure and deploy
- **Reliability**: Standard stream-based communication

## Basic Configuration

### Simple Stdio Server

```yaml
mcps:
  - name: "filesystem"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
```

### Configuration Parameters

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `name` | string | Unique server identifier | Yes |
| `transport` | string | Must be "stdio" | Yes |
| `command` | string | Executable to run | Yes |
| `args` | array | Command arguments | No |
| `env` | object | Environment variables | No |
| `cwd` | string | Working directory | No |
| `timeout` | number | Connection timeout in seconds | No |

## Common MCP Servers

### File System Server

Access local files and directories:

```yaml
mcps:
  - name: "filesystem"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
    env:
      NODE_ENV: "production"
```

**Capabilities:**
- Read text files
- List directories
- Get file metadata
- Search file contents

### Brave Search Server

Web search capabilities:

```yaml
mcps:
  - name: "brave_search"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-brave-search"]
    env:
      BRAVE_API_KEY: "${BRAVE_API_KEY}"
```

**Features:**
- Web search
- News search
- Location-based results

### Git Server

Git repository operations:

```yaml
mcps:
  - name: "git"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-git", "--repository", "/path/to/repo"]
```

**Operations:**
- View commits
- Read file contents
- Search code
- Get repository status

### SQLite Server

Database access:

```yaml
mcps:
  - name: "sqlite"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "/path/to/database.db"]
```

**Features:**
- Execute SQL queries
- View table schemas
- Export data

### GitHub Server

GitHub API integration:

```yaml
mcps:
  - name: "github"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
```

**Capabilities:**
- Search repositories
- View issues and PRs
- Access file contents
- Get repository information

## Advanced Configuration

### Multiple Directory Access

```yaml
mcps:
  - name: "multi_fs"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/docs", "/data", "/config"]
```

### Environment Variables

```yaml
mcps:
  - name: "configured_server"
    transport: "stdio"
    command: "python"
    args: ["my_mcp_server.py", "--config", "config.json"]
    env:
      API_KEY: "${API_KEY}"
      DEBUG: "true"
      LOG_LEVEL: "${LOG_LEVEL}"
    cwd: "/app"
```

### Timeout Configuration

```yaml
mcps:
  - name: "slow_server"
    transport: "stdio"
    command: "python"
    args: ["slow_mcp_server.py"]
    timeout: 60  # 60 second timeout
```

## Custom MCP Server Development

### Python Stdio Server

```python
#!/usr/bin/env python3
import asyncio
import json
import sys
from mcp import Tool, types
from mcp.server import Server
from mcp.types import TextContent

server = Server("custom-python-server")

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        Tool(
            name="custom_calculator",
            description="Perform advanced calculations",
            inputSchema={
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Mathematical expression"}
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
            # Secure evaluation (in production, use a proper math parser)
            result = eval(expression, {"__builtins__": {}})
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

### Node.js Stdio Server

```javascript
#!/usr/bin/env node

const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js');

class CustomNodeServer {
  constructor() {
    this.server = new Server(
      {
        name: 'custom-node-server',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupToolHandlers();
  }

  setupToolHandlers() {
    this.server.setRequestHandler('tools/list', async () => {
      return {
        tools: [
          {
            name: 'custom_formatter',
            description: 'Format text in various styles',
            inputSchema: {
              type: 'object',
              properties: {
                text: { type: 'string' },
                style: { type: 'string', enum: ['uppercase', 'lowercase', 'title'] }
              },
              required: ['text', 'style']
            }
          }
        ]
      };
    });

    this.server.setRequestHandler('tools/call', async (request) => {
      const { name, arguments: args } = request.params;

      if (name === 'custom_formatter') {
        const { text, style } = args;
        let result;

        switch (style) {
          case 'uppercase':
            result = text.toUpperCase();
            break;
          case 'lowercase':
            result = text.toLowerCase();
            break;
          case 'title':
            result = text.replace(/\w\S*/g, (txt) =>
              txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase()
            );
            break;
          default:
            throw new Error(`Unknown style: ${style}`);
        }

        return {
          content: [{ type: 'text', text: result }]
        };
      }

      throw new Error(`Unknown tool: ${name}`);
    });
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Custom Node.js MCP server running on stdio');
  }
}

const server = new CustomNodeServer();
server.run().catch(console.error);
```

### Configuration for Custom Servers

```yaml
mcps:
  - name: "custom_python"
    transport: "stdio"
    command: "python"
    args: ["custom_server.py"]
    cwd: "/path/to/server"

  - name: "custom_node"
    transport: "stdio"
    command: "node"
    args: ["custom_server.js"]
    env:
      NODE_ENV: "production"
```

## Security Considerations

### Path Restrictions

Limit file system access to specific directories:

```yaml
mcps:
  - name: "secure_filesystem"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/readonly/data"]
    # The server should enforce read-only access
```

### Environment Variable Validation

Validate and sanitize environment variables:

```python
import os

def validate_env_vars():
    required_vars = ['API_KEY', 'DATABASE_URL']
    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Required environment variable {var} not set")
    
    # Validate API key format
    api_key = os.getenv('API_KEY')
    if not api_key or len(api_key) < 32:
        raise ValueError("Invalid API key format")

validate_env_vars()
```

### Process Isolation

Each MCP server runs in its own process, providing:

- Memory isolation
- Crash containment
- Resource limits per server

## Performance Optimization

### Connection Pooling

Stdio transport handles connection pooling automatically through process management.

### Resource Limits

Set resource limits for MCP server processes:

```yaml
mcps:
  - name: "resource_limited"
    transport: "stdio"
    command: "python"
    args: ["memory_intensive_server.py"]
    # Process will be limited by system ulimits
```

### Caching

Implement caching in your MCP servers:

```python
from functools import lru_cache
import asyncio

@lru_cache(maxsize=100)
def expensive_operation(param):
    # Expensive computation
    return result

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "cached_tool":
        result = expensive_operation(arguments["param"])
        return [TextContent(type="text", text=result)]
```

## Error Handling

### Server Startup Failures

Handle server startup failures gracefully:

```python
import subprocess
import asyncio

async def start_mcp_server(config):
    try:
        process = await asyncio.create_subprocess_exec(
            config["command"],
            *config.get("args", []),
            env=config.get("env", {}),
            cwd=config.get("cwd"),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to be ready
        await asyncio.wait_for(process.wait(), timeout=config.get("timeout", 10))
        
        return process
    except asyncio.TimeoutError:
        print(f"MCP server {config['name']} failed to start within timeout")
        raise
    except Exception as e:
        print(f"Failed to start MCP server {config['name']}: {e}")
        raise
```

### Communication Errors

Handle communication errors between agent and server:

```python
async def call_mcp_tool(server_process, tool_name, args):
    try:
        # Send request to server
        request = json.dumps({
            "method": "tools/call",
            "params": {"name": tool_name, "arguments": args}
        })
        
        server_process.stdin.write(request.encode())
        await server_process.stdin.drain()
        
        # Read response
        response_data = await server_process.stdout.read(4096)
        response = json.loads(response_data.decode())
        
        return response
    except json.JSONDecodeError:
        print("Invalid JSON response from MCP server")
        return None
    except Exception as e:
        print(f"MCP communication error: {e}")
        return None
```

## Monitoring and Logging

### Server Process Monitoring

Monitor MCP server processes:

```python
import psutil

def monitor_mcp_processes(mcp_configs):
    for config in mcp_configs:
        if config.get("transport") == "stdio":
            # Find process by command
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                if config["command"] in proc.info['cmdline']:
                    print(f"MCP server {config['name']} running (PID: {proc.info['pid']})")
                    break
```

### Logging Configuration

Configure logging for MCP servers:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('mcp_stdio')

# Log MCP server events
logger.info(f"Starting MCP server: {config['name']}")
logger.error(f"MCP server {config['name']} failed: {error}")
```

## Testing Stdio MCP Servers

### Unit Testing

```python
import pytest
from unittest.mock import patch, MagicMock

def test_stdio_server_startup():
    config = {
        "name": "test_server",
        "transport": "stdio",
        "command": "python",
        "args": ["test_server.py"]
    }
    
    with patch('asyncio.create_subprocess_exec') as mock_subprocess:
        mock_process = MagicMock()
        mock_subprocess.return_value = mock_process
        
        # Test server startup
        process = await start_mcp_server(config)
        
        mock_subprocess.assert_called_once_with(
            "python", "test_server.py",
            env={}, cwd=None,
            stdin=-1, stdout=-1, stderr=-1
        )

def test_stdio_tool_call():
    # Mock server process
    mock_process = MagicMock()
    
    # Test tool call
    result = await call_mcp_tool(mock_process, "test_tool", {"param": "value"})
    
    # Verify communication
    assert mock_process.stdin.write.called
    assert mock_process.stdout.read.called
```

### Integration Testing

```python
def test_full_stdio_integration():
    # Start actual MCP server
    config = {
        "name": "integration_test",
        "transport": "stdio",
        "command": "python",
        "args": ["test_mcp_server.py"]
    }
    
    # Start server
    process = await start_mcp_server(config)
    
    try:
        # Test tool listing
        tools = await call_mcp_tool(process, "tools/list", {})
        assert "tools" in tools
        
        # Test tool execution
        result = await call_mcp_tool(process, "test_tool", {"input": "test"})
        assert result is not None
        
    finally:
        # Cleanup
        process.terminate()
        await process.wait()
```

## Best Practices

### 1. Server Resource Management

```python
class MCPManager:
    def __init__(self):
        self.servers = {}
    
    async def start_server(self, config):
        if config["name"] in self.servers:
            return self.servers[config["name"]]
        
        process = await start_mcp_server(config)
        self.servers[config["name"]] = process
        return process
    
    async def stop_all_servers(self):
        for name, process in self.servers.items():
            process.terminate()
            await process.wait()
        
        self.servers.clear()
```

### 2. Error Recovery

```python
async def call_tool_with_retry(server_config, tool_name, args, max_retries=3):
    for attempt in range(max_retries):
        try:
            process = await start_mcp_server(server_config)
            result = await call_mcp_tool(process, tool_name, args)
            return result
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            print(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
```

### 3. Configuration Validation

```python
def validate_stdio_config(config):
    required_fields = ["name", "transport", "command"]
    
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field: {field}")
    
    if config["transport"] != "stdio":
        raise ValueError("Transport must be 'stdio'")
    
    if not isinstance(config.get("args", []), list):
        raise ValueError("args must be a list")
    
    if not isinstance(config.get("env", {}), dict):
        raise ValueError("env must be a dictionary")
```

## Troubleshooting

### Common Issues

1. **Server won't start**: Check command path, arguments, and permissions
2. **Communication failures**: Verify JSON message format and encoding
3. **Timeout errors**: Increase timeout values or optimize server performance
4. **Process crashes**: Check server logs and error handling

### Debug Mode

Enable debug logging for stdio transport:

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Enable asyncio debug mode
asyncio.get_event_loop().set_debug(True)

# Log all stdio communication
logger = logging.getLogger('mcp.stdio')
logger.setLevel(logging.DEBUG)
```

## Next Steps

- Learn about [SSE Transport](https://docs.crewai.com/en/mcp/sse-transport) for real-time communication
- Explore [HTTP Transport](https://docs.crewai.com/en/mcp/streamable-http-transport) for web-based servers
- Check out [DSL Integration](https://docs.crewai.com/en/mcp/dsl-integration) for configuration options
- Read about [Multiple Servers](https://docs.crewai.com/en/mcp/multiple-servers) for complex setups
- Review [Security Considerations](https://docs.crewai.com/en/mcp/security) for secure deployments