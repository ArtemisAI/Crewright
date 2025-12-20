import os
import sys
# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import signal
from typing import Any

# Windows Signal Patch
if os.name == 'nt':
    for sig in ['SIGHUP', 'SIGTSTP', 'SIGQUIT', 'SIGALRM', 'SIGUSR1', 'SIGUSR2', 'SIGPIPE', 'SIGBUS', 'SIGCHLD', 'SIGCONT', 'SIGIO', 'SIGIOT', 'SIGKILL', 'SIGPROF', 'SIGPWR', 'SIGSTOP', 'SIGSYS', 'SIGTRAP', 'SIGURG', 'SIGVTALRM', 'SIGWINCH', 'SIGXCPU', 'SIGXFSZ']:
        if not hasattr(signal, sig):
            setattr(signal, sig, 1)

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool

class CalculatorTool(BaseTool):
    name: str = "Calculator"
    description: str = "A tool that multiplies two numbers."

    def _run(self, expression: str) -> str:
        # Expecting expression like "5 * 5"
        try:
            print(f"[TOOL] Calculator called with: {expression}")
            result = eval(expression, {"__builtins__": None}, {})
            return str(result)
        except Exception as e:
            return f"Error: {e}"

def run_test():
    print("Stage 2: Basic Tool Verification")
    
    agent = Agent(
        role='Math Genius',
        goal='Solve math with tools',
        backstory='You use a calculator for everything.',
        verbose=True,
        tools=[CalculatorTool()]
    )

    task = Task(
        description='Calculate 12 * 12 using your tool. Return ONLY the number.',
        expected_output='The number 144',
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    result = crew.kickoff()
    print(f"\nResult: {result}")

    if "144" in str(result):
        print("\nSUCCESS: Stage 2 Passed")
    else:
        print("\nFAILURE: Stage 2 Failed")
        sys.exit(1)

if __name__ == "__main__":
    run_test()
