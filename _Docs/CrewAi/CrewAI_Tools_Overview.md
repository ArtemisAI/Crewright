# Tools Overview

Tools in CrewAI extend agent capabilities beyond basic language model interactions. They enable agents to interact with external systems, perform computations, access data sources, and execute specialized tasks.

## What are Tools?

Tools are modular components that provide specific functionalities to agents. They can:

- Access external APIs and services
- Perform file system operations
- Execute code and computations
- Search and retrieve information
- Interact with databases
- Generate content in various formats

## Built-in Tools

CrewAI provides a comprehensive set of built-in tools organized by functionality.

### Web and Search Tools

#### SerperDevTool
Search the web using Serper.dev API for real-time information.

```python
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()
```

**Configuration:**
- Requires `SERPER_API_KEY` environment variable
- Supports both search and news queries
- Returns structured search results

#### ScrapeWebsiteTool
Extract content from websites.

```python
from crewai_tools import ScrapeWebsiteTool

scraper = ScrapeWebsiteTool()
```

**Features:**
- Extracts main content from web pages
- Handles JavaScript-rendered content
- Returns clean, readable text

#### WebsiteSearchTool
Search within specific websites.

```python
from crewai_tools import WebsiteSearchTool

site_search = WebsiteSearchTool(website_url="https://docs.crewai.com")
```

**Use cases:**
- Documentation search
- Company website content retrieval
- Knowledge base queries

### File System Tools

#### FileReadTool
Read content from files.

```python
from crewai_tools import FileReadTool

file_reader = FileReadTool()
```

**Capabilities:**
- Read text files of various formats
- Handle large files with chunking
- Support for different encodings

#### DirectoryReadTool
Navigate and list directory contents.

```python
from crewai_tools import DirectoryReadTool

dir_reader = DirectoryReadTool()
```

**Features:**
- List directory contents
- Get file metadata
- Recursive directory traversal

### Data Analysis Tools

#### CSVSearchTool
Search and analyze CSV files.

```python
from crewai_tools import CSVSearchTool

csv_analyzer = CSVSearchTool()
```

**Features:**
- Query CSV data with natural language
- Perform aggregations and filtering
- Generate insights from tabular data

#### JSONSearchTool
Search and analyze JSON data.

```python
from crewai_tools import JSONSearchTool

json_analyzer = JSONSearchTool()
```

**Capabilities:**
- Query complex JSON structures
- Extract specific data patterns
- Handle nested objects and arrays

### Development Tools

#### CodeDocsSearchTool
Search programming documentation.

```python
from crewai_tools import CodeDocsSearchTool

docs_search = CodeDocsSearchTool()
```

**Supported documentation:**
- Python standard library
- Popular frameworks (Django, Flask, FastAPI)
- JavaScript libraries (React, Node.js)
- API documentation

#### GithubSearchTool
Search GitHub repositories.

```python
from crewai_tools import GithubSearchTool

github_search = GithubSearchTool()
```

**Features:**
- Search code across repositories
- Find issues and pull requests
- Access repository information

### Communication Tools

#### EmailTool
Send and manage emails.

```python
from crewai_tools import EmailTool

email_tool = EmailTool()
```

**Capabilities:**
- Send emails with attachments
- Read inbox messages
- Manage email threads

### Content Creation Tools

#### TXTSearchTool
Search text files and documents.

```python
from crewai_tools import TXTSearchTool

text_search = TXTSearchTool()
```

**Use cases:**
- Document analysis
- Log file searching
- Text corpus queries

### Integration Tools

#### BrowserbaseLoadTool
Load web content using Browserbase.

```python
from crewai_tools import BrowserbaseLoadTool

browser_tool = BrowserbaseLoadTool()
```

**Features:**
- Headless browser automation
- JavaScript execution
- Screenshot capture

#### LlamaIndexTool
Integrate with LlamaIndex for advanced RAG.

```python
from crewai_tools import LlamaIndexTool

llamaindex_tool = LlamaIndexTool()
```

**Capabilities:**
- Document indexing
- Semantic search
- Knowledge base creation

## Custom Tool Creation

### Basic Custom Tool

Create custom tools by inheriting from BaseTool:

```python
from crewai.tools import BaseTool
from typing import Any

class CalculatorTool(BaseTool):
    name: str = "Calculator"
    description: str = "Perform mathematical calculations"

    def _run(self, expression: str) -> str:
        """Execute mathematical expression"""
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
```

### Tool with Arguments

