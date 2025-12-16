import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from crewai import Agent, Task, Crew, Process, LLM
from crewai.mcp import MCPServerStdio

# 1. Verify Package Version
PKG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/bridge/package.json"))
with open(PKG_PATH, "r") as f:
    pkg = json.load(f)
    print(f"📦 Verifying Build: {pkg['name']} @ {pkg['version']}")
    if pkg['version'] != "1.0.1":
        print("❌ Version mismatch! Expected 1.0.1")
        sys.exit(1)

# 2. Setup Agent with BUILT Artifact
BRIDGE_SERVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/bridge/dist/index.js"))
print(f"🔧 Using Bridge Artifact: {BRIDGE_SERVER_PATH}")

bridge_server = MCPServerStdio(
   command="node",
   args=[BRIDGE_SERVER_PATH],
   env=os.environ
)

my_llm = LLM(
    model=os.environ["MODEL_NAME"],
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)

agent = Agent(
    role="Release Verifier",
    goal="Verify v1.0.1 build artifact",
    backstory="You are a meticulous release engineer.",
    mcps=[bridge_server],
    verbose=True,
    llm=my_llm
)

verify_task = Task(
    description="""
    1. Navigate to 'https://www.google.com'.
    2. Get page content.
    3. Report if the title contains 'Google'.
    """,
    expected_output="Confirmation that title contains Google",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[verify_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Starting Build Verification...")
    try:
        crew.kickoff()
        print("✅ Build Verified Successfully")
    except Exception as e:
        print(f"❌ Build Verification Failed: {e}")
