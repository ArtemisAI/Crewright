import os
import sys
import time
from dotenv import load_dotenv

load_dotenv()

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from crewai import Agent, Task, Crew, Process, LLM
from crewai.mcp import MCPServerStdio

# Helper to locate the bridge server script
BRIDGE_SERVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../bridge/dist/index.js"))
print(f"Targeting Bridge Server at: {BRIDGE_SERVER_PATH}")

bridge_server = MCPServerStdio(
   command="node",
   args=[BRIDGE_SERVER_PATH],
   env=os.environ
)

# Configure LLM from Env
# Default to gpt-4o, but allow overrides for benchmarking
model_name = os.getenv("MODEL_NAME", "gpt-4o")
print(f"Using Model: {model_name}")

my_llm = LLM(
    model=model_name,
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)

# Custom Tee Logger for Robust Logging
class TeeLogger(object):
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()
        
    def fileno(self):
        return self.terminal.fileno()

# Define the Robust Agent
navigator = Agent(
    role="Robust Tester",
    goal="Verify browser tools with explicit stability checks",
    backstory="You are a QA engineer. You perform actions and ALWAYS verify they worked before moving on.",
    mcps=[bridge_server],
    verbose=True,
    allow_delegation=False,
    llm=my_llm
)

# Define the Robust Task
verify_task = Task(
    description="""
    1. **Navigate** to 'https://www.google.com'.
    2. **Wait** using `evaluate` with 'new Promise(r => setTimeout(r, 2000))'.
    3. **Fill** the search bar. Identify the selector (e.g., 'textarea[name="q"]') and use the `fill` tool with value 'CrewAI'.
    4. **Press** 'Enter' using the `press` tool.
    5. **Wait** for results. Use `evaluate` to sleep for 3 seconds (ensuring page load).
    6. **Screenshot** the results.
    7. **Report** the first 20 characters of the screenshot base64 string to confirm capture.
    """,
    expected_output="Confirmation of all actions (Navigate -> Wait -> Fill -> Press -> Wait -> Screenshot).",
    agent=navigator
)

crew = Crew(
    agents=[navigator],
    tasks=[verify_task],
    process=Process.sequential,
    verbose=True,
    planning=True, # Enable planning to handle the complex sequence better
    planning_llm=my_llm
)

if __name__ == "__main__":
    # Setup Logs
    log_dir = os.path.join(os.path.dirname(__file__), "../../logs")
    os.makedirs(log_dir, exist_ok=True)
    
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"robust_run_{timestamp}.log")
    
    # Redirect stdout and stderr
    sys.stdout = TeeLogger(log_file)
    sys.stderr = TeeLogger(log_file)

    print(f"Starting Robust Verification Run...")
    print(f"Logs: {log_file}")
    
    try:
        result = crew.kickoff()
        print("\n\n########################")
        print("## ROBUST VERIFICATION RESULT ##")
        print("########################\n")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
