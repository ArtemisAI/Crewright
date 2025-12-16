# Agents

Agents are the core of CrewAI. They are autonomous entities that can perform tasks, make decisions, and collaborate with other agents to achieve goals.

## What are Agents?

Agents in CrewAI are AI-powered entities designed to perform specific roles and tasks. Each agent has:

- **Role**: Defines the agent's function and expertise area
- **Goal**: The objective the agent aims to achieve
- **Backstory**: Context that shapes the agent's behavior and decision-making
- **Tools**: Capabilities the agent can use to accomplish tasks
- **LLM**: The language model that powers the agent's intelligence

## Creating Agents

### Basic Agent Creation

```python
from crewai import Agent

agent = Agent(
    role="Data Analyst",
    goal="Analyze data and provide insights",
    backstory="You are an experienced data analyst with expertise in statistical analysis and data visualization.",
    verbose=True
)
```

### Agent with Tools

```python
from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

agent = Agent(
    role="Research Analyst",
    goal="Gather and analyze information from various sources",
    backstory="You are a thorough researcher who excels at finding and synthesizing information from multiple sources.",
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    verbose=True
)
```

### Agent with Custom LLM

```python
from crewai import Agent
from crewai.llms import LLM

agent = Agent(
    role="Content Writer",
    goal="Create engaging content",
    backstory="You are a creative writer with a talent for crafting compelling narratives.",
    llm=LLM(
        model="gpt-4",
        temperature=0.7,
        api_key="your-api-key"
    ),
    verbose=True
)
```

## Agent Configuration

### Using YAML Configuration

You can define agents using YAML files for better organization and reusability.

**agents.yaml**
```yaml
data_analyst:
  role: "Senior Data Analyst"
  goal: "Analyze complex datasets and provide actionable insights"
  backstory: "You are an experienced data analyst with 10+ years of experience in statistical analysis, machine learning, and data visualization. You excel at finding patterns in data and communicating insights to stakeholders."
  llm: "gpt-4"
  verbose: true

researcher:
  role: "Research Specialist"
  goal: "Conduct thorough research on given topics"
  backstory: "You are a meticulous researcher with expertise in academic and industry research. You have access to various tools and databases to gather comprehensive information."
  tools:
    - "SerperDevTool"
    - "ScrapeWebsiteTool"
  verbose: true
```

### Using CrewAI Project Structure

With the CrewAI project structure, you can define agents as methods in your crew class:

```python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MyCrew:
    """My crew"""

    @agent
    def data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analyst'],
            verbose=True
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
```

## Agent Parameters

### Core Parameters

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `role` | str | The agent's role/function | Yes |
| `goal` | str | The agent's objective | Yes |
| `backstory` | str | Context for the agent's behavior | Yes |
| `llm` | LLM | Language model configuration | No |
| `tools` | List[Tool] | Tools available to the agent | No |
| `verbose` | bool | Enable detailed logging | No |

### Advanced Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `allow_delegation` | bool | Allow task delegation to other agents | True |
| `max_iter` | int | Maximum iterations for task completion | 25 |
| `max_rpm` | int | Maximum requests per minute | None |
| `max_execution_time` | int | Maximum execution time in seconds | None |
| `memory` | bool | Enable agent memory | True |
| `cache` | bool | Enable caching | True |
| `system_template` | str | Custom system message template | None |
| `prompt_template` | str | Custom prompt template | None |
| `response_template` | str | Custom response template | None |

## Agent Tools

Tools extend an agent's capabilities beyond basic LLM interactions. CrewAI supports various built-in tools and allows custom tool creation.

### Built-in Tools

```python
from crewai_tools import (
    SerperDevTool,      # Web search
    ScrapeWebsiteTool,  # Website scraping
    CodeDocsSearchTool, # Code documentation search
    DirectoryReadTool,  # File system operations
    FileReadTool,       # File reading
    CSVSearchTool,      # CSV data analysis
    JSONSearchTool      # JSON data analysis
)

research_agent = Agent(
    role="Research Analyst",
    goal="Gather comprehensive information",
    backstory="Expert researcher with access to various data sources",
    tools=[
        SerperDevTool(),
        ScrapeWebsiteTool(),
        CodeDocsSearchTool()
    ]
)
```

### Custom Tools

You can create custom tools by inheriting from the BaseTool class:

```python
from crewai.tools import BaseTool
from typing import Any

class CustomCalculatorTool(BaseTool):
    name: str = "Calculator"
    description: str = "Perform mathematical calculations"

    def _run(self, expression: str) -> str:
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"

calculator_agent = Agent(
    role="Math Assistant",
    goal="Solve mathematical problems",
    backstory="Expert mathematician with calculation tools",
    tools=[CustomCalculatorTool()]
)
```

## Agent Memory

Agents can maintain memory across interactions, allowing them to build context and learn from previous tasks.

```python
memory_agent = Agent(
    role="Learning Assistant",
    goal="Provide personalized learning experiences",
    backstory="Adaptive tutor that remembers student progress and preferences",
    memory=True,
    max_memory_items=100
)
```

