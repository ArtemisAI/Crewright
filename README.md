# Crewight 👻

**The Parasitic Browser Bridge for CrewAI.**
*Control your live, authenticated Chrome session with AI Agents.*

[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](https://github.com/crewai/crewight)
[![MCP](https://img.shields.io/badge/MCP-Compliant-blue)](https://modelcontextprotocol.io)
[![Stack](https://img.shields.io/badge/Stack-TypeScript_%7C_Manifest_V3-blue)](https://nodejs.org)

---

## 🧐 What is this?
**Crewight** (Crew + Light) is an MCP Server that lets AI Agents "hitch a ride" on your existing Chrome browser.

Unlike **Playwright MCP** (which launches a clean, empty browser), **Crewight** connects to your **already open** Chrome window.
*   **Login to nothing**: The agent uses *your* cookies.
*   **Bypass everything**: Cloudflare sees *you*, not a bot.
*   **Visual Feedback**: Watch the agent click and type in real-time.

## 🚀 Key Features
*   **Parasitic Stealth**: zero-config authentication.
*   **Manifest V3**: Secure, modern Chrome Extension architecture.
*   **Native MCP**: Works with CrewAI, Claude Desktop, Cursor, and any MCP client.

## 📦 Installation

### 1. The Extension (Chrome)
1.  Navigate to `chrome://extensions`.
2.  Enable **Developer Mode**.
3.  Click **Load Unpacked**.
4.  Select the `src/bridge/extension` folder from this repo.
5.  *Look for the "Crewight Bridge" icon.*

### 2. The Server (Node.js)
```bash
npx @crewai/crewight
```
*(Or run locally during dev)*:
```bash
cd src/bridge
npm install
npm run build
```

## ⚙️ Configuration (CrewAI)

### Standard Setup
```python
from crewai import Agent
from crewai.mcp import MCPServerStdio

crewight_server = MCPServerStdio(
    command="npx",
    args=["@crewai/crewight"] 
    # OR local: args=["node", "./path/to/dist/index.js"]
)

agent = Agent(
    role="Browser Pilot",
    goal="Navigate LinkedIn",
    mcps=[crewight_server],
    ...
)
```

### Other Clients

<details>
<summary><b>Claude Desktop</b></summary>

Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "crewight": {
      "command": "npx",
      "args": ["@crewai/crewight"]
    }
  }
}
```
</details>

<details>
<summary><b>Cursor</b></summary>

Go to **Cursor Settings** -> **MCP** -> **Add new** -> Command: `npx @crewai/crewight`
</details>

## 🛠️ Tools Available

| Tool | Description |
| :--- | :--- |
| `navigate(url)` | Moves the active tab to a new URL. |
| `get_page_content()` | Returns the text content of the page (Markdown friendly). |
| `click_element(selector)` | Clicks a DOM element via CSS selector. |
| `type_text(selector, text)` | Types into an input field. |
| `ask_human(question)` | Pauses execution and asks YOU for help (e.g., OTP codes). |

## 📚 Documentation
*   [**Architecture**](./ARCHITECTURE.md) - Why "Parasitic" vs Headless?
*   [**Roadmap**](./ROADMAP.md) - What's coming next?
*   [**Contributing**](./CONTRIBUTING.md) - Build the future of agentic browsing.

---
*Built with ❤️ by the CrewAI Team.*
