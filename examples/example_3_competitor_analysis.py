import signal
import sys
import os

# Mock signals for Windows compatibility
if os.name == 'nt':
    for sig in ['SIGHUP', 'SIGTSTP', 'SIGQUIT', 'SIGALRM', 'SIGUSR1', 'SIGUSR2', 'SIGPIPE', 'SIGBUS', 'SIGCHLD', 'SIGCONT', 'SIGIO', 'SIGIOT', 'SIGKILL', 'SIGPROF', 'SIGPWR', 'SIGSTOP', 'SIGSYS', 'SIGTRAP', 'SIGURG', 'SIGVTALRM', 'SIGWINCH', 'SIGXCPU', 'SIGXFSZ']:
        if not hasattr(signal, sig):
            setattr(signal, sig, 1)

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.research_crew.crew import ResearchCrew

def run():
    inputs = {
        'topic': 'Compare the feature set of iPhone 15 vs Samsung Galaxy S24. List key differences.'
    }
    
    try:
        print(f"Starting research on: {inputs['topic']}")
        ResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"Error running crew: {e}")

if __name__ == "__main__":
    run()
