# CrewAI Tasks - Complete Documentation

## Overview

In the CrewAI framework, a `Task` is a specific assignment completed by an `Agent`. Tasks provide all necessary details for execution, such as a description, the agent responsible, required tools, and more, facilitating a wide range of action complexities. Tasks within CrewAI can be collaborative, requiring multiple agents to work together. This is managed through the task properties and orchestrated by the Crew's process, enhancing teamwork and efficiency.

CrewAI AOP includes a Visual Task Builder in Crew Studio that simplifies complex task creation and chaining. Design your task flows visually and test them in real-time without writing code. The Visual Task Builder enables:

- Drag-and-drop task creation
- Visual task dependencies and flow
- Real-time testing and validation
- Easy sharing and collaboration

## Task Execution Flow

Tasks can be executed in two ways:
- **Sequential**: Tasks are executed in the order they are defined
- **Hierarchical**: Tasks are assigned to agents based on their roles and expertise

The execution flow is defined when creating the crew:

```python
crew = Crew(
    agents=[agent1, agent2],
    tasks=[task1, task2],
    process=Process.sequential  # or Process.hierarchical
)
```

## Task Attributes

| Attribute | Type | Description | Required |
|-----------|------|-------------|----------|
| description | str | A clear, concise statement of what the task entails. | Yes |
| expected_output | str | A detailed description of what the task's completion looks like. | Yes |
| name | Optional[str] | A name identifier for the task. | No |
| agent | Optional[BaseAgent] | The agent responsible for executing the task. | No |
| tools | List[BaseTool] | The tools/resources the agent is limited to use for this task. | No |
| context | Optional[List["Task"]] | Other tasks whose outputs will be used as context for this task. | No |
| async_execution | Optional[bool] | Whether the task should be executed asynchronously. Defaults to False. | No |
| human_input | Optional[bool] | Whether the task should have a human review the final answer of the agent. Defaults to False. | No |
| markdown | Optional[bool] | Whether the task should instruct the agent to return the final answer formatted in Markdown. Defaults to False. | No |
| config | Optional[Dict[str, Any]] | Task-specific configuration parameters. | No |
| output_file | Optional[str] | File path for storing the task output. | No |
| create_directory | Optional[bool] | Whether to create the directory for output_file if it doesn't exist. Defaults to True. | No |
| output_json | Optional[Type[BaseModel]] | A Pydantic model to structure the JSON output. | No |
| output_pydantic | Optional[Type[BaseModel]] | A Pydantic model for task output. | No |
| callback | Optional[Any] | Function/object to be executed after task completion. | No |
| guardrail | Optional[Callable] | Function to validate task output before proceeding to next task. | No |
| guardrails | Optional[List[Callable] \| List[str]] | List of guardrails to validate task output before proceeding to next task. | No |
| guardrail_max_retries | Optional[int] | Maximum number of retries when guardrail validation fails. Defaults to 3. | No |

> **Note**: The task attribute `max_retries` is deprecated and will be removed in v1.0.0. Use `guardrail_max_retries` instead to control retry attempts when a guardrail fails.

## Creating Tasks

There are two ways to create tasks in CrewAI: using YAML configuration (recommended) or defining them directly in code.

### YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define tasks. We strongly recommend using this approach to define tasks in your CrewAI projects.

After creating your CrewAI project as outlined in the Installation section, navigate to the `src/latest_ai_development/config/tasks.yaml` file and modify the template to match your specific task requirements.

Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:

```python
crew.kickoff(inputs={'topic': 'AI Agents'})
```

Here's an example of how to configure tasks using YAML:

**tasks.yaml**
```yaml
research_task:
  description: >
    Conduct a thorough research about {topic}
    Make sure you find any interesting and relevant information given
    the current year is 2025.
  expected_output: >
    A list with 10 bullet points of the most relevant information about {topic}
  agent: researcher

reporting_task:
  description: >
    Review the context you got and expand each topic into a full section for a report.
    Make sure the report is detailed and contains any and all relevant information.
  expected_output: >
    A fully fledge reports with the mains topics, each with a full section of information.
    Formatted as markdown without '```'
  agent: reporting_analyst
  markdown: true
  output_file: report.md
