# Crewright 👻

**The Parasitic Browser Bridge for [CrewAI](https://crewai.com).**
*Control your live, authenticated Chrome session with AI Agents.*

[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](https://github.com/crewai/crewright)
[![MCP](https://img.shields.io/badge/MCP-Compliant-blue)](https://modelcontextprotocol.io)
[![Stack](https://img.shields.io/badge/Stack-TypeScript_%7C_Manifest_V3-blue)](https://nodejs.org)
[![CrewAI](https://img.shields.io/badge/Powered%20By-CrewAI-orange)](https://docs.crewai.com)

---

## 🧐 What is this?
**Crewright** is the missing link between **[CrewAI](https://crewai.com)** and your browser.
*> "Like Playwright, but for CrewAI!"*

Unlike **Playwright MCP** (which launches a clean, empty browser), **Crewright** connects to your **already open** Chrome window.
*   **Login to nothing**: The agent uses *your* cookies.
*   **Bypass everything**: Cloudflare sees *you*, not a bot.
*   **Visual Feedback**: Watch the agent click and type in real-time.

It is designed to work seamlessly with the [CrewAI Framework](https://docs.crewai.com) to give your agents "eyes" and "hands" on the web.

## 🚀 Key Features
*   **Parasitic Stealth**: zero-config authentication.
*   **Manifest V3**: Secure, modern Chrome Extension architecture.
*   **Native MCP**: Works with CrewAI, Claude Desktop, Cursor, and any MCP client.

## 📦 Installation

### 1. The Extension (Chrome)
To give CrewAI access to your browser, you need to load the bridge extension.

1.  Open Chrome and navigate to `chrome://extensions`.
2.  Enable **Developer Mode** (toggle in the top right corner).
3.  Click **Load Unpacked**.
4.  Select the `src/bridge/extension` folder from this directory.
5.  *Verify*: You should see the **Crewright Bridge** card with a 👻 icon.
6.  *Check*: Ensure the toggle is **ON**.

> **Note**: This extension runs entirely locally. It communicates *only* with your local Agent. No data is sent to the cloud.

### 2. The Server (Node.js)
```bash
npx @crew-ai/crewright
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

crewright_server = MCPServerStdio(
    command="npx",
    args=["@crew-ai/crewright"] 
    # OR local: args=["node", "./path/to/dist/index.js"]
)

agent = Agent(
    role="Browser Pilot",
    goal="Navigate LinkedIn",
    mcps=[crewright_server],
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
    "crewright": {
      "command": "npx",
      "args": ["@crewai/crewright"]
    }
  }
}
```
</details>

<details>
<summary><b>Cursor</b></summary>

Go to **Cursor Settings** -> **MCP** -> **Add new** -> Command: `npx @crewai/crewright`
</details>

## 🛠️ Tools Available

> [!NOTE]
> **v1.1.0 (Dev Branch) Update**: Tool names have been renamed to match **Playwright** conventions.

| Tool | Description | Playwright Equivalent |
| :--- | :--- | :--- |
| `navigate(url)` | Moves the active tab to a new URL. | `page.goto(url)` |
| `get_page_content()` | Returns the text content of the page. | `page.content()` |
| `click(selector)` | Clicks a DOM element. | `page.click(selector)` |
| `fill(selector, value)` | Fills an input field. | `page.fill(selector, value)` |
| `press(key)` | Simulates specific key press (e.g. 'Enter'). | `page.press(selector, key)` |
| `evaluate(expression)` | Executes JavaScript in the page context. | `page.evaluate(expression)` |
| `screenshot()` | Captures a screenshot (Base64). | `page.screenshot()` |
| `hover(selector)` | Hovers over an element. | `page.hover(selector)` |
| `scroll(direction)` | Scrolls the viewport ('up', 'down', 'top', 'bottom'). | *Custom Helper* |
| `ask_human(question)` | Pauses execution and asks YOU for help. | *CrewAI Exclusive* |

## 📚 Documentation
*   [**Architecture**](./ARCHITECTURE.md) - Why "Parasitic" vs Headless?
*   [**Roadmap**](./ROADMAP.md) - What's coming next?
*   [**Contributing**](./CONTRIBUTING.md) - Build the future of agentic browsing.

## ❤️ Support & Sponsorship
This project is open-source and maintained by **Daniel Gonzalez** (ArtemisAI).
If you find this tool useful for your agents, please consider supporting the development!

*   **Sponsor**: [GitHub Sponsors](https://github.com/sponsors/ArtemisAI)
*   **Hire Me**: [AI Solopreneur & Developer](https://dan-ai.pro/)
*   **ArtemisAI**: [Enterprise AI Solutions](https://artemis-ai.ca)

---
*Built with ❤️ by the **ArtemisAI (Daniel Gonzalez)** to help out all the bots 🤖 needing good tools.*
