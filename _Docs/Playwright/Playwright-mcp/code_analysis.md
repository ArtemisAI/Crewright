# Playwright MCP Code Analysis

## Architecture Overview
The `microsoft/playwright-mcp` repository serves primarily as a **thin wrapper and distribution point**.

- **Core Logic**: The actual MCP server implementation resides in the main **Playwright monorepo** (`playwright/lib/mcp`).
- **Entry Point**: `index.js` and `cli.js` in this repo simply require the logic from the `playwright` core library.
- **Extension**: This repository *does* contain the source code for the **Playwright MCP Bridge** Chrome extension.

### Repository Structure
- `cli.js`: Command-line interface entry point.
- `index.js`: Programmatic API entry point.
- `extension/`: Source code for the Chrome Extension.
- `package.json`: Defines dependencies, notably `playwright` (e.g., `1.58.0-alpha...`).

---

## Chrome Extension Analysis (`extension/src`)
The extension facilitates connection between the MCP server (running locally) and an existing Chrome browser tab.

### `background.ts` coverage
The background script manages the lifecycle of connections.
- **`TabShareExtension` Class**: The main controller.
- **Event Listeners**: Listens for tab updates, removals, and runtime messages.
- **`_connectToRelay`**: Establishes a WebSocket connection to the MCP server (Relay).
- **`_connectTab`**: Links a specific browser tab to the active MCP connection.
- **Safety**: Uses a `_pendingTabSelection` map to handle the flow between selecting a tab and connecting it.
- **Feedback**: Updates the extension badge (Green '✓') to indicate a successful connection.

### `relayConnection.ts` coverage
This file implements the bridge between the WebSocket (MCP) and the Chrome Remote Debugging Protocol (CDP).
- **`RelayConnection` Class**: Wraps a WebSocket.
- **`start/attachToTab`**: Uses `chrome.debugger.attach` to control the tab.
- **`forwardCDPCommand`**: The core function. It receives CDP commands from the MCP server (over WebSocket) and executes them on the browser tab using `chrome.debugger.sendCommand`.
- **`forwardCDPEvent`**: Listens for CDP events from the browser and forwards them back to the MCP server.

**Key Insight**: The extension effectively turns the browser tab into a remote puppet controllable via WebSocket, which the Playwright MCP server uses to drive automation.

---

## MCP Server Implementation
While the code isn't in this repo, `cli.js` reveals usage of `playwright/lib/mcp/program`.
- It dynamically "decorates" the CLI program with MCP-specific commands.
- It likely reuses Playwright's existing CDP connection logic but adapts it to the Model Context Protocol (MCP) format (server-sent events, tool definitions).

## Conclusions
1. **Dependency on Core**: This project cannot function without the specific version of Playwright Core capable of MCP.
2. **Bridge Architecture**: For "existing browser" control, it relies heavily on the Chrome Extension acting as a WebSocket-to-CDP relay.
3. **Rapid Iteration**: The alpha version of Playwright (`1.58.0-alpha`) suggests this feature is bleeding-edge.