```

To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:

**crew.py**
```python
# src/latest_ai_development/crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  @agent
  def researcher(self) -> Agent:
    return Agent(
      config=self.agents_config['researcher'], # type: ignore[index]
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def reporting_analyst(self) -> Agent:
    return Agent(
      config=self.agents_config['reporting_analyst'], # type: ignore[index]
      verbose=True
    )

  @task
  def research_task(self) -> Task:
    return Task(
      config=self.tasks_config['research_task'] # type: ignore[index]
    )

  @task
  def reporting_task(self) -> Task:
    return Task(
      config=self.tasks_config['reporting_task'] # type: ignore[index]
    )

  @crew
  def crew(self) -> Crew:
    return Crew(
      agents=[research_agent],
      tasks=[research_task, reporting_task],
      process=Process.sequential
    )
```

> **Note**: The names you use in your YAML files (`agents.yaml` and `tasks.yaml`) should match the method names in your Python code.

### Direct Code Definition (Alternative)

Alternatively, you can define tasks directly in your code without using YAML configuration:

**task.py**
```python
from crewai import Task

research_task = Task(
    description="""
        Conduct a thorough research about AI Agents.
        Make sure you find any interesting and relevant information given
        the current year is 2025.
    """,
    expected_output="""
        A list with 10 bullet points of the most relevant information about AI Agents
    """,
    agent=researcher
)

reporting_task = Task(
    description="""
        Review the context you got and expand each topic into a full section for a report.
        Make sure the report is detailed and contains any and all relevant information.
    """,
    expected_output="""
        A fully fledge reports with the mains topics, each with a full section of information.
    """,
    agent=reporting_analyst,
    markdown=True,  # Enable markdown formatting for the final output
    output_file="report.md"
)
```

> **Tip**: Directly specify an `agent` for assignment or let the hierarchical CrewAI's process decide based on roles, availability, etc.

## Task Output

Understanding task outputs is crucial for building effective AI workflows. CrewAI provides a structured way to handle task results through the `TaskOutput` class, which supports multiple output formats and can be easily passed between tasks.

The output of a task in CrewAI framework is encapsulated within the `TaskOutput` class. This class provides a structured way to access results of a task, including various formats such as raw output, JSON, and Pydantic models.

By default, the `TaskOutput` will only include the `raw` output. A `TaskOutput` will only include the `pydantic` or `json_dict` output if the original `Task` object was configured with `output_pydantic` or `output_json`, respectively.

### Task Output Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| description | str | Description of the task. |
| summary | Optional[str] | Summary of the task, auto-generated from the first 10 words of the description. |
| raw | str | The raw output of the task. This is the default format for the output. |
| pydantic | Optional[BaseModel] | A Pydantic model object representing the structured output of the task. |
| json_dict | Optional[Dict[str, Any]] | A dictionary representing the JSON output of the task. |
| agent | str | The agent that executed the task. |
| output_format | OutputFormat | The format of the task output, with options including RAW, JSON, and Pydantic. The default is RAW. |
| messages | list[LLMMessage] | The messages from the last task execution. |

### Task Methods and Properties

| Method/Property | Description |
|-----------------|-------------|
| json | Returns the JSON string representation of the task output if the output format is JSON. |
| to_dict | Converts the JSON and Pydantic outputs to a dictionary. |
| str | Returns the string representation of the task output, prioritizing Pydantic, then JSON, then raw. |

### Accessing Task Outputs

Once a task has been executed, its output can be accessed through the `output` attribute of the `Task` object. The `TaskOutput` class provides various ways to interact with and present this output.

#### Example

```python
# Example task
task = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    agent=research_agent,
    tools=[search_tool]
)

# Execute the crew
crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()

# Accessing the task output
task_output = task.output

print(f"Task Description: {task_output.description}")
print(f"Task Summary: {task_output.summary}")
print(f"Raw Output: {task_output.raw}")
if task_output.json_dict:
    print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
if task_output.pydantic:
    print(f"Pydantic Output: {task_output.pydantic}")
```

## Markdown Output Formatting

The `markdown` parameter enables automatic markdown formatting for task outputs. When set to `True`, the task will instruct the agent to format the final answer using proper Markdown syntax.

### Using Markdown Formatting

```python
# Example task with markdown formatting enabled
formatted_task = Task(
    description="Create a comprehensive report on AI trends",
    expected_output="A well-structured report with headers, sections, and bullet points",
    agent=reporter_agent,
    markdown=True  # Enable automatic markdown formatting
)
```

When `markdown=True`, the agent will receive additional instructions to format the output using:
- `#` for headers
- `**text**` for bold text
- `*text*` for italic text
- `-` or `*` for bullet points
- `` `code` `` for inline code
- ```language ``` for code blocks

### YAML Configuration with Markdown

**tasks.yaml**
```yaml
analysis_task:
  description: >
    Analyze the market data and create a detailed report
  expected_output: >
    A comprehensive analysis with charts and key findings
  agent: analyst
  markdown: true  # Enable markdown formatting
  output_file: analysis.md
```

### Benefits of Markdown Output

- **Consistent Formatting**: Ensures all outputs follow proper markdown conventions
- **Better Readability**: Structured content with headers, lists, and emphasis
- **Documentation Ready**: Output can be directly used in documentation systems
- **Cross-Platform Compatibility**: Markdown is universally supported

> **Note**: The markdown formatting instructions are automatically added to the task prompt when `markdown=True`, so you don't need to specify formatting requirements in your task description.

## Task Dependencies and Context

Tasks can depend on the output of other tasks using the `context` attribute. For example:

```python
research_task = Task(
    description="Research the latest developments in AI",
    expected_output="A list of recent AI developments",
    agent=researcher
)

analysis_task = Task(
    description="Analyze the research findings and identify key trends",
    expected_output="Analysis report of AI trends",
    agent=analyst,
    context=[research_task]  # This task will wait for research_task to complete
)
```

## Task Guardrails

