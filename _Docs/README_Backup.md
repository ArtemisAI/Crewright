# Crewai Chrome Extension (Crewight)

**Developed by [ArtemisAI](https://artemis-ai.ca)**

This project provides a custom Chrome extension (Crewight) for [CrewAI](https://crewai.com) tools, integrating with [Browser Use](https://github.com/browser-use/browser-use) to enable AI agents to perform complex, headed (visible) web research tasks via browser automation. Unlike generic Playwright extensions, this is a tailored extension designed specifically for seamless CrewAI connectivity and control.

## 🚀 Features

- **Custom Chrome Extension**: A bespoke extension (Crewight) built for direct CrewAI integration, enabling real-time browser control without relying on generic Playwright extensions.
- **Chrome CDP Integration**: Leverages Playwright's CDP support for direct Chrome browser control and automation.
- **Headed Browser Automation**: Watch the agent browse the web in real-time through a visible Chrome instance.
- **Service-Based Architecture**: Separation of concerns between the CrewAI agent (client) and the Browser execution (server).
- **Configurable**: Fully controlled via `.env` file (LLM providers, window size, headless mode).
- **Windows Compatible**: Includes patches for Windows signal handling issues.
- **Observability**: Integrated with CrewAI traces (telemetry).

## 🛠️ Setup

### Prerequisites

- Python 3.10+
- [Playwright](https://playwright.dev/) (for CDP-based Chrome automation)
- Chrome browser installed

### Installation

1. **Clone the repository**
2. **Create a virtual environment**:

    ```powershell
    python -m venv .venv
    ```

3. **Install dependencies**:

    ```powershell
    .venv\Scripts\pip install -r requirements.txt
    ```

4. **Install Playwright browsers** (ensures Chrome CDP compatibility):

    ```powershell
    .venv\Scripts\playwright install
    ```

5. **Load the Custom Chrome Extension**:
   - Open Chrome and go to `chrome://extensions/`.
   - Enable "Developer mode" (toggle in the top right).
   - Click "Load unpacked" and select the `src/bridge/extension` folder from this repository.
   - The Crewight extension should now be installed and active.

### Configuration

Copy `.env.example` to `.env` and configure your settings:

```env
# LLM Configuration
OPENAI_API_KEY=sk-mecRZ326kTQ5VGc0NWKsOA
OPENAI_API_BASE=https://llm.artemis-ai.ca/v1
MODEL_NAME=deepseek-v3.1-671b-cloud

# Browser Settings (CDP-specific)
BROWSER_USE_HEADLESS=false  # Set to false to see the Chrome browser
BROWSER_WINDOW_WIDTH=1280
BROWSER_WINDOW_HEIGHT=1024

# Service Settings
BROWSER_USE_HOST=0.0.0.0
BROWSER_USE_PORT=4999
```

## 🏃 Usage

### 1. Start the Browser Service

The CDP extension service must be running for the agents to work.

```powershell
.venv\Scripts\python crewai_tools/browser_use_tool/browser_use_service.py
```

### 2. Run the Research Crew

You can run the provided examples to see the agent in action with Chrome CDP.

**Example 1: Tech Trends**

```powershell
.venv\Scripts\python examples/example_1_tech_trends.py
```

**Example 2: Crypto Prices**

```powershell
.venv\Scripts\python examples/example_2_financial_snapshot.py
```

**Example 3: Product Comparison**

```powershell
.venv\Scripts\python examples/example_3_competitor_analysis.py
```

## 🔧 Troubleshooting

### Login to CrewAI

If you need to login to CrewAI and are on Windows, use the patched script:

```powershell
.venv\Scripts\python login_patch.py
```

### Windows Signal Errors

If you encounter `AttributeError: module 'signal' has no attribute 'SIGHUP'`, ensure you are using the provided example scripts or the patched test scripts (`tests/test_crew_win.py`), which include necessary compatibility patches.

### CDP-Specific Issues

- Ensure Chrome is installed and up-to-date for full CDP support.
- If headless mode is enabled, set `BROWSER_USE_HEADLESS=true` in `.env` for background execution.

### Extension Issues

- Verify the Crewight extension is loaded and enabled in `chrome://extensions/`.
- If the extension doesn't connect, check the console for errors and ensure the service is running.
- Reload the extension after updates by clicking the refresh icon in the extensions page.

## 📂 Project Structure

- `src/bridge/extension/`: The custom Chrome extension (Crewight) for CrewAI connectivity and browser control.
- `src/research_crew/`: Core CrewAI implementation with extension integration.
- `crewai_tools/`: The custom BrowserUseTool and Service.
- `examples/`: Ready-to-run scenarios demonstrating extension-based research.
- `logs/`: Execution logs (check here if something seems silent).
