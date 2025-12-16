# Known Issues

## Resolved
- **Stdio Corruption (Python)**: `print()` statements in `bridge_server.py` broke MCP protocol. **Fix**: Migrated server to Node.js/TypeScript `StdioServerTransport` which handles I/O robustly.
- **Connection Race Condition**: Agent failed if Extension wasn't active. **Fix**: Added "Wait for Connection" logic (15s retry) in both Python and TypeScript servers.
- **Windows Process Instability**: Python `asyncio` loop handling for Stdio was unstable on Windows. **Fix**: Full migration to **Node.js** bridge server.

## Active
- **None**: Bridge is verified stable.