Task guardrails provide a way to validate and transform task outputs before they are passed to the next task. This feature helps ensure data quality and provides feedback to agents when their output doesn't meet specific criteria.

CrewAI supports two types of guardrails:

1. **Function-based guardrails**: Python functions with custom validation logic, giving you complete control over the validation process and ensuring reliable, deterministic results.
2. **LLM-based guardrails**: String descriptions that use the agent's LLM to validate outputs based on natural language criteria. These are ideal for complex or subjective validation requirements.

### Function-Based Guardrails

To add a function-based guardrail to a task, provide a validation function through the `guardrail` parameter:

```python
from typing import Tuple, Union, Dict, Any
from crewai import TaskOutput

def validate_blog_content(result: TaskOutput) -> Tuple[bool, Any]:
    """Validate blog content meets requirements."""
    try:
        # Check word count
        word_count = len(result.raw.split())
        if word_count > 200:
            return (False, "Blog content exceeds 200 words")

        # Additional validation logic here
        return (True, result.raw.strip())
    except Exception as e:
        return (False, "Unexpected error during validation")

blog_task = Task(
    description="Write a blog post about AI",
    expected_output="A blog post under 200 words",
    agent=blog_agent,
    guardrail=validate_blog_content  # Add the guardrail function
)
```

### LLM-Based Guardrails (String Descriptions)

Instead of writing custom validation functions, you can use string descriptions that leverage LLM-based validation. When you provide a string to the `guardrail` or `guardrails` parameter, CrewAI automatically creates an `LLMGuardrail` that uses the agent's LLM to validate the output based on your description.

