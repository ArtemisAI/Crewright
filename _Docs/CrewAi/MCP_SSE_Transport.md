# SSE Transport

Server-Sent Events (SSE) transport enables real-time, bidirectional communication between CrewAI agents and MCP (Model Context Protocol) servers. Unlike stdio transport which is process-based, SSE transport uses HTTP connections for network-based communication.

## Overview

SSE transport provides:

- **Real-time communication**: Event-driven updates from servers
- **Network flexibility**: Connect to remote MCP servers
- **Scalability**: Support for multiple concurrent connections
- **Web compatibility**: Works with web-based MCP server deployments

## Basic Configuration

### Simple SSE Server

```yaml
mcps:
  - name: "realtime_data"
    transport: "sse"
    url: "https://api.example.com/mcp/sse"
    headers:
      Authorization: "Bearer ${API_TOKEN}"
```

### Configuration Parameters

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `name` | string | Unique server identifier | Yes |
| `transport` | string | Must be "sse" | Yes |
| `url` | string | SSE endpoint URL | Yes |
| `headers` | object | HTTP headers for requests | No |
| `timeout` | number | Connection timeout in seconds | No |
| `reconnect_interval` | number | Reconnection interval in seconds | No |
| `max_reconnects` | number | Maximum reconnection attempts | No |

## SSE Server Implementation

### Basic SSE MCP Server

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import json
from mcp import Tool, types
from mcp.server import Server
from mcp.types import TextContent

app = FastAPI()
server = Server("sse-mcp-server")

