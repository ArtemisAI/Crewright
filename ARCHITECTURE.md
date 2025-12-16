# Architecture: Crewright vs. Playwright MCP

> **Why did we build this?**
> Why not just use `npx @playwright/mcp`?

## The Problem: The "Clean Slate" Trap
Standard headless automation (Playwright, Selenium, Puppeteer) launches a **clean, isolated browser instance**.

### 1. The Auth Wall
Modern web apps (Google, LinkedIn, Enterprise Portals) verify identity using:
*   **2FA / MFA**: SMS codes, Authenticator apps.
*   **Device Fingerprinting**: "Unrecognized device" alerts.
*   **Behavioral Analysis**: Mouse jitter, typing speed.

**Robots cannot solve these easily.** Even if an Agent has your password, it will likely be blocked by a "Verify it's you" challenge.

### 2. The Anti-Bot Moat
Companies like Cloudflare, Akamai, and Datadome specifically hunt for headless browsers.
*   **TLS Fingerprinting**: Headless Node.js/Python HTTP stacks look different.
*   **JS Runtime Flags**: `navigator.webdriver = true`.

## The Solution: Crewright (Parasitic Architecture)
**Crewright does not launch a browser.** It infects yours.

### "Parasitic" Control
By installing the **Crewright Extension** in your *daily driver* Chrome profile, the agent inherits:
1.  **Your Cookies**: Already logged into Gmail, GitHub, Corporate SSO.
2.  **Your Fingerprint**: The browser fingerprint matches a real human (you).
3.  **Your Trust Score**: Requests come from a known, trusted IP and device.

### Comparison Matrix

| Feature | Playwright MCP | **Crewright** |
| :--- | :--- | :--- |
| **Session** | New / Clean | **Existing / Authenticated** |
| **Detection Risk** | High (Headless) | **Near Zero (Extension)** |
| **Auth Handling** | Agent must login | **User is already logged in** |
| **Control Comp.** | Playwright API | **MCP Tools (Navigate, Click)** |
| **Execution** | Node.js Process | **Chrome Extension Context** |

## System Components

### 1. The Host (Chrome Extension)
*   **Manifest V3**: Compliant, secure.
*   **Permissions**: `activeTab`, `scripting`.
*   **Role**: Executes commands in the DOM of the *currently active tab* or a specific background tab.

### 2. The Bridge (MCP Server)
*   **Node.js**: Translates MCP commands (`navigate`, `get_page_content`) into WebSocket messages.
*   **Stdio**: Communicates securely with the local Agent process.

### 3. The Brain (CrewAI Agent)
*   **Decision Making**: Decides *what* to click or read based on the task using a specialized LLM.

## When to use what?

*   **Use Playwright MCP** when:
    *   You are scraping public data (Wikipedia).
    *   You need to run 10,000 instances in parallel (Cloud).
    *   Auth is simple or non-existent.

*   **Use Crewright** when:
    *   You need to perform actions inside a logged-in account (LinkedIn, Gmail).
    *   You are blocked by Cloudflare/Akamai.
    *   You want the agent to "assist" you in your current session.
