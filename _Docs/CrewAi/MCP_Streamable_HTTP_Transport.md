# Streamable HTTP Transport

The Streamable HTTP transport provides request-response communication between CrewAI agents and MCP (Model Context Protocol) servers over HTTP. Unlike SSE transport which is event-driven, HTTP transport uses traditional request-response patterns with optional streaming capabilities.

## Overview

HTTP transport offers:

- **Request-response communication**: Traditional HTTP API patterns
- **Streaming support**: Optional streaming for large responses
- **Web compatibility**: Works with existing HTTP APIs and web services
- **Load balancing**: Easy integration with load balancers and proxies

## Basic Configuration

### Simple HTTP Server

```yaml
mcps:
  - name: "api_service"
    transport: "http"
    url: "https://api.example.com/mcp"
    headers:
      Authorization: "Bearer ${API_TOKEN}"
```

### Configuration Parameters

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `name` | string | Unique server identifier | Yes |
| `transport` | string | Must be "http" | Yes |
| `url` | string | Base URL for HTTP requests | Yes |
| `headers` | object | Default HTTP headers | No |
| `timeout` | number | Request timeout in seconds | No |
| `retries` | number | Number of retry attempts | No |
| `retry_delay` | number | Delay between retries in seconds | No |

## HTTP MCP Server Implementation

### Basic HTTP Server

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from mcp import Tool, types
from mcp.server import Server
from mcp.types import TextContent

app = FastAPI()
server = Server("http-mcp-server")

