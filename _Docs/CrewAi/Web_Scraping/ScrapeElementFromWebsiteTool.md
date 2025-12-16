# Scrape Element From Website Tool

A tool that can be used to read a website content and extract specific elements.

## Description

The ScrapeElementFromWebsiteTool is designed to extract and read the content of a specified website, with the ability to target specific elements using CSS selectors. It provides precise extraction of content from web pages by allowing users to specify which elements to extract.

## Installation

To use this tool, you need to install the CrewAI tools package:

```bash
pip install 'crewai[tools]'
```

## Example

The following example demonstrates how to use the ScrapeElementFromWebsiteTool with a CrewAI agent:

```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeElementFromWebsiteTool

# Initialize the tool
scrape_tool = ScrapeElementFromWebsiteTool()

# Define an agent that uses the tool
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract specific information from websites",
    backstory="An expert web scraper who can extract targeted content from websites using CSS selectors.",
    tools=[scrape_tool],
    verbose=True,
)

# Example task to scrape specific content from a website
scrape_task = Task(
    description="Extract the main content from the homepage of example.com using the CSS selector '.main-content'",
    expected_output="The main content from example.com's homepage.",
    agent=web_scraper_agent,
)

# Create and run the crew
crew = Crew(
    agents=[web_scraper_agent],
    tasks=[scrape_task],
    verbose=True,
    process=Process.sequential,
)
result = crew.kickoff()
```

You can also initialize the tool with predefined parameters:

```python
# Initialize the tool with predefined parameters
scrape_tool = ScrapeElementFromWebsiteTool(
    website_url='https://example.com',
    css_element='.main-content'
)
```

## Parameters

The ScrapeElementFromWebsiteTool accepts the following parameters during initialization:

- `website_url`: Optional. The URL of the website to scrape. If provided during initialization, the agent won't need to specify it when using the tool.
- `css_element`: Optional. The CSS selector for the elements to extract. If provided during initialization, the agent won't need to specify it when using the tool.

When using the tool with an agent, the agent will need to provide the following parameters (unless they were specified during initialization):

- `website_url`: Required. The URL of the website to scrape.
- `css_element`: Required. The CSS selector for the elements to extract.

## Implementation Details

The ScrapeElementFromWebsiteTool uses CSS selectors to target specific elements on web pages. This allows for precise extraction of content, making it ideal for scraping structured data or specific sections of websites.