## Agent Delegation

Agents can delegate tasks to other agents when working in crews, enabling collaborative problem-solving.

```python
team_leader = Agent(
    role="Project Manager",
    goal="Coordinate team efforts and ensure project success",
    backstory="Experienced project manager who delegates tasks effectively",
    allow_delegation=True
)

developer = Agent(
    role="Software Developer",
    goal="Write clean, efficient code",
    backstory="Skilled developer with expertise in multiple programming languages",
    allow_delegation=False  # This agent doesn't delegate tasks
)
```

## Agent Caching

Caching can improve performance by storing and reusing previous computations.

```python
cached_agent = Agent(
    role="Data Processor",
    goal="Process and analyze data efficiently",
    backstory="Efficient data processor that optimizes repeated operations",
    cache=True,
    cache_timeout=3600  # Cache for 1 hour
)
```

## Best Practices

### 1. Clear Role Definition

Define specific, actionable roles that clearly delineate responsibilities:

```python
# Good
research_agent = Agent(
    role="Market Research Analyst",
    goal="Analyze market trends and consumer behavior",
    backstory="Specialized in market analysis with 5+ years experience"
)

# Avoid
generic_agent = Agent(
    role="Helper",
    goal="Help with things",
    backstory="I help"
)
```

### 2. Appropriate Tool Selection

Choose tools that complement the agent's capabilities:

```python
data_scientist = Agent(
    role="Data Scientist",
    goal="Build predictive models and analyze datasets",
    backstory="PhD in Statistics with expertise in machine learning",
    tools=[
        CSVSearchTool(),
        JSONSearchTool(),
        CodeDocsSearchTool()  # For API documentation
    ]
)
```

### 3. Balanced Backstory

Provide context without overwhelming the agent:

```python
# Good
writer = Agent(
    role="Content Writer",
    goal="Create engaging blog posts",
    backstory="Creative writer with 3 years experience in tech blogging, specializing in AI and software development topics"
)

# Avoid
overloaded_writer = Agent(
    role="Content Writer",
    goal="Create engaging blog posts",
    backstory="Born in 1985 in New York City, graduated from Harvard with a degree in English Literature, worked at 5 different companies including Google and Microsoft, has 3 cats named Whiskers, Mittens, and Fluffy, enjoys hiking on weekends, favorite color is blue, allergic to peanuts..."
)
```

### 4. Resource Management

Configure resource limits appropriately:

```python
production_agent = Agent(
    role="API Processor",
    goal="Process API requests efficiently",
    backstory="Optimized for high-throughput API processing",
    max_rpm=100,           # Rate limiting
    max_execution_time=30, # Timeout protection
    cache=True            # Performance optimization
)
```

## Common Patterns

### Research Agent Pattern

```python
research_agent = Agent(
    role="Research Analyst",
    goal="Gather and synthesize information from multiple sources",
    backstory="Expert researcher with access to web search, academic databases, and industry reports",
    tools=[
        SerperDevTool(),
        ScrapeWebsiteTool(),
        DirectoryReadTool()
    ],
    allow_delegation=False,
    verbose=True
)
```

### Coding Agent Pattern

```python
coding_agent = Agent(
    role="Software Developer",
    goal="Write clean, efficient, and well-documented code",
    backstory="Senior developer with expertise in Python, JavaScript, and cloud technologies",
    tools=[
        CodeDocsSearchTool(),
        FileReadTool(),
        DirectoryReadTool()
    ],
    llm=LLM(model="gpt-4", temperature=0.1),  # Lower temperature for code
    allow_delegation=True,
    verbose=True
)
```

### Analysis Agent Pattern

```python
analysis_agent = Agent(
    role="Data Analyst",
    goal="Analyze data and provide actionable insights",
    backstory="Experienced analyst skilled in statistical analysis and data visualization",
    tools=[
        CSVSearchTool(),
        JSONSearchTool()
    ],
    memory=True,  # Remember previous analyses
    cache=True,   # Cache expensive computations
    verbose=True
)
```

## Troubleshooting

### Common Issues

1. **Agent not responding**: Check LLM configuration and API keys
2. **Tools not working**: Verify tool initialization and required dependencies
3. **Memory issues**: Monitor memory usage and adjust max_memory_items
4. **Performance problems**: Enable caching and adjust rate limits

### Debugging

Enable verbose logging to troubleshoot agent behavior:

```python
debug_agent = Agent(
    role="Debug Assistant",
    goal="Help identify and resolve issues",
    backstory="Expert debugger with systematic troubleshooting approach",
    verbose=True,
    max_iter=50  # Allow more iterations for complex debugging
)
```

## Next Steps

- Learn about [Tasks](https://docs.crewai.com/en/concepts/tasks) to understand how agents execute work
- Explore [Crews](https://docs.crewai.com/en/concepts/crews) to see how multiple agents collaborate
- Check out [Tools](https://docs.crewai.com/en/concepts/tools) for available capabilities
- Read about [Flows](https://docs.crewai.com/en/concepts/flows) for complex workflow orchestration