import os
import sys
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from crewai import Agent, Task, Crew, Process, LLM
from crewai.mcp import MCPServerStdio

# Use LOCAL Bridge for this test (Current Dev Branch)
BRIDGE_SERVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/bridge/dist/index.js"))
bridge_server = MCPServerStdio(
   command="node",
   args=[BRIDGE_SERVER_PATH],
   env=os.environ
)

my_llm = LLM(
    model=os.getenv("MODEL_NAME", "gpt-4o"),
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)

agent = Agent(
    role="Code Tester",
    goal="Verify evaluate tool works",
    backstory="You are a code verification agent.",
    mcps=[bridge_server],
    verbose=True,
    llm=my_llm
)

verify_task = Task(
    description="""
    1. Navigate to 'https://example.com'.
    2. Use `evaluate` to execute: "document.title".
    3. Use `evaluate` to execute: "1 + 1".
    4. Report the results.
    """,
    expected_output="Title is 'Example Domain', Math is 2",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[verify_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    try:
        crew.kickoff()
    except Exception as e:
        print(f"Error: {e}")