```python
class WeatherTool(BaseTool):
    name: str = "Weather Checker"
    description: str = "Get weather information for a location"

    def _run(self, location: str, unit: str = "celsius") -> str:
        """Get weather for specified location"""
        # Implementation here
        return f"Weather for {location}: Sunny, 25°C"
```

### Async Tool

```python
import asyncio
from crewai.tools import BaseTool

class AsyncWebScraperTool(BaseTool):
    name: str = "Async Web Scraper"
    description: str = "Asynchronously scrape web content"

    async def _arun(self, url: str) -> str:
        """Async web scraping implementation"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
```

### Tool with Configuration

```python
class DatabaseTool(BaseTool):
    name: str = "Database Query Tool"
    description: str = "Execute database queries"

    def __init__(self, connection_string: str):
        super().__init__()
        self.connection_string = connection_string
        self.connection = None

    def _run(self, query: str) -> str:
        """Execute database query"""
        # Database implementation
        return "Query results"
```

## Tool Integration with Agents

### Adding Tools to Agents

```python
from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

research_agent = Agent(
    role="Research Analyst",
    goal="Gather comprehensive information",
    backstory="Expert researcher with access to web resources",
    tools=[
        SerperDevTool(),
        ScrapeWebsiteTool()
    ],
    verbose=True
)
```

### Tool Configuration

```python
# Configure tools with specific parameters
search_tool = SerperDevTool(
    search_url="https://google.serper.dev/search",
    n_results=10
)

scraper_tool = ScrapeWebsiteTool(
    continue_on_error=True,
    main_content=True
)

agent = Agent(
    role="Content Researcher",
    goal="Research and summarize web content",
    backstory="Web research specialist",
    tools=[search_tool, scraper_tool]
)
```

## Tool Categories and Use Cases

### Research and Information Gathering

```python
research_tools = [
    SerperDevTool(),           # Web search
    ScrapeWebsiteTool(),       # Content extraction
    WebsiteSearchTool(),       # Site-specific search
    CodeDocsSearchTool(),      # Documentation search
    GithubSearchTool()         # Code repository search
]

researcher = Agent(
    role="Research Analyst",
    goal="Gather and synthesize information",
    tools=research_tools
)
```

### Data Analysis and Processing

```python
data_tools = [
    CSVSearchTool(),           # CSV analysis
    JSONSearchTool(),          # JSON querying
    FileReadTool(),            # File reading
    DirectoryReadTool()        # Directory navigation
]

data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze and process data",
    tools=data_tools
)
```

### Content Creation and Management

```python
content_tools = [
    TXTSearchTool(),           # Text search
    FileReadTool(),            # Content reading
    DirectoryReadTool()        # File organization
]

content_creator = Agent(
    role="Content Creator",
    goal="Create and manage content",
    tools=content_tools
)
```

### Development and Coding

```python
dev_tools = [
    CodeDocsSearchTool(),      # API documentation
    GithubSearchTool(),        # Code search
    FileReadTool(),            # Code reading
    DirectoryReadTool()        # Project navigation
]

developer = Agent(
    role="Software Developer",
    goal="Write and maintain code",
    tools=dev_tools
)
```

## Tool Best Practices

### 1. Tool Selection

Choose tools that complement agent capabilities:

```python
# Good: Focused toolset for specific task
writer = Agent(
    role="Technical Writer",
    goal="Create API documentation",
    tools=[CodeDocsSearchTool(), FileReadTool()]
)

# Avoid: Overwhelming toolset
jack_of_all_trades = Agent(
    role="General Assistant",
    goal="Help with various tasks",
    tools=[SerperDevTool(), ScrapeWebsiteTool(), CSVSearchTool(), JSONSearchTool(), CodeDocsSearchTool(), GithubSearchTool(), FileReadTool(), DirectoryReadTool()]
)
```

### 2. Error Handling

Implement robust error handling in custom tools:

```python
class RobustApiTool(BaseTool):
    name: str = "Robust API Tool"
    description: str = "Call external APIs with error handling"

    def _run(self, endpoint: str) -> str:
        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return "Error: Request timed out"
        except requests.exceptions.HTTPError as e:
            return f"Error: HTTP {e.response.status_code}"
        except Exception as e:
            return f"Error: {str(e)}"
```

### 3. Resource Management

Manage resources appropriately in tools:

```python
class DatabaseTool(BaseTool):
    name: str = "Database Tool"
    description: str = "Query database with connection pooling"

    def __init__(self):
        super().__init__()
        self.pool = None

    def _run(self, query: str) -> str:
        if not self.pool:
            self.pool = self._create_connection_pool()

        try:
            with self.pool.get_connection() as conn:
                # Execute query
                return "Query results"
        except Exception as e:
            return f"Database error: {str(e)}"
```

