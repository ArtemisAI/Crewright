# @artemisai/crewright

The Parasitic Browser Bridge for CrewAI. Control authenticated Chrome sessions via MCP.

[![npm version](https://img.shields.io/npm/v/@artemisai/crewright.svg)](https://www.npmjs.com/package/@artemisai/crewright)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

Crewright enables CrewAI agents to control your already-open Chrome browser, inheriting your authentication state and avoiding anti-bot detection. Unlike headless browsers, it uses your existing session for seamless web automation.

## Installation

```bash
npm install -g @artemisai/crewright
# or
npx @artemisai/crewright
```

## Usage

Crewright is an MCP (Model Context Protocol) server that communicates with a Chrome extension.

### 1. Install the Chrome Extension

1. Download and load the extension from the [main repository](https://github.com/ArtemisAI/CrewAi-tools/tree/main/src/bridge/extension)
2. Enable Developer Mode in Chrome
3. Load the unpacked extension

### 2. Use with CrewAI

```python
from crewai import Agent
from crewai.mcp import MCPServerStdio

crewright_server = MCPServerStdio(
    command="npx",
    args=["@artemisai/crewright"]
)

agent = Agent(
    role="Web Navigator",
    goal="Browse and extract information",
    mcps=[crewright_server],
    ...
)
```

### 3. Available Tools

- `navigate(url)` - Navigate to a URL
- `get_page_content()` - Get page text content
- `click_element(selector)` - Click a CSS selector
- `type_text(selector, text)` - Type into an input field
- `ask_human(question)` - Request human assistance

## Requirements

- Node.js 16+
- Chrome browser with the Crewright extension installed

## License

MIT

## Author

Daniel Gonzalez (ArtemisAI) - https://dan-ai.pro/