Requirements:
- The task must have an `agent` assigned (the guardrail uses the agent's LLM)
- Provide a clear, descriptive string explaining the validation criteria

```python
from crewai import Task

# Single LLM-based guardrail
blog_task = Task(
    description="Write a blog post about AI",
    expected_output="A blog post under 200 words",
    agent=blog_agent,
    guardrail="The blog post must be under 200 words and contain no technical jargon"
)
```

LLM-based guardrails are particularly useful for:
- Complex validation logic that's difficult to express programmatically
- Subjective criteria like tone, style, or quality assessments
- Natural language requirements that are easier to describe than code

The LLM guardrail will:
1. Analyze the task output against your description
2. Return `(True, output)` if the output complies with the criteria
3. Return `(False, feedback)` with specific feedback if validation fails

Example with detailed validation criteria:

```python
research_task = Task(
    description="Research the latest developments in quantum computing",
    expected_output="A comprehensive research report",
    agent=researcher_agent,
    guardrail="""
    The research report must:
    - Be at least 1000 words long
    - Include at least 5 credible sources
    - Cover both technical and practical applications
    - Be written in a professional, academic tone
    - Avoid speculation or unverified claims
    """
)
```

### Multiple Guardrails

You can apply multiple guardrails to a task using the `guardrails` parameter. Multiple guardrails are executed sequentially, with each guardrail receiving the output from the previous one. This allows you to chain validation and transformation steps.

The `guardrails` parameter accepts:
- A list of guardrail functions or string descriptions
- A single guardrail function or string (same as `guardrail`)

> **Note**: If `guardrails` is provided, it takes precedence over `guardrail`. The `guardrail` parameter will be ignored when `guardrails` is set.

```python
from typing import Tuple, Any
from crewai import TaskOutput, Task

def validate_word_count(result: TaskOutput) -> Tuple[bool, Any]:
    """Validate word count is within limits."""
    word_count = len(result.raw.split())
    if word_count < 100:
        return (False, f"Content too short: {word_count} words. Need at least 100 words.")
    if word_count > 500:
        return (False, f"Content too long: {word_count} words. Maximum is 500 words.")
    return (True, result.raw)

def validate_no_profanity(result: TaskOutput) -> Tuple[bool, Any]:
    """Check for inappropriate language."""
    profanity_words = ["badword1", "badword2"]  # Example list
    content_lower = result.raw.lower()
    for word in profanity_words:
        if word in content_lower:
            return (False, f"Inappropriate language detected: {word}")
    return (True, result.raw)

def format_output(result: TaskOutput) -> Tuple[bool, Any]:
    """Format and clean the output."""
    formatted = result.raw.strip()
    # Capitalize first letter
    formatted = formatted[0].upper() + formatted[1:] if formatted else formatted
    return (True, formatted)

# Apply multiple guardrails sequentially
blog_task = Task(
    description="Write a blog post about AI",
    expected_output="A well-formatted blog post between 100-500 words",
    agent=blog_agent,
    guardrails=[
        validate_word_count,      # First: validate length
        validate_no_profanity,    # Second: check content
        format_output             # Third: format the result
    ],
    guardrail_max_retries=3
)
```

In this example, the guardrails execute in order:
1. `validate_word_count` checks the word count
2. `validate_no_profanity` checks for inappropriate language (using the output from step 1)
3. `format_output` formats the final result (using the output from step 2)

If any guardrail fails, the error is sent back to the agent, and the task is retried up to `guardrail_max_retries` times.

### Mixing Function-Based and LLM-Based Guardrails

You can combine both function-based and string-based guardrails in the same list:

```python
from typing import Any, Dict, List, Tuple, Union
from crewai import TaskOutput, Task

def validate_word_count(result: TaskOutput) -> Tuple[bool, Any]:
    """Validate word count is within limits."""
    word_count = len(result.raw.split())
    if word_count < 100:
        return (False, f"Content too short: {word_count} words. Need at least 100 words.")
    if word_count > 500:
        return (False, f"Content too long: {word_count} words. Maximum is 500 words.")
    return (True, result.raw)

# Mix function-based and LLM-based guardrails
blog_task = Task(
    description="Write a blog post about AI",
    expected_output="A well-formatted blog post between 100-500 words",
    agent=blog_agent,
    guardrails=[
        validate_word_count,  # Function-based: precise word count check
        "The content must be engaging and suitable for a general audience",  # LLM-based: subjective quality check
        "The writing style should be clear, concise, and free of technical jargon"  # LLM-based: style validation
    ],
    guardrail_max_retries=3
)
```

This approach combines the precision of programmatic validation with the flexibility of LLM-based assessment for subjective criteria.

### Guardrail Function Requirements

1. **Function Signature**:
   - Must accept exactly one parameter (the task output)
   - Should return a tuple of `(bool, Any)`
   - Type hints are recommended but optional

2. **Return Values**:
   - On success: returns a tuple of `(bool, Any)`. For example: `(True, validated_result)`
   - On Failure: returns a tuple of `(bool, str)`. For example: `(False, "Error message explaining the failure")`

### Error Handling Best Practices

1. **Structured Error Responses**:

```python
from crewai import TaskOutput, LLMGuardrail

def validate_with_context(result: TaskOutput) -> Tuple[bool, Any]:
    try:
        # Main validation logic
        validated_data = perform_validation(result)
        return (True, validated_data)
    except ValidationError as e:
        return (False, f"VALIDATION_ERROR: {str(e)}")
    except Exception as e:
        return (False, str(e))
```

2. **Error Categories**:
   - Use specific error codes
   - Include relevant context
   - Provide actionable feedback

3. **Validation Chain**:

```python
from typing import Any, Dict, List, Tuple, Union
from crewai import TaskOutput

def complex_validation(result: TaskOutput) -> Tuple[bool, Any]:
    """Chain multiple validation steps."""
    try:
        # Step 1: Basic validation
        if not result:
            return (False, "Empty result")

        # Step 2: Content validation
        try:
            validated = validate_content(result)
            if not validated:
                return (False, "Invalid content")

            # Step 3: Format validation
            formatted = format_output(validated)
            return (True, formatted)
        except Exception as e:
            return (False, str(e))
    except Exception as e:
        return (False, str(e))
```

### Handling Guardrail Results

When a guardrail returns `(False, error)`:
1. The error is sent back to the agent
2. The agent attempts to fix the issue
3. The process repeats until:
   - The guardrail returns `(True, result)`
   - Maximum retries are reached (`guardrail_max_retries`)

Example with retry handling:

```python
from typing import Optional, Tuple, Union
from crewai import TaskOutput, Task

def validate_json_output(result: TaskOutput) -> Tuple[bool, Any]:
    """Validate and parse JSON output."""
    try:
        # Try to parse as JSON
        data = json.loads(result)
        return (True, data)
    except json.JSONDecodeError as e:
        return (False, "Invalid JSON format")

task = Task(
    description="Generate a JSON report",
    expected_output="A valid JSON object",
    agent=analyst,
    guardrail=validate_json_output,
    guardrail_max_retries=3  # Limit retry attempts
)
```

## Getting Structured Consistent Outputs from Tasks

> **Note**: It's also important to note that the output of the final task of a crew becomes the final output of the actual crew itself.

### Using `output_pydantic`

The `output_pydantic` property allows you to define a Pydantic model that the task output should conform to. This ensures that the output is not only structured but also validated according to the Pydantic model.

Here's an example demonstrating how to use output_pydantic:

```python
import json

from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    content: str


blog_agent = Agent(
    role="Blog Content Generator Agent",
    goal="Generate a blog title and content",
    backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
    verbose=False,
    allow_delegation=False,
    llm="gpt-4o",
)

task1 = Task(
    description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
    expected_output="A compelling blog title and well-written content.",
    agent=blog_agent,
    output_pydantic=Blog,
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[blog_agent],
    tasks=[task1],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff()

# Option 1: Accessing Properties Using Dictionary-Style Indexing
print("Accessing Properties - Option 1")
title = result["title"]
content = result["content"]
print("Title:", title)
print("Content:", content)

# Option 2: Accessing Properties Directly from the Pydantic Model
print("Accessing Properties - Option 2")
title = result.pydantic.title
content = result.pydantic.content
print("Title:", title)
print("Content:", content)

# Option 3: Accessing Properties Using the to_dict() Method
print("Accessing Properties - Option 3")
output_dict = result.to_dict()
title = output_dict["title"]
content = output_dict["content"]
print("Title:", title)
print("Content:", content)

# Option 4: Printing the Entire Blog Object
print("Accessing Properties - Option 5")
print("Blog:", result)
```

In this example:
- A Pydantic model `Blog` is defined with `title` and `content` fields.
- The task `task1` uses the `output_pydantic` property to specify that its output should conform to the `Blog` model.
- After executing the crew, you can access the structured output in multiple ways as shown.

#### Explanation of Accessing the Output

1. **Dictionary-Style Indexing**: You can directly access the fields using `result["field_name"]`. This works because the CrewOutput class implements the `__getitem__` method.
2. **Directly from Pydantic Model**: Access the attributes directly from the `result.pydantic` object.
3. **Using to_dict() Method**: Convert the output to a dictionary and access the fields.
4. **Printing the Entire Object**: Simply print the result object to see the structured output.

### Using `output_json`

The `output_json` property allows you to define the expected output in JSON format. This ensures that the task's output is a valid JSON structure that can be easily parsed and used in your application.

Here's an example demonstrating how to use `output_json`:

```python
import json

from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel


# Define the Pydantic model for the blog
class Blog(BaseModel):
    title: str
    content: str


# Define the agent
blog_agent = Agent(
    role="Blog Content Generator Agent",
    goal="Generate a blog title and content",
    backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
    verbose=False,
    allow_delegation=False,
    llm="gpt-4o",
)

# Define the task with output_json set to the Blog model
task1 = Task(
    description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
    expected_output="A JSON object with 'title' and 'content' fields.",
    agent=blog_agent,
    output_json=Blog,
)

# Instantiate the crew with a sequential process
crew = Crew(
    agents=[blog_agent],
    tasks=[task1],
    verbose=True,
    process=Process.sequential,
)

# Kickoff the crew to execute the task
result = crew.kickoff()

# Option 1: Accessing Properties Using Dictionary-Style Indexing
print("Accessing Properties - Option 1")
title = result["title"]
content = result["content"]
print("Title:", title)
print("Content:", content)

# Option 2: Printing the Entire Blog Object
print("Accessing Properties - Option 2")
print("Blog:", result)
```

In this example:
- A Pydantic model `Blog` is defined with `title` and `content` fields, which is used to specify the structure of the JSON output.
- The task `task1` uses the `output_json` property to indicate that it expects a JSON output conforming to the `Blog` model.
- After executing the crew, you can access the structured JSON output in two ways as shown.

#### Explanation of Accessing the Output

1. **Accessing Properties Using Dictionary-Style Indexing**: You can access the fields directly using `result["field_name"]`. This is possible because the CrewOutput class implements the `__getitem__` method, allowing you to treat the output like a dictionary. In this option, we're retrieving the title and content from the result.
2. **Printing the Entire Blog Object**: By printing `result`, you get the string representation of the CrewOutput object. Since the `str` method is implemented to return the JSON output, this will display the entire output as a formatted string representing the Blog object.

By using `output_pydantic` or `output_json`, you ensure that your tasks produce outputs in a consistent and structured format, making it easier to process and utilize the data within your application or across multiple tasks.

## Integrating Tools with Tasks

Leverage tools from the CrewAI Toolkit and LangChain Tools for enhanced task performance and agent interaction.

## Creating a Task with Tools

```python
import os
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key

from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

research_agent = Agent(
  role='Researcher',
  goal='Find and summarize the latest AI news',
  backstory="You're a researcher at a large company.
  You're responsible for analyzing data and providing insights
  to the business.""",
  verbose=True
)

# to perform a semantic search for a specified query from a text's content across the internet
search_tool = SerperDevTool()

task = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool]
)

crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print(result)
```

This demonstrates how tasks with specific tools can override an agent's default set for tailored task execution.

## Referring to Other Tasks

In CrewAI, the output of one task is automatically relayed into the next one, but you can specifically define what tasks' output, including multiple, should be used as context for another task. This is useful when you have a task that depends on the output of another task that is not performed immediately after it. This is done through the `context` attribute of the task:

```python
# ...

research_ai_task = Task(
    description="Research the latest developments in AI",
    expected_output="A list of recent AI developments",
    async_execution=True,
    agent=research_agent,
    tools=[search_tool]
)

research_ops_task = Task(
    description="Research the latest developments in AI Ops",
    expected_output="A list of recent AI Ops developments",
    async_execution=True,
    agent=research_agent,
    tools=[search_tool]
)

write_blog_task = Task(
    description="Write a full blog post about the importance of AI and its latest news",
    expected_output="Full blog post that is 4 paragraphs long",
    agent=writer_agent,
    context=[research_ai_task, research_ops_task]
)

#...
```

## Asynchronous Execution

You can define a task to be executed asynchronously. This means that the crew will not wait for it to be completed to continue with the next task. This is useful for tasks that take a long time to be completed, or that are not crucial for the next tasks to be performed.

You can then use the `context` attribute to define in a future task that it should wait for the output of the asynchronous task to be completed.

```python
#...

list_ideas = Task(
    description="List of 5 interesting ideas to explore for an article about AI.",
    expected_output="Bullet point list of 5 ideas for an article.",
    agent=researcher,
    async_execution=True # Will be executed asynchronously
)

list_important_history = Task(
    description="Research the history of AI and give me the 5 most important events.",
    expected_output="Bullet point list of 5 important events.",
    agent=researcher,
    async_execution=True # Will be executed asynchronously
)

write_article = Task(
    description="Write an article about AI, its history, and interesting ideas.",
    expected_output="A 4 paragraph article about AI.",
    agent=writer,
    context=[list_ideas, list_important_history] # Will wait for the output of the two tasks to be completed
)

#...
```

## Callback Mechanism

The callback function is executed after the task is completed, allowing for actions or notifications to be triggered based on the task's outcome.

```python
# ...

def callback_function(output: TaskOutput):
    # Do something after the task is completed
    # Example: Send an email to the manager
    print(f"""
        Task completed!
        Task: {output.description}
        Output: {output.raw}
    """)

research_task = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    agent=research_agent,
    tools=[search_tool],
    callback=callback_function
)

#...
```

## Accessing a Specific Task Output

Once a crew finishes running, you can access the output of a specific task by using the `output` attribute of the task object:

```python
# ...
task1 = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    agent=research_agent,
    tools=[search_tool]
)

#...

crew = Crew(
    agents=[research_agent],
    tasks=[task1, task2, task3],
    verbose=True
)

result = crew.kickoff()

# Returns a TaskOutput object with the description and results of the task
print(f"""
    Task completed!
    Task: {task1.output.description}
    Output: {task1.output.raw}
""")
```

## Tool Override Mechanism

Specifying tools in a task allows for dynamic adaptation of agent capabilities, emphasizing CrewAI's flexibility.

## Error Handling and Validation Mechanisms

While creating and executing tasks, certain validation mechanisms are in place to ensure the robustness and reliability of task attributes. These include but are not limited to:

- Ensuring only one output type is set per task to maintain clear output expectations.
- Preventing the manual assignment of the `id` attribute to uphold the integrity of the unique identifier system.

These validations help in maintaining the consistency and reliability of task executions within the crewAI framework.

## Creating Directories when Saving Files

The `create_directory` parameter controls whether CrewAI should automatically create directories when saving task outputs to files. This feature is particularly useful for organizing outputs and ensuring that file paths are correctly structured, especially when working with complex project hierarchies.

### Default Behavior

By default, `create_directory=True`, which means CrewAI will automatically create any missing directories in the output file path:

```python
# Default behavior - directories are created automatically
report_task = Task(
    description='Generate a comprehensive market analysis report',
    expected_output='A detailed market analysis with charts and insights',
    agent=analyst_agent,
    output_file='reports/2025/market_analysis.md',  # Creates 'reports/2025/' if it doesn't exist
    markdown=True
)
```

### Disabling Directory Creation

If you want to prevent automatic directory creation and ensure that the directory already exists, set `create_directory=False`:

```python
# Strict mode - directory must already exist
strict_output_task = Task(
    description='Save critical data that requires existing infrastructure',
    expected_output='Data saved to pre-configured location',
    agent=data_agent,
    output_file='secure/vault/critical_data.json',
    create_directory=False  # Will raise RuntimeError if 'secure/vault/' doesn't exist
)
```

### YAML Configuration

You can also configure this behavior in your YAML task definitions:

**tasks.yaml**
```yaml
analysis_task:
  description: >
    Generate quarterly financial analysis
  expected_output: >
    A comprehensive financial report with quarterly insights
  agent: financial_analyst
  output_file: reports/quarterly/q4_2024_analysis.pdf
  create_directory: true  # Automatically create 'reports/quarterly/' directory

audit_task:
  description: >
    Perform compliance audit and save to existing audit directory
  expected_output: >
    A compliance audit report
  agent: auditor
  output_file: audit/compliance_report.md
  create_directory: false  # Directory must already exist
```

### Use Cases

**Automatic Directory Creation (`create_directory=True`)**:
- Development and prototyping environments
- Dynamic report generation with date-based folders
- Automated workflows where directory structure may vary
- Multi-tenant applications with user-specific folders

**Manual Directory Management (`create_directory=False`)**:
- Production environments with strict file system controls
- Security-sensitive applications where directories must be pre-configured
- Systems with specific permission requirements
- Compliance environments where directory creation is audited

### Error Handling

When `create_directory=False` and the directory doesn't exist, CrewAI will raise a `RuntimeError`:

```python
try:
    result = crew.kickoff()
except RuntimeError as e:
    # Handle missing directory error
    print(f"Directory creation failed: {e}")
    # Create directory manually or use fallback location
```

## Conclusion

Tasks are the driving force behind the actions of agents in CrewAI. By properly defining tasks and their outcomes, you set the stage for your AI agents to work effectively, either independently or as a collaborative unit. Equipping tasks with appropriate tools, understanding the execution process, and following robust validation practices are crucial for maximizing CrewAI's potential, ensuring agents are effectively prepared for their assignments and that tasks are executed as intended.
```

## Task Configuration

### Using YAML Configuration

Tasks can be defined in YAML files for better organization:

**tasks.yaml**
```yaml
market_research:
  description: "Research current market trends in AI technology"
  expected_output: "A comprehensive report on AI market trends with key statistics and insights"
  agent: research_analyst

data_analysis:
  description: "Analyze collected market data and identify patterns"
  expected_output: "Statistical analysis with charts and key findings"
  agent: data_analyst
  context:
    - market_research

final_report:
  description: "Compile all findings into a final executive report"
  expected_output: "Executive summary, detailed findings, and strategic recommendations"
  agent: report_writer
  context:
    - market_research
    - data_analysis
  output_file: "ai_market_report.md"
```

### Using CrewAI Project Structure

With the project structure, tasks are defined as methods:

```python
from crewai import Task
from crewai.project import CrewBase, task

@CrewBase
class MarketAnalysisCrew:
    """Market Analysis Crew"""

    @task
    def market_research(self) -> Task:
        return Task(
            config=self.tasks_config['market_research']
        )

    @task
    def data_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['data_analysis'],
            context=[self.market_research()]
        )

    @task
    def final_report(self) -> Task:
        return Task(
            config=self.tasks_config['final_report'],
            context=[self.market_research(), self.data_analysis()],
            output_file="output/market_report.md"
        )
