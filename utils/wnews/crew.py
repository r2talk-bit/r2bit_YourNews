from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
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
    agents_config_path = 'config/agents.yaml'
    tasks_config_path = 'config/tasks.yaml'
    
    # Load YAML configs with explicit UTF-8 encoding
    @property
    def agents_config(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, self.agents_config_path)
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    
    @property
    def tasks_config(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, self.tasks_config_path)
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)

    # Create tools
    search_tool = SerperDevTool()

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def ai_insights_curator(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_insights_curator'],
            tools=[self.search_tool],
            verbose=True
        )

    @agent
    def ai_content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_content_writer'],
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
    def curate_ai_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['curate_ai_insights_task'],
            output_file='insights.txt'
        )

    @task
    def write_impact_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_impact_analysis_task'],
            context=[self.curate_ai_insights_task()]
        )

    @task
    def review_and_edit_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_edit_task'],
            output_file='r2talk_newsletter.md',
            context=[self.write_impact_analysis_task()]
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