### 4. Security Considerations

Implement security measures in tools:

```python
class SecureApiTool(BaseTool):
    name: str = "Secure API Tool"
    description: str = "Secure API calls with authentication"

    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key
        self.allowed_domains = ["trusted-api.com", "secure-service.org"]

    def _run(self, url: str) -> str:
        parsed_url = urlparse(url)
        if parsed_url.netloc not in self.allowed_domains:
            return "Error: Domain not allowed"

        headers = {"Authorization": f"Bearer {self.api_key}"}
        # Make secure API call
        return "Secure API response"
```

## Tool Testing and Validation

### Unit Testing Tools

```python
import pytest
from your_tools import CalculatorTool

def test_calculator_tool():
    tool = CalculatorTool()
    result = tool._run("2 + 2")
    assert result == "4"

def test_calculator_error_handling():
    tool = CalculatorTool()
    result = tool._run("invalid expression")
    assert "Error" in result
```

### Integration Testing

```python
def test_agent_with_tools():
    agent = Agent(
        role="Calculator",
        goal="Perform calculations",
        tools=[CalculatorTool()]
    )

    task = Task(
        description="Calculate 5 + 3",
        expected_output="The result of 5 + 3",
        agent=agent
    )

    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()

    assert "8" in result
```

## Tool Performance Optimization

### Caching

```python
from functools import lru_cache

class CachedSearchTool(BaseTool):
    name: str = "Cached Search Tool"
    description: str = "Search with caching"

    @lru_cache(maxsize=100)
    def _run(self, query: str) -> str:
        # Expensive search operation
        return f"Results for: {query}"
```

### Async Operations

```python
import asyncio

class AsyncBatchTool(BaseTool):
    name: str = "Async Batch Tool"
    description: str = "Process multiple requests asynchronously"

    async def _arun(self, requests: List[str]) -> str:
        tasks = [self._process_request(req) for req in requests]
        results = await asyncio.gather(*tasks)
        return "\n".join(results)

    async def _process_request(self, request: str) -> str:
        # Simulate async processing
        await asyncio.sleep(0.1)
        return f"Processed: {request}"
```

## Tool Discovery and Management

### Tool Registry

```python
class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name: str, tool_class):
        self.tools[name] = tool_class

    def get_tool(self, name: str, **kwargs):
        tool_class = self.tools.get(name)
        if tool_class:
            return tool_class(**kwargs)
        raise ValueError(f"Tool {name} not found")

# Usage
registry = ToolRegistry()
registry.register("calculator", CalculatorTool)
registry.register("search", SerperDevTool)

calculator = registry.get_tool("calculator")
search = registry.get_tool("search", api_key="your-key")
```

## Common Tool Patterns

### 1. Wrapper Tools

```python
class ApiWrapperTool(BaseTool):
    """Wrapper for third-party API"""

    def __init__(self, api_client):
        super().__init__()
        self.client = api_client

    def _run(self, endpoint: str, **params) -> str:
        response = self.client.call(endpoint, **params)
        return response.data
```

### 2. Composite Tools

```python
class ResearchSuiteTool(BaseTool):
    """Composite tool combining multiple research capabilities"""

    def __init__(self):
        super().__init__()
        self.search_tool = SerperDevTool()
        self.scraper_tool = ScrapeWebsiteTool()

    def _run(self, query: str) -> str:
        # Use search to find relevant URLs
        search_results = self.search_tool._run(query)

        # Extract URLs and scrape content
        urls = self._extract_urls(search_results)
        content = []

        for url in urls[:3]:  # Limit to top 3 results
            scraped = self.scraper_tool._run(url)
            content.append(scraped)

        return "\n\n".join(content)
```

### 3. Configurable Tools

```python
class ConfigurableTool(BaseTool):
    """Tool with runtime configuration"""

    def __init__(self, config: dict):
        super().__init__()
        self.config = config

    def _run(self, input_data: str, **overrides) -> str:
        # Merge config with overrides
        effective_config = {**self.config, **overrides}

        # Use configuration in processing
        return f"Processed with config: {effective_config}"
```

## Next Steps

- Learn about [Agents](https://docs.crewai.com/en/concepts/agents) to understand how tools enhance agent capabilities
- Explore [Tasks](https://docs.crewai.com/en/concepts/tasks) to see how tools are used in task execution
- Check out [Crews](https://docs.crewai.com/en/concepts/crews) for multi-agent tool coordination
- Read about [Flows](https://docs.crewai.com/en/concepts/flows) for complex tool orchestration