```

## Task Parameters

### Core Parameters

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `description` | str | What the task entails | Yes |
| `expected_output` | str | What the result should look like | Yes |
| `agent` | Agent | Which agent performs the task | Yes |
| `context` | List[Task] | Tasks this task depends on | No |

### Advanced Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `async_execution` | bool | Run task asynchronously | False |
| `output_file` | str | File to save output to | None |
| `output_json` | Any | JSON schema for structured output | None |
| `output_pydantic` | BaseModel | Pydantic model for output validation | None |
| `callback` | Callable | Function to call after completion | None |
| `human_input` | bool | Require human approval | False |

## Task Dependencies and Context

Tasks can depend on other tasks, creating a workflow where results flow between tasks.

### Sequential Dependencies

```python
research_task = Task(
    description="Research AI market trends",
    expected_output="Market research data",
    agent=researcher
)

analysis_task = Task(
    description="Analyze research data",
    expected_output="Analysis report",
    agent=analyst,
    context=[research_task]  # Depends on research_task output
)

report_task = Task(
    description="Create final report",
    expected_output="Complete report",
    agent=writer,
    context=[research_task, analysis_task]  # Depends on both tasks
)
```

### Parallel Execution

Tasks without dependencies can run in parallel:

```python
web_research = Task(
    description="Research web sources",
    expected_output="Web research findings",
    agent=web_researcher,
    async_execution=True
)

