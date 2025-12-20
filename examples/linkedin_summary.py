import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai.mcp import MCPServerStdio

# ==============================================================================
# 🚀 Crewright Example: LinkedIn Feed Summarizer
# ==============================================================================
# This example demonstrates how to use Crewright's "Parasitic Bridge" to access
# an authenticated LinkedIn session (running in your local Chrome) and summarize
# the latest updates.
#
# PREREQUISITES:
# 1. Chrome must be running with the Crewright Extension installed.
# 2. You must be logged into LinkedIn in that Chrome window.
# 3. Environment variables (OPENAI_API_KEY, MODEL_NAME) must be set.
# ==============================================================================

# 1. Setup the Bridge Connection
# We use 'npx' to run the bridge server. If you have it installed globally or locally,
# this connects your Agent to your Browser.
bridge_server = MCPServerStdio(
    command="npx",
    args=["-y", "@crew-ai/crewright"],
    env=os.environ
)

# 2. Configure LLM
my_llm = LLM(
    model=os.environ.get("MODEL_NAME", "gpt-4o"),
    base_url=os.environ.get("OPENAI_API_BASE"), # Optional: For local LLMs
    api_key=os.environ.get("OPENAI_API_KEY")
)

# 3. Define the Agent
# The 'Browser Analyst' uses the tools provided by the bridge (navigate, click, fill, etc.)
browser_agent = Agent(
    role="Browser Analyst",
    goal="Analyze social media feeds",
    backstory="You are an expert at digesting information from web feeds.",
    mcps=[bridge_server],
    verbose=True,
    llm=my_llm
)

# 4. Define the Task
# Note how we don't need login steps - we assume the user is already authenticated!
summary_task = Task(
    description="""
    1. Navigate to 'https://www.linkedin.com/feed/'.
    2. Wait a moment for the feed to load (use `evaluate` with a 3-5s sleep if needed, 
       or just rely on the page load event).
    3. Get the page content.
    4. Extract the top 3 post topics or updates you see in the feed.
    5. summarize them nicely.
    """,
    expected_output="A summary of the top 3 LinkedIn feed updates.",
    agent=browser_agent
)

# 5. Run the Crew
crew = Crew(
    agents=[browser_agent],
    tasks=[summary_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("starting LinkedIn Summary...")
    result = crew.kickoff()
    print("\n\n########################")
    print("##  SUMMARY RESULTS   ##")
    print("########################\n")
    print(result)