# Store active connections
active_connections = set()

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        Tool(
            name="realtime_monitor",
            description="Monitor real-time data streams",
            inputSchema={
                "type": "object",
                "properties": {
                    "stream_id": {"type": "string"}
                },
                "required": ["stream_id"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "realtime_monitor":
        stream_id = arguments["stream_id"]
        # Start monitoring stream
        return [TextContent(type="text", text=f"Started monitoring stream: {stream_id}")]
    else:
        raise ValueError(f"Unknown tool: {name}")

async def generate_events():
    """Generate server-sent events"""
    while True:
        # Simulate real-time data
        data = {
            "timestamp": asyncio.get_event_loop().time(),
            "event": "data_update",
            "payload": {"value": 42}
        }
        
        yield f"data: {json.dumps(data)}\n\n"
        await asyncio.sleep(1)  # Send event every second

@app.get("/mcp/sse")
async def sse_endpoint():
    return StreamingResponse(
        generate_events(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
        }
    )

@app.post("/mcp/rpc")
async def rpc_endpoint(request: dict):
    """Handle RPC calls over HTTP"""
    method = request.get("method")
    params = request.get("params", {})
    
    if method == "tools/list":
        tools = await list_tools()
        return {"tools": [tool.dict() for tool in tools]}
    elif method == "tools/call":
        result = await call_tool(params["name"], params.get("arguments", {}))
        return {"content": [content.dict() for content in result]}
    
    return {"error": "Method not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Node.js SSE Server

```javascript
const express = require('express');
const { Server } = require('@modelcontextprotocol/sdk/server/index.js');
const { SSEServerTransport } = require('@modelcontextprotocol/sdk/server/sse.js');

const app = express();
const server = new Server(
  {
    name: 'sse-node-server',
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
        name: 'weather_monitor',
        description: 'Monitor weather updates',
        inputSchema: {
          type: 'object',
          properties: {
            location: { type: 'string' }
          },
          required: ['location']
        }
      }
    ]
  };
});

server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;

  if (name === 'weather_monitor') {
    const { location } = args;
    
    // Simulate weather monitoring
    return {
      content: [{
        type: 'text',
        text: `Started monitoring weather for ${location}`
      }]
    };
  }

  throw new Error(`Unknown tool: ${name}`);
});

// SSE endpoint
app.get('/mcp/sse', (req, res) => {
  const transport = new SSEServerTransport(res, req);
  server.connect(transport);
});

// RPC endpoint for tool calls
app.post('/mcp/rpc', express.json(), async (req, res) => {
  try {
    const response = await server.processRequest(req.body);
    res.json(response);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(3000, () => {
  console.log('SSE MCP server listening on port 3000');
});
```

## Advanced SSE Configuration

### Authentication

```yaml
mcps:
  - name: "secure_sse"
    transport: "sse"
    url: "https://secure-api.example.com/mcp/sse"
    headers:
      Authorization: "Bearer ${JWT_TOKEN}"
      X-API-Key: "${API_KEY}"
      User-Agent: "CrewAI-Agent/1.0"
```

### Connection Management

```yaml
mcps:
  - name: "reliable_sse"
    transport: "sse"
    url: "https://api.example.com/mcp/sse"
    timeout: 30
    reconnect_interval: 5
    max_reconnects: 10
    headers:
      Authorization: "Bearer ${TOKEN}"
```

### Multiple SSE Servers

```yaml
mcps:
  - name: "market_data"
    transport: "sse"
    url: "https://finance-api.example.com/mcp/sse"
    headers:
      Authorization: "Bearer ${FINANCE_TOKEN}"
  
  - name: "social_media"
    transport: "sse"
    url: "https://social-api.example.com/mcp/sse"
    headers:
      Authorization: "Bearer ${SOCIAL_TOKEN}"
  
  - name: "iot_sensors"
    transport: "sse"
    url: "https://iot.example.com/mcp/sse"
    headers:
      Authorization: "Bearer ${IOT_TOKEN}"
```

## Real-time Event Handling

### Event Processing

```python
import asyncio
import aiohttp
import json

class SSEClient:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers or {}
        
    async def connect(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.url) as response:
                async for line in response.content:
                    line = line.decode('utf-8').strip()
                    
                    if line.startswith('data: '):
                        data = line[6:]  # Remove 'data: ' prefix
                        try:
                            event_data = json.loads(data)
                            await self.process_event(event_data)
                        except json.JSONDecodeError:
                            print(f"Invalid JSON: {data}")
    
    async def process_event(self, event_data):
        """Process incoming SSE events"""
        event_type = event_data.get('event')
        
        if event_type == 'data_update':
            await self.handle_data_update(event_data.get('payload', {}))
        elif event_type == 'tool_result':
            await self.handle_tool_result(event_data.get('result', {}))
        elif event_type == 'error':
            await self.handle_error(event_data.get('error', {}))
    
    async def handle_data_update(self, payload):
        print(f"Received data update: {payload}")
        # Process data update
    
    async def handle_tool_result(self, result):
        print(f"Received tool result: {result}")
        # Process tool result
    
    async def handle_error(self, error):
        print(f"Received error: {error}")
        # Handle error

# Usage
client = SSEClient("https://api.example.com/mcp/sse", headers={"Authorization": "Bearer token"})
await client.connect()
```

### Event Filtering

```python
class FilteredSSEClient(SSEClient):
    def __init__(self, url, headers=None, event_filters=None):
        super().__init__(url, headers)
        self.event_filters = event_filters or []
    
    async def process_event(self, event_data):
        # Apply filters
        for filter_func in self.event_filters:
            if not filter_func(event_data):
                return  # Skip event
        
        await super().process_event(event_data)

# Usage with filters
def important_events_only(event_data):
    return event_data.get('priority', 0) > 5

client = FilteredSSEClient(
    "https://api.example.com/mcp/sse",
    headers={"Authorization": "Bearer token"},
    event_filters=[important_events_only]
)
```

## Error Handling and Reconnection

### Automatic Reconnection

```python
import asyncio
import aiohttp
import logging

logger = logging.getLogger(__name__)

class ResilientSSEClient:
    def __init__(self, url, headers=None, max_reconnects=5, reconnect_interval=5):
        self.url = url
        self.headers = headers or {}
        self.max_reconnects = max_reconnects
        self.reconnect_interval = reconnect_interval
        self.reconnect_count = 0
        
    async def connect_with_retry(self):
        while self.reconnect_count < self.max_reconnects:
            try:
                await self.connect()
                self.reconnect_count = 0  # Reset on successful connection
            except Exception as e:
                logger.error(f"SSE connection failed: {e}")
                self.reconnect_count += 1
                
                if self.reconnect_count < self.max_reconnects:
                    logger.info(f"Reconnecting in {self.reconnect_interval}s... ({self.reconnect_count}/{self.max_reconnects})")
                    await asyncio.sleep(self.reconnect_interval)
                else:
                    logger.error("Max reconnection attempts reached")
                    raise
    
    async def connect(self):
        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(self.url) as response:
                    response.raise_for_status()
                    
                    async for line in response.content:
                        line = line.decode('utf-8').strip()
                        
                        if line.startswith('data: '):
                            data = line[6:]
                            try:
                                event_data = json.loads(data)
                                await self.process_event(event_data)
                            except json.JSONDecodeError as e:
                                logger.warning(f"Invalid JSON received: {data} ({e})")
                                
        except aiohttp.ClientError as e:
            logger.error(f"HTTP error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
```

### Error Event Handling

```python
async def process_event(self, event_data):
    try:
        event_type = event_data.get('event')
        
        if event_type == 'error':
            await self.handle_error_event(event_data)
        elif event_type == 'data_update':
            await self.handle_data_update(event_data.get('payload', {}))
        else:
            logger.warning(f"Unknown event type: {event_type}")
            
    except Exception as e:
        logger.error(f"Error processing event {event_data}: {e}")
        # Send error acknowledgment if needed
        await self.send_error_acknowledgment(event_data.get('id'))

async def handle_error_event(self, event_data):
    error_info = event_data.get('error', {})
    error_code = error_info.get('code')
    error_message = error_info.get('message')
    
    logger.error(f"SSE error received: {error_code} - {error_message}")
    
    if error_code == 'AUTHENTICATION_FAILED':
        # Handle auth failure - maybe refresh token
        await self.refresh_authentication()
    elif error_code == 'RATE_LIMITED':
        # Handle rate limiting - back off
        await asyncio.sleep(60)
    else:
        # Generic error handling
        self.reconnect_count += 1
```

## Security Considerations

### Authentication

```yaml
mcps:
  - name: "authenticated_sse"
    transport: "sse"
    url: "https://secure-api.example.com/mcp/sse"
    headers:
      Authorization: "Bearer ${JWT_TOKEN}"
      X-API-Key: "${API_KEY}"
      X-Client-ID: "${CLIENT_ID}"
```

### SSL/TLS Configuration

```python
import ssl

# Custom SSL context for self-signed certificates
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

connector = aiohttp.TCPConnector(ssl=ssl_context)

async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
    # SSE connection with custom SSL
    pass
```

### Message Encryption

```python
from cryptography.fernet import Fernet
import base64

class EncryptedSSEClient(SSEClient):
    def __init__(self, url, headers=None, encryption_key=None):
        super().__init__(url, headers)
        self.cipher = Fernet(encryption_key) if encryption_key else None
    
    async def process_event(self, event_data):
        if self.cipher and 'encrypted_payload' in event_data:
            # Decrypt payload
            encrypted_data = base64.b64decode(event_data['encrypted_payload'])
            decrypted_data = self.cipher.decrypt(encrypted_data)
            event_data['payload'] = json.loads(decrypted_data.decode())
        
        await super().process_event(event_data)
```

## Performance Optimization

### Connection Pooling

```python
import aiohttp

# Configure connection pooling
connector = aiohttp.TCPConnector(
    limit=10,  # Max connections
    limit_per_host=2,  # Max connections per host
    ttl_dns_cache=30,  # DNS cache TTL
    use_dns_cache=True
)

async with aiohttp.ClientSession(connector=connector) as session:
    # Use pooled connections for SSE
    pass
```

### Event Batching

```python
class BatchingSSEClient(SSEClient):
    def __init__(self, *args, batch_size=10, batch_timeout=1.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch_size = batch_size
        self.batch_timeout = batch_timeout
        self.batch = []
        self.last_batch_time = asyncio.get_event_loop().time()
    
    async def process_event(self, event_data):
        self.batch.append(event_data)
        current_time = asyncio.get_event_loop().time()
        
        # Check if batch is ready
        if (len(self.batch) >= self.batch_size or 
            current_time - self.last_batch_time >= self.batch_timeout):
            await self.process_batch(self.batch)
            self.batch = []
            self.last_batch_time = current_time
    
    async def process_batch(self, batch):
        """Process a batch of events"""
        print(f"Processing batch of {len(batch)} events")
        # Process batch efficiently
```

### Compression

```yaml
mcps:
  - name: "compressed_sse"
    transport: "sse"
    url: "https://api.example.com/mcp/sse"
    headers:
      Accept-Encoding: "gzip, deflate"
      Authorization: "Bearer ${TOKEN}"
```

## Monitoring and Logging

### Connection Monitoring

```python
class MonitoredSSEClient(SSEClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection_start_time = None
        self.events_received = 0
        self.errors_count = 0
    
    async def connect(self):
        self.connection_start_time = asyncio.get_event_loop().time()
        try:
            await super().connect()
        finally:
            connection_duration = asyncio.get_event_loop().time() - self.connection_start_time
            logger.info(f"SSE connection duration: {connection_duration:.2f}s")
            logger.info(f"Events received: {self.events_received}")
            logger.info(f"Errors encountered: {self.errors_count}")
    
    async def process_event(self, event_data):
        self.events_received += 1
        try:
            await super().process_event(event_data)
        except Exception as e:
            self.errors_count += 1
            logger.error(f"Event processing error: {e}")
            raise
```

### Performance Metrics

```python
import time

class MetricsSSEClient(MonitoredSSEClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_processing_times = []
    
    async def process_event(self, event_data):
        start_time = time.perf_counter()
        try:
            await super().process_event(event_data)
        finally:
            processing_time = time.perf_counter() - start_time
            self.event_processing_times.append(processing_time)
            
            # Log slow events
            if processing_time > 1.0:  # More than 1 second
                logger.warning(f"Slow event processing: {processing_time:.2f}s for event {event_data.get('id')}")
    
    def get_metrics(self):
        if not self.event_processing_times:
            return {}
        
        return {
            'avg_processing_time': sum(self.event_processing_times) / len(self.event_processing_times),
            'max_processing_time': max(self.event_processing_times),
            'min_processing_time': min(self.event_processing_times),
            'total_events': len(self.event_processing_times)
        }
```

## Testing SSE MCP Servers

### Unit Testing

```python
import pytest
from unittest.mock import patch, MagicMock
import aiohttp

@pytest.mark.asyncio
async def test_sse_connection():
    client = SSEClient("https://test.example.com/sse")
    
    mock_response = MagicMock()
    mock_response.content = iter([
        b'data: {"event": "test", "data": "hello"}\n\n',
        b'data: {"event": "test", "data": "world"}\n\n'
    ])
    
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_get.return_value.__aenter__.return_value = mock_response
        
        events_processed = []
        
        async def mock_process_event(event_data):
            events_processed.append(event_data)
        
        client.process_event = mock_process_event
        
        await client.connect()
        
        assert len(events_processed) == 2
        assert events_processed[0]['data'] == 'hello'
        assert events_processed[1]['data'] == 'world'

@pytest.mark.asyncio
async def test_sse_reconnection():
    client = ResilientSSEClient("https://test.example.com/sse", max_reconnects=2)
    
    with patch.object(client, 'connect', side_effect=[Exception("Connection failed"), None]):
        await client.connect_with_retry()
        
        assert client.connect.call_count == 2
```

### Integration Testing

```python
@pytest.mark.asyncio
async def test_full_sse_workflow():
    # Start test SSE server
    server = TestSSEServer()
    server_url = await server.start()
    
    try:
        # Connect client
        client = SSEClient(server_url)
        received_events = []
        
        async def collect_events(event_data):
            received_events.append(event_data)
        
        client.process_event = collect_events
        
        # Start client in background
        client_task = asyncio.create_task(client.connect())
        
        # Wait for some events
        await asyncio.sleep(2)
        
        # Stop client
        client_task.cancel()
        
        # Verify events received
        assert len(received_events) > 0
        
    finally:
        await server.stop()
```

## Best Practices

### 1. Connection Management

```python
class ConnectionManager:
    def __init__(self):
        self.connections = {}
    
    async def get_connection(self, name, config):
        if name not in self.connections:
            client = ResilientSSEClient(
                config['url'],
                headers=config.get('headers'),
                max_reconnects=config.get('max_reconnects', 5)
            )
            self.connections[name] = client
        
        return self.connections[name]
    
    async def close_all(self):
        for name, client in self.connections.items():
            # Close connection if supported
            pass
        self.connections.clear()
```

### 2. Event Processing

```python
class EventProcessor:
    def __init__(self):
        self.event_handlers = {}
    
    def register_handler(self, event_type, handler):
        self.event_handlers[event_type] = handler
    
    async def process_event(self, event_data):
        event_type = event_data.get('event')
        handler = self.event_handlers.get(event_type)
        
        if handler:
            try:
                await handler(event_data)
            except Exception as e:
                logger.error(f"Event handler error for {event_type}: {e}")
        else:
            logger.warning(f"No handler for event type: {event_type}")
```

### 3. Configuration Validation

```python
def validate_sse_config(config):
    required_fields = ['name', 'transport', 'url']
    
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field: {field}")
    
    if config['transport'] != 'sse':
        raise ValueError("Transport must be 'sse'")
    
    # Validate URL
    from urllib.parse import urlparse
    parsed = urlparse(config['url'])
    if not parsed.scheme or not parsed.netloc:
        raise ValueError("Invalid URL format")
    
    # Validate headers
    if 'headers' in config and not isinstance(config['headers'], dict):
        raise ValueError("Headers must be a dictionary")
```

## Troubleshooting

### Common Issues

1. **Connection failures**: Check URL, network connectivity, and SSL certificates
2. **Authentication errors**: Verify tokens, API keys, and header formats
3. **Event parsing errors**: Check JSON format and encoding
4. **Reconnection issues**: Adjust reconnect intervals and max attempts

### Debug Mode

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Enable aiohttp debug logging
logging.getLogger('aiohttp').setLevel(logging.DEBUG)

# Custom debug client
class DebugSSEClient(SSEClient):
    async def connect(self):
        print(f"Connecting to {self.url}")
        print(f"Headers: {self.headers}")
        await super().connect()
    
    async def process_event(self, event_data):
        print(f"Received event: {event_data}")
        await super().process_event(event_data)
```

## Next Steps

- Learn about [HTTP Transport](https://docs.crewai.com/en/mcp/streamable-http-transport) for request-response communication
- Explore [Stdio Transport](https://docs.crewai.com/en/mcp/stdio-transport) for local server connections
- Check out [DSL Integration](https://docs.crewai.com/en/mcp/dsl-integration) for configuration options
- Read about [Multiple Servers](https://docs.crewai.com/en/mcp/multiple-servers) for complex setups
- Review [Security Considerations](https://docs.crewai.com/en/mcp/security) for secure deployments