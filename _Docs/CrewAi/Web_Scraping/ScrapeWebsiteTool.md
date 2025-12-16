# Scrape Website Tool

A tool that can be used to read a website content.

## Description

The ScrapeWebsiteTool is designed to extract and read the content of a specified website. It provides a simple way to scrape web content and return it in a clean, readable format.

## Installation

To use this tool, you need to install the CrewAI tools package:

```bash
pip install 'crewai[tools]'
```

## Example

The following example demonstrates how to use the ScrapeWebsiteTool with a CrewAI agent:

```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool

# Initialize the tool
scrape_tool = ScrapeWebsiteTool()

# Define an agent that uses the tool
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract information from websites",
    backstory="An expert web scraper who can extract content from any website.",
    tools=[scrape_tool],
    verbose=True,
)

# Example task to scrape content from a website
scrape_task = Task(
    description="Extract the main content from the homepage of example.com",
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
scrape_tool = ScrapeWebsiteTool(website_url='https://example.com')
```

## Parameters

The ScrapeWebsiteTool accepts the following parameters during initialization:

- `website_url`: Optional. The URL of the website to scrape. If provided during initialization, the agent won't need to specify it when using the tool.

When using the tool with an agent, the agent will need to provide the following parameters (unless they were specified during initialization):

- `website_url`: Required. The URL of the website to scrape.

## Implementation Details

The ScrapeWebsiteTool uses standard web scraping techniques to extract content from websites. It handles common web scraping challenges and returns clean, readable content.