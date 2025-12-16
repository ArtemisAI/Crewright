
import asyncio
import json
import threading
import sys
import uvicorn
from contextlib import asynccontextmanager
from typing import Optional
from mcp.server.fastmcp import FastMCP
from websockets.server import serve

# Global State
active_socket = None
response_futures = {}  # id -> asyncio.Future

def log(msg):
    sys.stderr.write(f"{msg}\n")
    sys.stderr.flush()

# WebSocket Handler
async def ws_handler(websocket):
    global active_socket
    active_socket = websocket
    log("[Bridge] Extension Connected!")
    try:
        async for message in websocket:
            data = json.loads(message)
            if "id" in data and data["id"] in response_futures:
                response_futures[data["id"]].set_result(data.get("result"))
                del response_futures[data["id"]]
    except Exception as e:
        log(f"[Bridge] Connection lost: {e}")
        active_socket = None

async def start_websocket_server():
    log("[Bridge] Starting WebSocket Server on 0.0.0.0:8765...")
    async with serve(ws_handler, "0.0.0.0", 8765):
        await asyncio.get_running_loop().create_future()  # Infinite loop

# Lifespan manager to run WebSocket server alongside FastMCP
@asynccontextmanager
async def bridge_lifespan(server):
    # Start WebSocket server in background task
    log("[Bridge] Initializing...")
    ws_task = asyncio.create_task(start_websocket_server())
    yield
    # Cleanup
    ws_task.cancel()
    try:
        await ws_task
    except asyncio.CancelledError:
        pass
    log("[Bridge] Shutdown complete.")

# Initialize FastMCP Server with SSE settings
mcp = FastMCP("StealthBridge", lifespan=bridge_lifespan)

# Helper to send command to extension
async def send_to_extension(method: str, params: dict):
    # Wait for connection if not active (up to 15s)
    if not active_socket:
        log("[Bridge] Waiting for extension to connect...")
        for _ in range(15):
            if active_socket:
                log("[Bridge] Extension connected!")
                break
            await asyncio.sleep(1)
            
    if not active_socket:
        return "Error: No browser connected. Please install the extension and ensure it is active. (Timed out waiting for connection)"
    
    import uuid
    req_id = str(uuid.uuid4())
    future = asyncio.get_running_loop().create_future()
    response_futures[req_id] = future
    
    cmd = {
        "id": req_id,
        "method": method,
        "params": params
    }
    
    await active_socket.send(json.dumps(cmd))
    
    # Wait for response (timeout 30s)
    try:
        return await asyncio.wait_for(future, timeout=30.0)
    except asyncio.TimeoutError:
        del response_futures[req_id]
        return "Error: Timeout waiting for browser response."

# MCP Tools

@mcp.tool()
async def navigate(url: str) -> str:
    """Navigates the active tab to the specified URL."""
    return await send_to_extension("navigate", {"url": url})

@mcp.tool()
async def get_page_content() -> str:
    """Returns the text content of the current page."""
    return await send_to_extension("get_page_content", {})

@mcp.tool()
async def click_element(selector: str) -> str:
    """Clicks an element defined by the CSS selector."""
    return await send_to_extension("click_element", {"selector": selector})

@mcp.tool()
async def type_text(selector: str, text: str) -> str:
    """Types text into an input defined by the CSS selector."""
    return await send_to_extension("type_text", {"selector": selector, "text": text})

@mcp.tool()
async def ask_human(question: str) -> str:
    """Pauses execution and asks the human operator for help via the console."""
    log(f"\n[AGENT NEEDS HELP] {question}")
    log("Press Enter in this terminal to resume after you have assisted...")
    return "Please alert the user manually. (Stdio input not supported in this mode)"

if __name__ == "__main__":
    log("[Bridge] Starting SSE Server on localhost:8000...")
    # Run FastMCP with SSE transport
    mcp.run(transport="sse", port=8000)
