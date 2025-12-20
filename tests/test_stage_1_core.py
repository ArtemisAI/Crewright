import os
import sys
import signal

# Windows Signal Patch
if os.name == 'nt':
    for sig in ['SIGHUP', 'SIGTSTP', 'SIGQUIT', 'SIGALRM', 'SIGUSR1', 'SIGUSR2', 'SIGPIPE', 'SIGBUS', 'SIGCHLD', 'SIGCONT', 'SIGIO', 'SIGIOT', 'SIGKILL', 'SIGPROF', 'SIGPWR', 'SIGSTOP', 'SIGSYS', 'SIGTRAP', 'SIGURG', 'SIGVTALRM', 'SIGWINCH', 'SIGXCPU', 'SIGXFSZ']:
        if not hasattr(signal, sig):
            setattr(signal, sig, 1)

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, Process

def run_test():
    print("Stage 1: Core Agent Verification (No Tools)")
    
    # Define a simple agent
    agent = Agent(
        role='Math Genius',
        goal='Solve simple math problems',
        backstory='You are a calculator.',
        verbose=True,
        allow_delegation=False,
        tools=[] # Explicitly no tools
    )

    # Define a simple task
    task = Task(
        description='What is 2 + 2? Return ONLY the number.',
        expected_output='The number 4',
        agent=agent
    )

    # Define the crew
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential
    )

    # Run
    result = crew.kickoff()
    print(f"\nResult: {result}")

    if "4" in str(result):
        print("\nSUCCESS: Stage 1 Passed")
    else:
        print("\nFAILURE: Stage 1 Failed - Unexpected output")
        sys.exit(1)

if __name__ == "__main__":
    run_test()
