import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.research_crew.crew import ResearchCrew

def run():
    inputs = {
        'topic': 'General Research' # Not strictly needed as the task is static, but good practice
    }
    
    try:
        ResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"Error running crew: {e}")

if __name__ == "__main__":
    run()
