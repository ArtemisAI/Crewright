# Hyperbrowser Load Tool

Hyperbrowser is a powerful web automation and scraping platform that provides reliable browser infrastructure for AI agents.

## Description

Hyperbrowser is a developer platform that provides serverless infrastructure for running, managing, and monitoring headless browsers. It offers features like:

- Serverless Infrastructure providing reliable browsers to extract data from complex UIs
- Stealth Mode with included fingerprinting tactics and automatic captcha solving
- Session Debugger to inspect your Browser Session with networks timeline and logs
- Live Debug to quickly debug your automation

## Installation

Get an API key from [hyperbrowser.ai](https://hyperbrowser.ai/) and set it in environment variables (`HYPERBROWSER_API_KEY`).
Install the Hyperbrowser SDK along with `crewai[tools]` package:

```bash
pip install hyperbrowser 'crewai[tools]'
```

## Example

Utilize the HyperbrowserLoadTool as follows to allow your agent to load websites:

```python
from crewai_tools import HyperbrowserLoadTool

tool = HyperbrowserLoadTool()
```

## Arguments

The following parameters can be used to customize the HyperbrowserLoadTool's behavior:

- `api_key`: Optional. Hyperbrowser API key. Default is HYPERBROWSER_API_KEY env variable.
- `session_id`: Optional. Provide an existing Session ID.
- `text_content`: Optional. Retrieve only text content. Default is False.
- `proxy`: Optional. Enable/Disable Proxies. Default is False.