academic_research = Task(
    description="Research academic papers",
    expected_output="Academic research findings",
    agent=academic_researcher,
    async_execution=True
)

synthesis_task = Task(
    description="Synthesize all research",
    expected_output="Comprehensive synthesis",
    agent=synthesizer,
    context=[web_research, academic_research]  # Waits for both to complete
)
```

## Output Handling

### File Output

Save task results directly to files:

```python
report_task = Task(
    description="Generate monthly sales report",
    expected_output="Complete sales report in PDF format",
    agent=report_generator,
    output_file="monthly_sales_report.pdf"
)
```

### JSON Output

Structure output as JSON:

```python
analysis_task = Task(
    description="Analyze customer feedback",
    expected_output="Structured analysis with sentiment scores and key themes",
    agent=analyst,
    output_json={
        "sentiment_score": "float",
        "key_themes": ["string"],
        "recommendations": ["string"]
    }
)
```

### Pydantic Output

Use Pydantic models for type validation:

```python
from pydantic import BaseModel

class AnalysisResult(BaseModel):
    sentiment_score: float
    key_themes: List[str]
    recommendations: List[str]

analysis_task = Task(
    description="Analyze customer feedback",
    expected_output="Structured analysis results",
    agent=analyst,
    output_pydantic=AnalysisResult
)
```

## Callbacks and Human Input

### Task Callbacks

Execute functions after task completion:

```python
def send_notification(result):
    print(f"Task completed! Result: {result}")

