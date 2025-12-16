import os
import sys
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
my_llm = LLM(
    model=os.getenv("MODEL_NAME"),
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)

# Define the Navigator Agent
navigator = Agent(
    role="Stealth Navigator",
    goal="Verify new browser tools (hover, key press, screenshot)",
    backstory="You are a QA agent. You must search google and capture the result visually.",
    mcps=[bridge_server],
    verbose=True,
    allow_delegation=False,
    llm=my_llm
)

# Define the Test Task
verify_task = Task(
    description="""
    1. Navigate to 'https://www.google.com'.
    2. Type 'CrewAI' into the search textarea (selector: 'textarea[name="q"]').
    3. Use 'press_key' with argument 'Enter' to submit the search.
    4. Wait a moment (or use evaluate_script to sleep).
    5. Take a 'screenshot'.
    6. Report success if you captured the screenshot (it returns base64).
    """,
    expected_output="Confirmation that screenshot was captured.",
    agent=navigator
)

crew = Crew(
    agents=[navigator],
    tasks=[verify_task],
    process=Process.sequential,
    verbose=True,
    planning=True,
    planning_llm=my_llm,
    output_log_file=os.path.join("logs", "latest_run.log") # Attempt to use built-in logging if available
)

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

if __name__ == "__main__":
    # Setup Logs
    log_dir = os.path.join(os.path.dirname(__file__), "../../logs")
    os.makedirs(log_dir, exist_ok=True)
    
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"verification_run_{timestamp}.log")
    
    # Redirect stdout and stderr
    sys.stdout = TeeLogger(log_file)
    sys.stderr = TeeLogger(log_file) # Capture errors too

    print(f"Starting Phase 2 Tool Verification...")
    print(f"Logs being saved to: {log_file}")
    
    try:
        result = crew.kickoff()
        print(result)
    except Exception as e:
        print(f"Error: {e}")
