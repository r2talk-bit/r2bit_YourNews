# YourNews - Sistema de busca e curadoria de notícias usando CrewAI
#
# Este arquivo implementa uma equipe (crew) de agentes de IA usando o framework CrewAI.
# CrewAI é um framework para criar aplicações multi-agentes, onde vários agentes de IA
# trabalham juntos para realizar tarefas complexas, cada um com seu papel específico.
# Saiba mais em: https://www.crewai.io/

# Importações do framework CrewAI
from crewai import Agent, Crew, Process, Task  # Classes principais do CrewAI
from crewai.project import CrewBase, agent, crew, task  # Decoradores para facilitar a criação de projetos
from crewai_tools import ScrapeWebsiteTool, SerperDevTool  # Ferramentas que os agentes podem usar
from pydantic import BaseModel  # Para validação de dados
import yaml  # Para ler arquivos de configuração YAML
import os  # Para manipulação de caminhos de arquivos


# O decorador @CrewBase indica que esta classe define uma equipe de agentes
# Ele adiciona funcionalidades especiais à classe, como gerenciamento automático de agentes e tarefas
@CrewBase
class Wnews():
    """Classe que define a equipe de agentes para busca e curadoria de notícias"""
    
    # Você pode usar os decoradores @before_kickoff e @after_kickoff para executar código
    # antes ou depois da equipe começar a trabalhar
    # https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

    # No CrewAI, usamos arquivos YAML para configurar os agentes e tarefas de forma mais organizada
    # Isso separa a configuração do código, facilitando a manutenção e modificação
    # Saiba mais sobre arquivos de configuração YAML aqui:
    # Agentes: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tarefas: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    def __init__(self):
        # Definimos os caminhos para os arquivos de configuração
        self._agents_config_path = 'config/agents.yaml'  # Caminho para o arquivo de configuração dos agentes
        self._tasks_config_path = 'config/tasks.yaml'    # Caminho para o arquivo de configuração das tarefas
        
        # Obtemos os caminhos absolutos para os arquivos de configuração
        # Isso é importante para garantir que os arquivos sejam encontrados independentemente 
        # de onde o script é executado
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório atual do arquivo
        self._full_agents_config_path = os.path.join(current_dir, self._agents_config_path)
        self._full_tasks_config_path = os.path.join(current_dir, self._tasks_config_path)
    
    
    # Caminhos para os arquivos de configuração que serão usados pelos métodos abaixo
    agents_config = "config/agents.yaml"  # Configurações dos agentes (personalidade, objetivos, etc.)
    tasks_config = "config/tasks.yaml"    # Configurações das tarefas (descrições, instruções, etc.)

    # ===== FERRAMENTAS DOS AGENTES =====
    # As ferramentas são recursos que os agentes podem usar para realizar suas tarefas
    # Por exemplo, ferramentas de busca na web, raspagem de sites, etc.
    
    # Exemplos de ferramentas disponíveis:
    # - SerperDevTool(): permite que o agente faça buscas na web usando a API Serper
    # - ScrapeWebsiteTool(): permite que o agente extraia informações de páginas web
    
    # Para saber mais sobre como adicionar ferramentas aos seus agentes:
    # https://docs.crewai.com/concepts/agents#agent-tools
    
    # ===== DEFINIÇÃO DOS AGENTES =====
    # Cada método decorado com @agent define um agente diferente na nossa equipe
    # O decorador @agent registra automaticamente o agente na equipe
    
    @agent  # Este decorador registra o agente na equipe automaticamente
    def news_researcher(self) -> Agent:
        """Agente pesquisador de notícias
        
        Este agente é responsável por buscar notícias relevantes na internet.
        Ele usa ferramentas de busca na web e raspagem de sites para encontrar informações.
        """
        return Agent(
            # Carrega a configuração do agente do arquivo YAML (personalidade, objetivos, etc.)
            config=self.agents_config['news_researcher'],
            # Fornece ferramentas para o agente usar
            tools=[SerperDevTool(),ScrapeWebsiteTool()],
            # Quando verbose=True, mostra detalhes do pensamento do agente durante a execução
            verbose=True
        )

    @agent
    def news_curator_analyst(self) -> Agent:
        """Agente curador e analista de notícias
        
        Este agente analisa as notícias encontradas pelo pesquisador,
        identifica tendências e seleciona as informações mais relevantes.
        """
        return Agent(
            config=self.agents_config['news_curator_analyst'],
            # Este agente não recebe ferramentas específicas, pois trabalha com os dados já coletados
            verbose=True
        )

    @agent
    def newsletter_editor(self) -> Agent:
        """Agente editor de newsletter
        
        Este agente formata as informações analisadas em um formato de newsletter,
        garantindo que o conteúdo seja claro, conciso e bem estruturado.
        """
        return Agent(
            config=self.agents_config['newsletter_editor'],
            verbose=True
        )

    # ===== DEFINIÇÃO DAS TAREFAS =====
    # As tarefas são as atividades que os agentes precisam realizar
    # Cada tarefa é atribuída a um agente específico e pode depender de outras tarefas
    
    # Para saber mais sobre saídas estruturadas de tarefas,
    # dependências entre tarefas e callbacks, consulte a documentação:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    @task  # Este decorador registra a tarefa na equipe automaticamente
    def news_research_task(self) -> Task:
        """Tarefa de pesquisa de notícias
        
        Esta é a primeira tarefa da sequência, onde o agente pesquisador
        busca notícias relevantes sobre um determinado assunto.
        """
        return Task(
            # Carrega a configuração da tarefa do arquivo YAML (descrição, instruções, etc.)
            config=self.tasks_config['news_research_task'],
            # Define um arquivo onde o resultado da tarefa será salvo
            output_file='news_research.txt'
        )

    @task
    def news_curator_analyst_task(self) -> Task:
        """Tarefa de curadoria e análise de notícias
        
        Esta tarefa depende da tarefa de pesquisa e usa seus resultados
        para analisar e selecionar as informações mais relevantes.
        """
        return Task(
            config=self.tasks_config['news_curator_analyst_task'],
            output_file='news_analysis.txt',
            # O parâmetro context define as dependências desta tarefa
            # Aqui, esta tarefa depende da tarefa de pesquisa e recebe seus resultados
            context=[self.news_research_task()]
        )

    @task
    def review_and_edit_task(self) -> Task:
        """Tarefa de revisão e edição
        
        Esta é a última tarefa da sequência, onde o editor formata
        o conteúdo em um formato de newsletter final.
        """
        return Task(
            config=self.tasks_config['review_and_edit_task'],
            output_file='r2talk_newsletter.md',  # Arquivo final da newsletter em formato Markdown
            # Esta tarefa depende da tarefa de curadoria e análise
            context=[self.news_curator_analyst_task()]
        )

    # ===== CRIAÇÃO DA EQUIPE =====
    # O método decorado com @crew define a equipe completa,
    # combinando os agentes e tarefas definidos acima
    
    @crew  # Este decorador registra a equipe automaticamente
    def crew(self) -> Crew:
        """Cria a equipe de agentes para busca e curadoria de notícias
        
        Esta equipe é composta por três agentes (pesquisador, curador/analista e editor)
        que trabalham sequencialmente para criar uma newsletter sobre um assunto.
        """
        # Para saber como adicionar fontes de conhecimento à sua equipe, consulte:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            # Lista de agentes da equipe (criada automaticamente pelo decorador @agent)
            agents=self.agents, 
            # Lista de tarefas da equipe (criada automaticamente pelo decorador @task)
            tasks=self.tasks, 
            # Define o processo como sequencial: as tarefas são executadas em ordem
            process=Process.sequential,
            # Quando verbose=True, mostra detalhes da execução da equipe
            verbose=True,
            # Alternativa: process=Process.hierarchical - para um processo hierárquico
            # Saiba mais em: https://docs.crewai.com/how-to/Hierarchical/
        )
