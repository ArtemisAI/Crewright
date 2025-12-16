# Browserbase Web Loader Tool

Browserbase is a developer platform to reliably run, manage, and monitor headless browsers.

## Description

Browserbase is a developer platform to reliably run, manage, and monitor headless browsers. Power your AI data retrievals with:

- Serverless Infrastructure providing reliable browsers to extract data from complex UIs
- Stealth Mode with included fingerprinting tactics and automatic captcha solving
- Session Debugger to inspect your Browser Session with networks timeline and logs
- Live Debug to quickly debug your automation

## Installation

Get an API key and Project ID from browserbase.com and set it in environment variables (BROWSERBASE_API_KEY, BROWSERBASE_PROJECT_ID).
Install the Browserbase SDK along with crewai[tools] package:

```bash
pip install browserbase 'crewai[tools]'
```

## Example

Utilize the BrowserbaseLoadTool as follows to allow your agent to load websites:

```python
from crewai_tools import BrowserbaseLoadTool

# Initialize the tool with the Browserbase API key and Project ID
tool = BrowserbaseLoadTool()
```

## Arguments

The following parameters can be used to customize the BrowserbaseLoadTool's behavior:

- `api_key`: Optional. Browserbase API key. Default is BROWSERBASE_API_KEY env variable.
- `project_id`: Optional. Browserbase Project ID. Default is BROWSERBASE_PROJECT_ID env variable.
- `text_content`: Optional. Retrieve only text content. Default is False.
- `session_id`: Optional. Provide an existing Session ID.
- `proxy`: Optional. Enable/Disable Proxies. Default is False.