class ToolCallRequest(BaseModel):
    method: str
    params: dict = {}

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        Tool(
            name="data_processor",
            description="Process and analyze data",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string"},
                    "operation": {"type": "string", "enum": ["analyze", "summarize", "transform"]}
                },
                "required": ["data", "operation"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "data_processor":
        data = arguments["data"]
        operation = arguments["operation"]
        
        if operation == "analyze":
            result = f"Analysis of: {data[:100]}..."
        elif operation == "summarize":
            result = f"Summary: {data[:50]}..."
        elif operation == "transform":
            result = f"Transformed: {data.upper()}"
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        return [TextContent(type="text", text=result)]
    else:
        raise ValueError(f"Unknown tool: {name}")

@app.post("/mcp")
async def mcp_endpoint(request: ToolCallRequest):
    """Handle MCP requests over HTTP"""
    try:
        if request.method == "tools/list":
            tools = await list_tools()
            return {"tools": [tool.dict() for tool in tools]}
        elif request.method == "tools/call":
            result = await call_tool(
                request.params["name"], 
                request.params.get("arguments", {})
            )
            return {"content": [content.dict() for content in result]}
        else:
            raise HTTPException(status_code=400, detail=f"Unknown method: {request.method}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Node.js HTTP Server

```javascript
const express = require('express');
const { Server } = require('@modelcontextprotocol/sdk/server/index.js');

const app = express();
app.use(express.json());

const server = new Server(
  {
    name: 'http-node-server',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Setup tool handlers
server.setRequestHandler('tools/list', async () => {
  return {
    tools: [
      {
        name: 'text_analyzer',
        description: 'Analyze text content',
        inputSchema: {
          type: 'object',
          properties: {
            text: { type: 'string' },
            analysis_type: { 
              type: 'string', 
              enum: ['sentiment', 'keywords', 'summary'] 
            }
          },
          required: ['text', 'analysis_type']
        }
      }
    ]
  };
});

server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;

  if (name === 'text_analyzer') {
    const { text, analysis_type } = args;
    
    let result;
    switch (analysis_type) {
      case 'sentiment':
        result = `Sentiment analysis of: ${text.substring(0, 50)}...`;
        break;
      case 'keywords':
        result = `Keywords: ${text.split(' ').slice(0, 5).join(', ')}`;
        break;
      case 'summary':
        result = `Summary: ${text.substring(0, 100)}...`;
        break;
      default:
        throw new Error(`Unknown analysis type: ${analysis_type}`);
    }

    return {
      content: [{ type: 'text', text: result }]
    };
  }

  throw new Error(`Unknown tool: ${name}`);
});

// HTTP endpoint
app.post('/mcp', async (req, res) => {
  try {
    const response = await server.processRequest(req.body);
    res.json(response);
  } catch (error) {
    res.status(error.status || 500).json({ 
      error: { 
        message: error.message,
        code: error.code || 'INTERNAL_ERROR'
      }
    });
  }
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

app.listen(3000, () => {
  console.log('HTTP MCP server listening on port 3000');
});
```

## Advanced HTTP Configuration

### Authentication and Headers

```yaml
mcps:
  - name: "secure_api"
    transport: "http"
    url: "https://secure-api.example.com/mcp"
    headers:
      Authorization: "Bearer ${JWT_TOKEN}"
      X-API-Key: "${API_KEY}"
      X-Client-ID: "${CLIENT_ID}"
      Content-Type: "application/json"
      User-Agent: "CrewAI-Agent/1.0"
```

### Retry and Timeout Configuration

```yaml
mcps:
  - name: "reliable_api"
    transport: "http"
    url: "https://api.example.com/mcp"
    timeout: 30
    retries: 3
    retry_delay: 2
    headers:
      Authorization: "Bearer ${TOKEN}"
```

### Multiple HTTP Servers

```yaml
mcps:
  - name: "user_service"
    transport: "http"
    url: "https://user-api.example.com/mcp"
    headers:
      Authorization: "Bearer ${USER_TOKEN}"
  
  - name: "product_service"
    transport: "http"
    url: "https://product-api.example.com/mcp"
    headers:
      Authorization: "Bearer ${PRODUCT_TOKEN}"
  
  - name: "analytics_service"
    transport: "http"
    url: "https://analytics-api.example.com/mcp"
    headers:
      Authorization: "Bearer ${ANALYTICS_TOKEN}"
```

## HTTP Client Implementation

### Basic HTTP Client

```python
import aiohttp
import json
from typing import Dict, Any

class MCPHTTPClient:
    def __init__(self, base_url: str, headers: Dict[str, str] = None, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.headers = headers or {}
        self.timeout = timeout
        
    async def list_tools(self) -> Dict[str, Any]:
        """List available tools"""
        return await self._make_request("tools/list")
    
    async def call_tool(self, name: str, arguments: Dict[str, Any] = None) -> Dict[str, Any]:
        """Call a specific tool"""
        params = {"name": name}
        if arguments:
            params["arguments"] = arguments
        
        return await self._make_request("tools/call", params)
    
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make HTTP request to MCP server"""
        payload = {"method": method}
        if params:
            payload["params"] = params
        
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(
                f"{self.base_url}",
                json=payload,
                timeout=aiohttp.ClientTimeout(total=self.timeout)
            ) as response:
                response.raise_for_status()
                return await response.json()
```

### Advanced HTTP Client with Retry

```python
import asyncio
import logging
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

logger = logging.getLogger(__name__)

class ResilientMCPHTTPClient(MCPHTTPClient):
    def __init__(self, *args, retries: int = 3, **kwargs):
        super().__init__(*args, **kwargs)
        self.retries = retries
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((aiohttp.ClientError, asyncio.TimeoutError))
    )
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make HTTP request with retry logic"""
        try:
            result = await super()._make_request(method, params)
            return result
        except aiohttp.ClientResponseError as e:
            if e.status >= 500:
                logger.warning(f"Server error {e.status}, retrying: {e}")
                raise  # Will be retried
            else:
                logger.error(f"Client error {e.status}: {e}")
                raise  # Won't be retried
        except Exception as e:
            logger.error(f"Request failed: {e}")
            raise
```

## Streaming HTTP Support

### Server-Sent Events over HTTP

```python
from fastapi.responses import StreamingResponse
import json

@app.post("/mcp/stream")
async def streaming_mcp_endpoint(request: ToolCallRequest):
    """Handle streaming MCP requests"""
    
    async def generate_response():
        try:
            if request.method == "tools/call":
                # Simulate streaming response
                tool_name = request.params["name"]
                arguments = request.params.get("arguments", {})
                
                # Initial response
                yield f"data: {json.dumps({'status': 'processing', 'tool': tool_name})}\n\n"
                
                # Simulate processing steps
                for i in range(3):
                    await asyncio.sleep(0.5)
                    yield f"data: {json.dumps({'progress': (i+1)/3, 'step': i+1})}\n\n"
                
                # Final result
                result = await call_tool(tool_name, arguments)
                yield f"data: {json.dumps({'result': result, 'status': 'complete'})}\n\n"
                
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e), 'status': 'failed'})}\n\n"
    
    return StreamingResponse(
        generate_response(),
        media_type="text/plain",
        headers={"Content-Type": "text/event-stream"}
    )
```

### Client Streaming Support

```python
class StreamingMCPHTTPClient(MCPHTTPClient):
    async def call_tool_streaming(self, name: str, arguments: Dict[str, Any] = None):
        """Call tool with streaming response"""
        params = {"name": name}
        if arguments:
            params["arguments"] = arguments
        
        payload = {"method": "tools/call", "params": params}
        
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(
                f"{self.base_url}/stream",
                json=payload,
                timeout=aiohttp.ClientTimeout(total=self.timeout)
            ) as response:
                response.raise_for_status()
                
                async for line in response.content:
                    line = line.decode('utf-8').strip()
                    
                    if line.startswith('data: '):
                        data = line[6:]
                        try:
                            event_data = json.loads(data)
                            yield event_data
                        except json.JSONDecodeError:
                            continue

# Usage
client = StreamingMCPHTTPClient("https://api.example.com/mcp")
async for event in client.call_tool_streaming("data_processor", {"data": "large_dataset"}):
    print(f"Event: {event}")
```

## Error Handling

### HTTP Error Handling

```python
class ErrorHandlingMCPHTTPClient(MCPHTTPClient):
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make request with comprehensive error handling"""
        try:
            return await super()._make_request(method, params)
        except aiohttp.ClientResponseError as e:
            error_details = {
                "status_code": e.status,
                "message": e.message,
                "method": method,
                "url": str(e.request_info.url)
            }
            
            if e.status == 401:
                raise MCPAuthenticationError("Authentication failed", details=error_details)
            elif e.status == 403:
                raise MCPAuthorizationError("Access forbidden", details=error_details)
            elif e.status == 404:
                raise MCPNotFoundError("Resource not found", details=error_details)
            elif e.status == 429:
                raise MCRateLimitError("Rate limit exceeded", details=error_details)
            elif e.status >= 500:
                raise MCPServerError("Server error", details=error_details)
            else:
                raise MCPHTTPError(f"HTTP {e.status}: {e.message}", details=error_details)
                
        except asyncio.TimeoutError:
            raise MCPTimeoutError(f"Request timed out after {self.timeout}s")
        except aiohttp.ClientError as e:
            raise MCPConnectionError(f"Connection error: {str(e)}")
        except json.JSONDecodeError as e:
            raise MCPParseError(f"Invalid JSON response: {str(e)}")

# Custom exceptions
class MCPError(Exception):
    def __init__(self, message: str, details: Dict[str, Any] = None):
        super().__init__(message)
        self.details = details or {}

class MCPAuthenticationError(MCPError): pass
class MCPAuthorizationError(MCPError): pass
class MCPNotFoundError(MCPError): pass
class MCRateLimitError(MCPError): pass
class MCPServerError(MCPError): pass
class MCPHTTPError(MCPError): pass
class MCPTimeoutError(MCPError): pass
class MCPConnectionError(MCPError): pass
class MCPParseError(MCPError): pass
```

## Security Considerations

### SSL/TLS Configuration

```python
import ssl

# Custom SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = True
ssl_context.verify_mode = ssl.CERT_REQUIRED

# Or for development with self-signed certificates
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

connector = aiohttp.TCPConnector(ssl=ssl_context)

class SecureMCPHTTPClient(MCPHTTPClient):
    def __init__(self, *args, ssl_context=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.ssl_context = ssl_context
    
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        connector = aiohttp.TCPConnector(ssl=self.ssl_context) if self.ssl_context else None
        
        async with aiohttp.ClientSession(connector=connector, headers=self.headers) as session:
            # Make request with custom SSL
            pass
```

### Request Signing

```python
import hmac
import hashlib
import time

class SignedMCPHTTPClient(MCPHTTPClient):
    def __init__(self, *args, api_key: str, api_secret: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_key = api_key
        self.api_secret = api_secret
    
    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, str]:
        """Generate request signature"""
        timestamp = str(int(time.time()))
        message = f"{self.api_key}{timestamp}{json.dumps(payload, sort_keys=True)}"
        
        signature = hmac.new(
            self.api_secret.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return {
            "X-API-Key": self.api_key,
            "X-Timestamp": timestamp,
            "X-Signature": signature
        }
    
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        payload = {"method": method}
        if params:
            payload["params"] = params
        
        # Add signature headers
        signature_headers = self._sign_request(payload)
        headers = {**self.headers, **signature_headers}
        
        async with aiohttp.ClientSession(headers=headers) as session:
            # Make signed request
            pass
```

## Performance Optimization

### Connection Pooling

```python
# Configure connection pooling
connector = aiohttp.TCPConnector(
    limit=20,  # Max connections
    limit_per_host=5,  # Max connections per host
    ttl_dns_cache=300,  # DNS cache TTL (5 minutes)
    use_dns_cache=True,
    keepalive_timeout=60,
    enable_cleanup_closed=True
)

class PooledMCPHTTPClient(MCPHTTPClient):
    def __init__(self, *args, connector=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.connector = connector or aiohttp.TCPConnector(limit=10)
    
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        async with aiohttp.ClientSession(
            connector=self.connector, 
            headers=self.headers
        ) as session:
            # Reuse connections
            pass
```

### Response Caching

```python
from functools import lru_cache
import hashlib

class CachedMCPHTTPClient(MCPHTTPClient):
    def __init__(self, *args, cache_ttl: int = 300, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_ttl = cache_ttl
        self.cache = {}
    
    def _get_cache_key(self, method: str, params: Dict[str, Any]) -> str:
        """Generate cache key"""
        key_data = f"{method}:{json.dumps(params, sort_keys=True)}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        cache_key = self._get_cache_key(method, params or {})
        current_time = time.time()
        
        # Check cache
        if cache_key in self.cache:
            cached_result, timestamp = self.cache[cache_key]
            if current_time - timestamp < self.cache_ttl:
                return cached_result
        
        # Make request
        result = await super()._make_request(method, params)
        
        # Cache result
        self.cache[cache_key] = (result, current_time)
        
        return result
```

### Compression

```yaml
mcps:
  - name: "compressed_api"
    transport: "http"
    url: "https://api.example.com/mcp"
    headers:
      Accept-Encoding: "gzip, deflate, br"
      Authorization: "Bearer ${TOKEN}"
```

## Monitoring and Logging

### Request Logging

```python
import logging
import time

logger = logging.getLogger(__name__)

class LoggingMCPHTTPClient(MCPHTTPClient):
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        request_id = f"{method}_{int(time.time() * 1000)}"
        
        logger.info(f"[{request_id}] Starting {method} request")
        if params:
            logger.debug(f"[{request_id}] Params: {params}")
        
        start_time = time.time()
        try:
            result = await super()._make_request(method, params)
            duration = time.time() - start_time
            
            logger.info(f"[{request_id}] Completed in {duration:.2f}s")
            logger.debug(f"[{request_id}] Result: {result}")
            
            return result
        except Exception as e:
            duration = time.time() - start_time
            logger.error(f"[{request_id}] Failed after {duration:.2f}s: {e}")
            raise
```

### Metrics Collection

```python
from collections import defaultdict
import statistics

class MetricsMCPHTTPClient(LoggingMCPHTTPClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.metrics = defaultdict(list)
    
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        start_time = time.time()
        try:
            result = await super()._make_request(method, params)
            duration = time.time() - start_time
            
            self.metrics['request_duration'].append(duration)
            self.metrics['successful_requests'].append(1)
            
            return result
        except Exception as e:
            duration = time.time() - start_time
            
            self.metrics['request_duration'].append(duration)
            self.metrics['failed_requests'].append(1)
            
            raise
    
    def get_metrics(self):
        """Get performance metrics"""
        durations = self.metrics['request_duration']
        
        return {
            'total_requests': len(durations),
            'successful_requests': len(self.metrics['successful_requests']),
            'failed_requests': len(self.metrics['failed_requests']),
            'avg_response_time': statistics.mean(durations) if durations else 0,
            'min_response_time': min(durations) if durations else 0,
            'max_response_time': max(durations) if durations else 0,
            'success_rate': len(self.metrics['successful_requests']) / len(durations) if durations else 0
        }
```

## Testing HTTP MCP Servers

### Unit Testing

```python
import pytest
from unittest.mock import patch, MagicMock
import aiohttp

@pytest.mark.asyncio
async def test_http_tool_listing():
    client = MCPHTTPClient("https://test.example.com")
    
    mock_response_data = {
        "tools": [
            {
                "name": "test_tool",
                "description": "A test tool",
                "inputSchema": {"type": "object", "properties": {}}
            }
        ]
    }
    
    with patch('aiohttp.ClientSession.post') as mock_post:
        mock_response = MagicMock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None
        mock_post.return_value.__aenter__.return_value = mock_response
        
        result = await client.list_tools()
        
        assert "tools" in result
        assert len(result["tools"]) == 1
        assert result["tools"][0]["name"] == "test_tool"

@pytest.mark.asyncio
async def test_http_tool_call():
    client = MCPHTTPClient("https://test.example.com")
    
    mock_response_data = {
        "content": [{"type": "text", "text": "Tool result"}]
    }
    
    with patch('aiohttp.ClientSession.post') as mock_post:
        mock_response = MagicMock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None
        mock_post.return_value.__aenter__.return_value = mock_response
        
        result = await client.call_tool("test_tool", {"param": "value"})
        
        assert "content" in result
        assert result["content"][0]["text"] == "Tool result"
```

### Integration Testing

```python
@pytest.mark.asyncio
async def test_http_integration():
    # Start test server
    server = TestHTTPMCPServer()
    server_url = await server.start()
    
    try:
        client = MCPHTTPClient(server_url)
        
        # Test tool listing
        tools_response = await client.list_tools()
        assert "tools" in tools_response
        
        # Test tool call
        call_response = await client.call_tool("test_tool", {"input": "test"})
        assert "content" in call_response
        
    finally:
        await server.stop()
```

## Best Practices

### 1. Connection Management

```python
class ConnectionPoolManager:
    def __init__(self):
        self.pools = {}
    
    def get_pool(self, base_url: str) -> aiohttp.TCPConnector:
        """Get or create connection pool for URL"""
        if base_url not in self.pools:
            self.pools[base_url] = aiohttp.TCPConnector(
                limit=10,
                limit_per_host=3,
                ttl_dns_cache=300
            )
        return self.pools[base_url]
    
    async def close_all(self):
        """Close all connection pools"""
        for pool in self.pools.values():
            await pool.close()
        self.pools.clear()
```

### 2. Request Batching

```python
class BatchingMCPHTTPClient(MCPHTTPClient):
    def __init__(self, *args, batch_size: int = 10, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch_size = batch_size
        self.batch = []
    
    async def call_tool_batch(self, tool_calls):
        """Execute multiple tool calls in batch"""
        if len(tool_calls) <= self.batch_size:
            # Execute directly
            results = []
            for call in tool_calls:
                result = await self.call_tool(call["name"], call.get("arguments"))
                results.append(result)
            return results
        
        # Split into batches
        batches = [tool_calls[i:i + self.batch_size] 
                  for i in range(0, len(tool_calls), self.batch_size)]
        
        all_results = []
        for batch in batches:
            batch_results = await self.call_tool_batch(batch)
            all_results.extend(batch_results)
        
        return all_results
```

### 3. Configuration Validation

```python
def validate_http_config(config):
    required_fields = ['name', 'transport', 'url']
    
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field: {field}")
    
    if config['transport'] != 'http':
        raise ValueError("Transport must be 'http'")
    
    # Validate URL
    from urllib.parse import urlparse
    parsed = urlparse(config['url'])
    if not parsed.scheme or not parsed.netloc:
        raise ValueError("Invalid URL format")
    
    # Validate headers
    if 'headers' in config and not isinstance(config['headers'], dict):
        raise ValueError("Headers must be a dictionary")
    
    # Validate numeric fields
    numeric_fields = ['timeout', 'retries', 'retry_delay']
    for field in numeric_fields:
        if field in config and not isinstance(config[field], (int, float)):
            raise ValueError(f"{field} must be a number")
```

## Troubleshooting

### Common Issues

1. **Connection timeouts**: Increase timeout values or check network connectivity
2. **Authentication failures**: Verify tokens and header formats
3. **SSL errors**: Check certificates and SSL configuration
4. **Rate limiting**: Implement backoff and retry logic

### Debug Mode

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Enable aiohttp debug logging
logging.getLogger('aiohttp').setLevel(logging.DEBUG)

# Custom debug client
class DebugMCPHTTPClient(MCPHTTPClient):
    async def _make_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        print(f"Making {method} request to {self.base_url}")
        print(f"Headers: {self.headers}")
        if params:
            print(f"Params: {params}")
        
        result = await super()._make_request(method, params)
        print(f"Response: {result}")
        
        return result
```

## Next Steps

- Learn about [SSE Transport](https://docs.crewai.com/en/mcp/sse-transport) for real-time event streaming
- Explore [Stdio Transport](https://docs.crewai.com/en/mcp/stdio-transport) for local server connections
- Check out [DSL Integration](https://docs.crewai.com/en/mcp/dsl-integration) for configuration options
- Read about [Multiple Servers](https://docs.crewai.com/en/mcp/multiple-servers) for complex setups
- Review [Security Considerations](https://docs.crewai.com/en/mcp/security) for secure deployments