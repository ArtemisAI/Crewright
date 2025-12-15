# ArtemisAI CrewAI + Browser Use Integration

**Developed by [ArtemisAI](https://artemis-ai.ca)**

This project integrates [CrewAI](https://crewai.com) with [Browser Use](https://github.com/browser-use/browser-use) to enable AI agents to perform complex, headed (visible) web research tasks.

## 🚀 Features

- **Headed Browser Automation**: Watch the agent browse the web in real-time.
- **Service-Based Architecture**: Separation of concerns between the CrewAI agent (client) and the Browser execution (server).
- **Configurable**: Fully controlled via `.env` file (LLM providers, window size, headless mode).
- **Windows Compatible**: Includes patches for Windows signal handling issues.
- **Observability**: Integrated with CrewAI traces (telemetry).

## 🛠️ Setup

### Prerequisites

- Python 3.10+
- [Playwright](https://playwright.dev/)

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

4. **Install Playwright browsers**:

    ```powershell
    .venv\Scripts\playwright install
    ```

### Configuration

Copy `.env.example` to `.env` and configure your settings:

```env
# LLM Configuration
OPENAI_API_KEY=sk-mecRZ326kTQ5VGc0NWKsOA
OPENAI_API_BASE=https://llm.artemis-ai.ca/v1
MODEL_NAME=deepseek-v3.1-671b-cloud

# Browser Settings
BROWSER_USE_HEADLESS=false  # Set to false to see the browser
BROWSER_WINDOW_WIDTH=1280
BROWSER_WINDOW_HEIGHT=1024

# Service Settings
BROWSER_USE_HOST=0.0.0.0
BROWSER_USE_PORT=4999
```

## 🏃 Usage

### 1. Start the Browser Service

The service must be running for the agents to work.

```powershell
.venv\Scripts\python crewai_tools/browser_use_tool/browser_use_service.py
```

### 2. Run the Research Crew

You can run the provided examples to see the agent in action.

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

## 📂 Project Structure

- `src/research_crew/`: Core CrewAI implementation.
- `crewai_tools/`: The custom BrowserUseTool and Service.
- `examples/`: Ready-to-run scenarios.
- `logs/`: Execution logs (check here if something seems silent).
