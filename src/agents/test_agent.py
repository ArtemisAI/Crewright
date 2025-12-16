
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Ensure we can import from src if needed, though CrewAI handles imports usually.
# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from crewai import Agent, Task, Crew, Process, LLM
from crewai.mcp import MCPServerStdio

# Helper to locate the bridge server script
BRIDGE_SERVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../bridge/dist/index.js"))
print(f"Targeting Bridge Server at: {BRIDGE_SERVER_PATH}")

print("Targeting Custom Bridge via Node.js Stdio")

bridge_server = MCPServerStdio(
   command="node",
   args=[BRIDGE_SERVER_PATH],
   env=os.environ
)

# Configure LLM from Env
my_llm = LLM(
    model=os.getenv("MODEL_NAME"),
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)

# Define the Navigator Agent
navigator = Agent(
    role="Stealth Navigator",
    goal="Navigate the web using the stealth bridge to verify connectivity",
    backstory="You are a QA agent testing a new browser integration. You must click, type, and read.",
    mcps=[bridge_server],
    verbose=True,
    allow_delegation=False,
    llm=my_llm
)

# Define the Test Task
verify_task = Task(
    description="""
    1. Navigate to 'https://example.com'.
    2. Read the page content to confirm you are there.
    3. If successfully read, report the H1 title of the page.
    4. Then, try to Navigate to 'https://google.com'.
    5. Report success if you can do both.
    """,
    expected_output="A confirmation report of the navigation and page title.",
    agent=navigator
)

crew = Crew(
    agents=[navigator],
    tasks=[verify_task],
    process=Process.sequential,
    verbose=True,
    planning=True,
    planning_llm=my_llm
)

if __name__ == "__main__":
    print("Starting CrewAI Stealth Bridge Verification...")
    print("ENSURE YOUR CHROME EXTENSION IS CONNECTED!")
    try:
        result = crew.kickoff()
        print("\n\n########################")
        print("## VERIFICATION RESULT ##")
        print("########################\n")
        print(result)
    except Exception as e:
        print(f"Error running crew: {e}")