notification_task = Task(
    description="Send completion notification",
    expected_output="Notification sent successfully",
    agent=notifier,
    callback=send_notification
)
```

### Human Input Tasks

Require human approval for sensitive tasks:

```python
approval_task = Task(
    description="Review and approve budget changes",
    expected_output="Approved budget changes",
    agent=approver,
    human_input=True  # Requires human confirmation
)
```

## Task Execution Patterns

### Research and Analysis Pattern

```python
research_task = Task(
    description="Conduct comprehensive research on {topic}",
    expected_output="Detailed research findings with sources and key insights",
    agent=researcher
)

analysis_task = Task(
    description="Analyze research findings and extract key patterns",
    expected_output="Analysis report with trends, patterns, and recommendations",
    agent=analyst,
    context=[research_task]
)

summary_task = Task(
    description="Create executive summary of analysis",
    expected_output="Concise executive summary highlighting key findings",
    agent=writer,
    context=[analysis_task],
    output_file="executive_summary.md"
)
```

### Content Creation Pattern

```python
planning_task = Task(
    description="Create content plan for {topic}",
    expected_output="Detailed content outline with structure and key points",
    agent=planner
)

writing_task = Task(
    description="Write the main content based on the plan",
    expected_output="Complete article draft",
    agent=writer,
    context=[planning_task]
)

