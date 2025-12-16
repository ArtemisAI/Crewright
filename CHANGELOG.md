# Changelog

All notable changes to the **CrewAI Stealth-Stream Bridge** project will be documented in this file.

## [Unreleased] - 2025-12-16

### Added
- **Stealth-Stream Bridge Architecture**: Implemented a "parasitic" browser control system using a Chrome Extension and MCP Server.
- **Chrome Extension (v1.0)**:
    - Manifest V3 compliant.
    - `background.js`: Handles WebSocket connections and retry logic (15s timeout).
    - `content.js`: Executes `navigate`, `get_page_content`, `click_element`, `type_text` in the active tab context.
- **TypeScript Bridge Server**:
    - Replaced the initial Python implementation with a robust **Node.js/TypeScript** server (`src/bridge`).
    - Uses `StdioServerTransport` for stable communication with CrewAI.
    - Uses `ws` library for native WebSocket handling.
    - Exposes MCP tools: `navigate`, `get_page_content`, `click_element`, `type_text`, `ask_human`.
- **Test Agent**:
    - `src/agents/test_agent.py`: Verified end-to-end functionality (Agent -> Node Bridge -> Extension -> Browser).

### Changed
- **Architecture Pivot**: Migrated Bridge Server from **Python (FastMCP)** to **Node.js (McpServer)**.
    - *Reason*: Python's `asyncio` loop handling for Stdio was unstable on Windows, causing frequent timeouts and pipe errors. Node.js offers superior stability for Stdio/WebSocket workloads.
- **Protocol**: Switched internal Bridge-to-Extension communication to use standard JSON-RPC over WebSockets (`ws://localhost:8765`).

### Fixed
- **Connection Race Conditions**: Added "wait for connection" logic to preventing the Agent from failing if the browser wasn't immediately ready.
- **Navigation Reliability**: Updated `background.js` to await `chrome.tabs.onUpdated` 'complete' status before returning success.
