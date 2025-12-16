import os
import sys
# Add the project root to python path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools.browser_use_tool.browser_use_tool import BrowserUseTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class ResearchCrew():
    """ResearchCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[BrowserUseTool()],
            verbose=True,
            allow_delegation=False,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks,   # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            output_log_file=os.getenv('CREWAI_LOG_FILE', 'logs/research_crew.log')
        )
