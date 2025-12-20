import os
import sys
# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import signal

# Windows Signal Patch
if os.name == 'nt':
    for sig in ['SIGHUP', 'SIGTSTP', 'SIGQUIT', 'SIGALRM', 'SIGUSR1', 'SIGUSR2', 'SIGPIPE', 'SIGBUS', 'SIGCHLD', 'SIGCONT', 'SIGIO', 'SIGIOT', 'SIGKILL', 'SIGPROF', 'SIGPWR', 'SIGSTOP', 'SIGSYS', 'SIGTRAP', 'SIGURG', 'SIGVTALRM', 'SIGWINCH', 'SIGXCPU', 'SIGXFSZ']:
        if not hasattr(signal, sig):
            setattr(signal, sig, 1)

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, Process
from crewai_tools.browser_use_tool.browser_use_tool import BrowserUseTool

def run_test():
    print("Stage 4: Browser Tool Integration")
    
    tool = BrowserUseTool()
    
    agent = Agent(
        role='Researcher',
        goal='Use browser to find info',
        backstory='You are a web researcher.',
        verbose=True,
        tools=[tool]
    )

    # Simple task that requires browser
    # "Go to google.com" is the instruction passed to browser-use
    task = Task(
        description='1. Navigate to https://google.com \n2. Get the page title. \nReturn ONLY the page title.',
        expected_output='The title of the page',
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    print("Kickoff...")
    result = crew.kickoff()
    print(f"\nResult: {result}")

    if "Google" in str(result):
        print("\nSUCCESS: Stage 4 Passed")
    else:
        print("\nFAILURE: Stage 4 Failed")
        sys.exit(1)

if __name__ == "__main__":
    run_test()
