import os
import sys
from dotenv import load_dotenv

load_dotenv()

from crewai import Agent, Task, Crew, Process, LLM
from crewai.mcp import MCPServerStdio

# TARGET: Published NPM Package
# This verifies that a user can run 'npx @crew-ai/crewright' and it works.
# NOTE: v1.0.0 uses OLD tool names (type_text, click_element).
print(f"Targeting Published NPM Package: @crew-ai/crewright")

bridge_server = MCPServerStdio(
   command="npx",
   # We use -y to avoid "Need to install the following packages" prompt
   args=["-y", "@crew-ai/crewright"],
   env=os.environ
)

# Configure LLM
model_name = os.getenv("MODEL_NAME", "gpt-4o")
my_llm = LLM(
    model=model_name,
    base_url=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY")
)

agent = Agent(
    role="Release Tester",
    goal="Verify the published NPM package works",
    backstory="You are a simplified tester checking the V1 release.",
    mcps=[bridge_server],
    verbose=True,
    llm=my_llm
)

# Task uses OLD tool names because v1 on NPM doesn't have the new renames yet
verify_task = Task(
    description="""
    1. Navigate to 'https://example.com'.
    2. Read the page content using `get_page_content`.
    3. Report the first 100 characters.
    """,
    expected_output="Content of example.com",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[verify_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("Starting Release V1 Verification...")
    try:
        crew.kickoff()
        print("SUCCESS: V1 Release Validated")
    except Exception as e:
        print(f"FAILURE: {e}")
