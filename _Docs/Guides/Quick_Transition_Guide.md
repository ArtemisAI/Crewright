# ⚡ Quick Transition Guide: Migrating to Crewright

**Moving from Playwright, Selenium, or Browser-Use?**
This guide helps you adapt your Agents to Crewright's "Parasitic" philosophy.

---

## 🛑 The Mindset Shift
| Old Way (Playwright/Selenium) | New Way (Crewright) |
| :--- | :--- |
| **Headless**: Launches a hidden, cold browser. | **Parasitic**: Connects to your *existing* Chrome window. |
| **Login Scripts**: You must script detailed login steps & manage 2FA. | **Skip Login**: You login *once* manually; Agent reuses cookies. |
| **Cookies**: Loaded from JSON files. | **Cookies**: Already there. |
| **Anti-Bot**: Fights Cloudflare/Captchas. | **Anti-Bot**: "I'm already Human." |

---

## 🛠️ Tool Mapping

If your agent used these tools... use these Crewright equivalents:

| Action | Playwright-MCP | Crewright | Note |
| :--- | :--- | :--- | :--- |
| **Go to URL** | `navigate(url)` | `navigate(url)` | Identical. |
| **Click** | `click(selector)` | `click(selector)` | Identical. |
| **Type** | `fill(selector, text)` | `fill(selector, value)` | Arg name is `value`. |
| **Keyboard** | `press(key)` | `press(key)` | Identical. |
| **Wait** | `sleep(ms)` | `evaluate("new Promise...")` | Use JS to wait. |
| **Read** | `get_content()` | `get_page_content()` | Returns text/markdown. |

### 💡 The "Evaluate" Trick
Crewright doesn't have a dedicated `wait` tool. Instead, we give you the raw power of JavaScript execution (via `evaluate`).

**To Wait 5 Seconds:**
```python
# Old
agent.wait(5000)

# Crewright
agent.use_tool("evaluate", expression="new Promise(r => setTimeout(r, 5000))")
```

---

## 📦 Setup in CrewAI

### 1. Install
```bash
npm install -g @crew-ai/crewright
# OR rely on npx
```

### 2. Connect Your Agent
Remove your old tool list (e.g., `SeleniumTools`) and inject the **MCP Server**.

```python
from crewai.mcp import MCPServerStdio

# Define the Bridge
bridge = MCPServerStdio(
    command="npx",
    args=["-y", "@crew-ai/crewright"],
    env=os.environ
)

# Attach to Agent
agent = Agent(
    ...,
    mcps=[bridge] # <--- Magic happens here
)
```

### 3. Simplify Your Tasks
**Delete User/Pass logic.**
*   **Before**: "Navigate to login. Enter username. Enter password. Solve Captcha."
*   **After**: "Navigate to /dashboard." (Assume success).
