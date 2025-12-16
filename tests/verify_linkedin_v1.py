import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from crewai import Agent, Task, Crew, Process, LLM
from crewai.mcp import MCPServerStdio

# 1. Setup Agent with BUILT Artifact (v1.0.1)
BRIDGE_SERVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/bridge/dist/index.js"))
print(f"🔧 Using Bridge Artifact: {BRIDGE_SERVER_PATH}")

bridge_server = MCPServerStdio(
   command="node",
   args=[BRIDGE_SERVER_PATH],
   env=os.environ
)

# Configure LLM (Strict Env Var)
model_name = os.getenv("MODEL_NAME")
if not model_name:
    raise ValueError("MODEL_NAME environment variable is required")

my_llm = LLM(
    model=model_name,
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)

agent = Agent(
    role="Identity Verifier",
    goal="Confirm LinkedIn Login Status",
    backstory="You are verifying that the browser bridge successfully reuses the user's existing login session.",
    mcps=[bridge_server],
    verbose=True,
    llm=my_llm
)

verify_task = Task(
    description="""
    1. Navigate to 'https://www.linkedin.com/feed/'.
    2. Wait for 5 seconds using `evaluate` ("new Promise(r => setTimeout(r, 5000))") to ensure feed loads.
    3. Get page content.
    4. ANALYZE the content to find the logged-in user's name (look for "Welcome," user profile headings, or identity hints).
    5. REPORT the User Name found, or explicitly state "Not Logged In" if feed is missing.
    """,
    expected_output="Logged in User Name: [Name] OR 'Not Logged In'",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[verify_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Starting LinkedIn Verification...")
    try:
        crew.kickoff()
    except Exception as e:
        print(f"❌ Verification Failed: {e}")
