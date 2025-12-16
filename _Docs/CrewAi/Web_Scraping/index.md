# CrewAI Web Scraping & Browsing Tools

This directory contains comprehensive documentation for all CrewAI web scraping and browsing tools.

## Overview

CrewAI provides a comprehensive suite of web scraping and browsing tools that enable AI agents to extract data from websites, interact with web applications, and perform automated browsing tasks. These tools range from simple content extraction to advanced browser automation with anti-bot bypass capabilities.

## Tool Categories

### Basic Scraping Tools
- **[ScrapeWebsiteTool](ScrapeWebsiteTool.md)** - Simple website content extraction
- **[ScrapeElementFromWebsiteTool](ScrapeElementFromWebsiteTool.md)** - Targeted element extraction using CSS selectors

### Advanced Scraping Services
- **[FirecrawlCrawlWebsiteTool](FirecrawlCrawlWebsiteTool.md)** - Website crawling with structured data conversion
- **[FirecrawlScrapeWebsiteTool](FirecrawlScrapeWebsiteTool.md)** - Single page scraping with LLM-based extraction
- **[FirecrawlSearchTool](FirecrawlSearchTool.md)** - Web search with content extraction
- **[ScrapFlyScrapeTool](ScrapFlyScrapeTool.md)** - Advanced scraping with anti-bot bypass and proxies
- **[ScrapeGraphScrapeTool](ScrapeGraphScrapeTool.md)** - AI-powered intelligent content extraction
- **[SpiderTool](SpiderTool.md)** - High-performance open source scraper and crawler

### Browser Automation Tools
- **[SeleniumScrapingTool](SeleniumScrapingTool.md)** - Full browser automation for dynamic content
- **[BrowserBaseLoadTool](BrowserBaseLoadTool.md)** - Serverless browser infrastructure
- **[HyperbrowserLoadTool](HyperbrowserLoadTool.md)** - Advanced browser automation platform
- **[StagehandTool](StagehandTool.md)** - AI-powered browser interaction and automation

### Specialized Scrapers
- **[OxylabsScrapersTool](OxylabsScrapersTool.md)** - Enterprise-grade scrapers for Amazon, Google, and universal sites
- **[BrightDataTools](BrightDataTools.md)** - SERP search, web unlocker, and dataset API tools

## Quick Reference

| Tool | Purpose | Key Features |
|------|---------|--------------|
| ScrapeWebsiteTool | Basic content extraction | Simple, fast, no dependencies |
| ScrapeElementFromWebsiteTool | Targeted extraction | CSS selectors, precise targeting |
| Firecrawl Tools | Advanced scraping | Clean markdown output, LLM integration |
| ScrapFlyScrapeTool | Anti-bot scraping | Proxies, JavaScript rendering, bypass |
| ScrapeGraphScrapeTool | AI-powered extraction | Natural language prompts, intelligent parsing |
| SpiderTool | High-performance crawling | Fastest open source, LLM-ready data |
| SeleniumScrapingTool | Browser automation | Dynamic content, full browser control |
| BrowserBaseLoadTool | Serverless browsers | Stealth mode, captcha solving, debugging |
| HyperbrowserLoadTool | Advanced automation | Session management, live debugging |
| StagehandTool | AI browser interaction | Natural language commands, complex workflows |
| Oxylabs Tools | Enterprise scraping | Amazon, Google, universal scrapers |
| Bright Data Tools | Professional scraping | SERP search, web unlocker, datasets |

## Installation Requirements

Most tools require additional dependencies. Check individual tool documentation for specific installation commands.

Common requirements:
- `pip install 'crewai[tools]'` (base requirement)
- API keys for cloud services (Firecrawl, ScrapFly, etc.)
- Chrome/Chromium for Selenium-based tools
- Environment variables for authentication

## Usage Patterns

### Basic Scraping
```python
from crewai_tools import ScrapeWebsiteTool

tool = ScrapeWebsiteTool()
result = tool.run(website_url="https://example.com")
```

### Advanced Scraping with Configuration
```python
from crewai_tools import ScrapFlyScrapeTool

tool = ScrapFlyScrapeTool(api_key="your_key")
result = tool.run(
    url="https://example.com",
    scrape_format="markdown",
    scrape_config={"render_js": True, "proxy_pool": "residential"}
)
```

### Browser Automation
```python
from crewai_tools import SeleniumScrapingTool

tool = SeleniumScrapingTool()
result = tool.run(
    website_url="https://example.com",
    css_element=".content",
    wait_time=3
)
```

## Best Practices

1. **Choose the Right Tool**: Match tool capabilities to your scraping needs
2. **Handle Rate Limits**: Implement delays and respect website terms of service
3. **Error Handling**: Use built-in error handling features when available
4. **API Keys**: Securely manage API keys and monitor usage
5. **Legal Compliance**: Ensure scraping activities comply with applicable laws

## Related Documentation

- [CrewAI Tools Overview](../CrewAI_Tools_Overview.md)
- [CrewAI Agents](../CrewAI_Agents.md)
- [CrewAI Tasks](../CrewAI_Tasks.md)

## Support

For tool-specific issues, refer to the individual tool documentation or check the CrewAI documentation at https://docs.crewai.com/