# Known Issues

## Resolved
- **Stdio Corruption (Python)**: `print()` statements in `bridge_server.py` broke MCP protocol. **Fix**: Migrated server to Node.js/TypeScript `StdioServerTransport` which handles I/O robustly.
- **Connection Race Condition**: Agent failed if Extension wasn't active. **Fix**: Added "Wait for Connection" logic (15s retry) in both Python and TypeScript servers.
- **Windows Process Instability**: Python `asyncio` loop handling for Stdio was unstable on Windows. **Fix**: Full migration to **Node.js** bridge server.
- **CSP Security Block (`unsafe-eval`)**: The `evaluate` tool failed because MV3 content scripts cannot use `eval()`. **Fix**: Moved execution logic to `background.js` using `chrome.scripting.executeScript`.
- **Stale Extension Code**: Users (and verification agents) hit "Unknown method" errors if the extension is not manually reloaded after updates. **Fix**: Documented reload requirement; automated reload blocked by browser security.

## Active
- **Agent Planning Stall**: During verification, the agent occasionally hangs/stalls before reporting task completion (likely LLM planning latency).
- **NPX Output Noise**: Running via `npx` (Release V1) can pollute stdio with installation messages, breaking MCP connection. **Workaround**: Use `-y` flag or pre-install.
- **Windows File Association (VS Code Popup)**: On some Windows environments, running `npx package` triggers VS Code to open the script file instead of executing it with Node. **Fix**: Do NOT use `npx` in production code. Use `npm install` followed by explicit `node /path/to/script.js`.