editing_task = Task(
    description="Edit and polish the content",
    expected_output="Final edited version ready for publication",
    agent=editor,
    context=[writing_task],
    output_file="final_article.md"
)
```

### Data Processing Pattern

```python
data_collection_task = Task(
    description="Collect data from multiple sources",
    expected_output="Consolidated dataset ready for analysis",
    agent=data_collector
)

data_cleaning_task = Task(
    description="Clean and preprocess the data",
    expected_output="Clean, validated dataset",
    agent=data_engineer,
    context=[data_collection_task]
)

modeling_task = Task(
    description="Build and train predictive models",
    expected_output="Trained models with performance metrics",
    agent=data_scientist,
    context=[data_cleaning_task]
)

deployment_task = Task(
    description="Deploy models to production",
    expected_output="Deployed models with API endpoints",
    agent=ml_engineer,
    context=[modeling_task]
)
```

## Best Practices

### 1. Clear Descriptions

Write specific, actionable task descriptions:

```python
# Good
task = Task(
    description="Analyze quarterly sales data for Q1 2024 and identify top-performing products and regions",
    expected_output="Sales analysis report with charts showing product performance by region and recommendations for Q2 strategy",
    agent=sales_analyst
)

# Avoid
task = Task(
    description="Do analysis",
    expected_output="Some report",
    agent=analyst
)
```

### 2. Appropriate Context Dependencies

Only include necessary context to avoid information overload:

```python
# Good - focused context
summary_task = Task(
    description="Create executive summary",
    expected_output="Concise summary of key findings",
    agent=writer,
    context=[analysis_task]  # Only needs analysis results
)

# Avoid - too much context
summary_task = Task(
    description="Create executive summary",
    expected_output="Concise summary of key findings",
    agent=writer,
    context=[research_task, data_collection_task, cleaning_task, analysis_task]  # Overwhelming
)
```

### 3. Structured Output Expectations

Define clear, measurable output expectations:

```python
# Good
task = Task(
    description="Conduct customer satisfaction survey analysis",
    expected_output="Report containing: 1) Overall satisfaction score (0-100), 2) Top 5 satisfaction drivers, 3) Bottom 5 pain points, 4) Demographic breakdown of responses, 5) Recommended improvement actions",
    agent=analyst
)

# Avoid
task = Task(
    description="Analyze survey results",
    expected_output="Analysis of the survey",
    agent=analyst
)
```

### 4. Resource-Aware Task Design

Consider computational resources and time constraints:

```python
# For time-sensitive tasks
urgent_task = Task(
    description="Generate emergency response plan",
    expected_output="Action plan within 30 minutes",
    agent=emergency_coordinator,
    max_execution_time=1800  # 30 minutes
)

# For resource-intensive tasks
heavy_computation_task = Task(
    description="Process large dataset analysis",
    expected_output="Analysis results with visualizations",
    agent=data_scientist,
    async_execution=True  # Run in background
)
```

## Error Handling and Retries

Tasks can be configured to handle failures gracefully:

```python
robust_task = Task(
    description="Process payment transactions",
    expected_output="Transaction processing results",
    agent=payment_processor,
    max_retries=3,
    retry_delay=60  # Wait 60 seconds between retries
)
```

## Monitoring and Logging

Enable detailed logging for task execution:

```python
monitored_task = Task(
    description="Execute complex data transformation",
    expected_output="Transformed dataset",
    agent=data_engineer,
    verbose=True,
    log_file="task_execution.log"
)
```

## Common Patterns and Anti-Patterns

### ✅ Good Patterns

1. **Single Responsibility**: Each task has one clear purpose
2. **Clear Dependencies**: Explicit context relationships
3. **Structured Output**: Well-defined expected results
4. **Resource Awareness**: Appropriate timeouts and resource limits

### ❌ Anti-Patterns to Avoid

1. **God Tasks**: Tasks that try to do too many things
2. **Unclear Dependencies**: Missing or incorrect context
3. **Vague Expectations**: Ambiguous output requirements
4. **Resource Ignorance**: No consideration of time/memory constraints

## Integration with Crews

Tasks work within crews to create collaborative workflows:

```python
from crewai import Crew, Process

crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, report_task],
    process=Process.sequential  # Tasks execute in order
)
```

## Next Steps

- Learn about [Crews](https://docs.crewai.com/en/concepts/crews) to understand multi-agent collaboration
- Explore [Processes](https://docs.crewai.com/en/concepts/processes) for different execution patterns
- Check out [Flows](https://docs.crewai.com/en/concepts/flows) for complex workflow orchestration
- Read about [Tools](https://docs.crewai.com/en/concepts/tools) to extend agent capabilities