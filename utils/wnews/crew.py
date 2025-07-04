from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from pydantic import BaseModel
import yaml
import os


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Wnews():
    """Wnews crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    def __init__(self):
        # Set the configuration paths
        self._agents_config_path = 'config/agents.yaml'
        self._tasks_config_path = 'config/tasks.yaml'
        # Get the absolute paths for the configuration files
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self._full_agents_config_path = os.path.join(current_dir, self._agents_config_path)
        self._full_tasks_config_path = os.path.join(current_dir, self._tasks_config_path)
    
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # Create tools
    # search_tool = SerperDevTool()

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def news_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['news_researcher'],
            tools=[SerperDevTool(),ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def news_curator_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['news_curator_analyst'],
            verbose=True
        )

    @agent
    def newsletter_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['newsletter_editor'],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def news_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_research_task'],
            output_file='news_research.txt'
        )

    @task
    def news_curator_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_curator_analyst_task'],
            output_file='news_analysis.txt',
            context=[self.news_research_task()]
        )

    @task
    def review_and_edit_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_edit_task'],
            output_file='r2talk_newsletter.md',
            context=[self.news_curator_analyst_task()]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Wnews crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
