
import asyncio
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.bridge.bridge_server import start_websocket_server

# A simple wrapper to run the WS server and print to STDOUT (since we aren't using MCP Stdio here)
# We need to monkeypath the log function in bridge_server to print to stdout so we can see it
import src.bridge.bridge_server as bridge

def log_stdout(msg):
    print(msg)

bridge.log = log_stdout

if __name__ == "__main__":
    print("=== Stealth Bridge Diagnostic Tool ===")
    print("Starting WebSocket Server on ws://localhost:8765")
    print("Please open Chrome and ensure the extension icon has a GREEN badge.")
    print("Waiting for connection...")
    
    try:
        asyncio.run(start_websocket_server())
    except KeyboardInterrupt:
        print("Stopping server.")
