"""
YourNews - Módulo de Busca de Notícias

Este módulo contém funções para buscar notícias sobre um assunto específico
utilizando o framework CrewAI, que permite criar equipes de agentes de IA
para realizar tarefas complexas de forma colaborativa.

O módulo se integra com a classe Wnews definida em utils.wnews.crew,
que implementa uma equipe de agentes especializados em busca e curadoria de notícias.
"""

# Importações de bibliotecas padrão do Python
import os          # Para acessar variáveis de ambiente e manipular arquivos
import tempfile    # Para criar arquivos temporários
import dotenv     # Para carregar variáveis de ambiente de um arquivo .env

# Carrega as variáveis de ambiente do arquivo .env
# Isso é importante para não expor chaves de API diretamente no código
dotenv.load_dotenv()

# Importa a classe Wnews do módulo crew
# Esta classe implementa a equipe de agentes usando o framework CrewAI
from utils.wnews.crew import Wnews

def search_news(subject):
    """
    Busca notícias sobre um assunto específico usando o framework CrewAI.
    
    Esta função é o ponto de entrada principal para o sistema de busca de notícias.
    Ela verifica se as chaves de API necessárias estão disponíveis e, em seguida,
    utiliza a equipe de agentes definida na classe Wnews para buscar, analisar
    e formatar notícias sobre o assunto solicitado.
    
    Args:
        subject (str): O assunto sobre o qual buscar notícias
        
    Returns:
        str: String formatada em Markdown contendo as notícias encontradas
    """
    # Verifica se o usuário forneceu um assunto para busca
    if not subject:
        return "Please enter a subject to search for news."
    
    # Verifica se as chaves de API necessárias estão configuradas nas variáveis de ambiente
    # SerperDev é usado para buscas na web e OpenAI para processamento de linguagem natural
    serper_api_key = os.environ.get('SERPER_API_KEY')  # Chave para a API de busca SerperDev
    openai_api_key = os.environ.get('OPENAI_API_KEY')   # Chave para a API da OpenAI (GPT)
    
    # Registra o status das chaves de API e gerencia casos de chaves ausentes
    missing_keys = []  # Lista para armazenar nomes de chaves ausentes
    
    # Verifica se ambas as chaves estão disponíveis
    if serper_api_key and openai_api_key:
        print("Info: Both SERPER_API_KEY and OPENAI_API_KEY are set.")
    else:
        # Adiciona à lista as chaves que estão faltando
        if not serper_api_key:
            missing_keys.append('SERPER_API_KEY')
        if not openai_api_key:
            missing_keys.append('OPENAI_API_KEY')
            
        # Informa quais chaves estão faltando
        print(f"Info: Missing API keys: {', '.join(missing_keys)}")
        
        # Se alguma chave estiver faltando, usa uma função de demonstração
        # que retorna dados simulados em vez de fazer buscas reais
        return _mock_search_news(subject, missing_keys)
    
    # Se todas as chaves estiverem disponíveis, usa a implementação do CrewAI
    try:
        # Cria um arquivo temporário para armazenar a saída
        # Isso é útil para casos em que o resultado é muito grande
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.md') as temp_file:
            output_path = temp_file.name
            
        # Executa a equipe de agentes do CrewAI
        # 1. Cria uma instância da classe Wnews (a equipe de agentes)
        # 2. Acessa o objeto crew (a equipe configurada)
        # 3. Inicia o processo com kickoff() passando o tópico como entrada
        result = Wnews().crew().kickoff(inputs={'topic': subject})
        
        # Retorna o resultado formatado em Markdown
        return result
    except Exception as e:
        # Em caso de erro, retorna uma mensagem informativa
        return f"CrewAI error: {str(e)}"


def _mock_search_news(subject, missing_keys):
    """
    Gera resultados simulados de busca de notícias quando as chaves de API estão ausentes.
    
    Esta função é usada como um fallback quando as chaves de API necessárias não estão
    disponíveis, permitindo que o aplicativo ainda demonstre sua funcionalidade
    sem depender de serviços externos.
    
    Args:
        subject (str): O assunto sobre o qual buscar notícias
        missing_keys (list): Lista de nomes das chaves de API que estão faltando
        
    Returns:
        str: String formatada em Markdown simulando resultados de notícias
    """
    # Cria uma mensagem informativa sobre as chaves ausentes
    missing_keys_info = f"**Nota:** Esta é uma demonstração com dados simulados. Chaves de API ausentes: {', '.join(missing_keys)}\n\n"
    
    # Simula resultados de notícias com base no assunto fornecido
    mock_results = f"""
# Notícias sobre {subject}

{missing_keys_info}
## Principais Manchetes

### {subject} está em alta nos trending topics

Um estudo recente mostrou que {subject} tem sido um dos assuntos mais discutidos nas redes sociais nas últimas 24 horas. Especialistas apontam que o interesse crescente pode estar relacionado a eventos recentes.

### Novos desenvolvimentos em {subject}

Pesquisadores anunciaram hoje avanços significativos em {subject}, o que pode mudar a forma como entendemos este campo. "Estamos apenas começando a explorar as possibilidades", afirmou um dos cientistas envolvidos.

### Análise: O impacto de {subject} na sociedade moderna

Especialistas debatem como {subject} está moldando nossa sociedade e quais são as implicações para o futuro. Muitos acreditam que estamos testemunhando apenas o começo de uma transformação significativa.

## Conclusão

{subject} continua sendo um tópico de grande interesse e relevância. Fique atento para mais atualizações sobre este assunto em breve.

---
*Esta newsletter foi gerada automaticamente pelo YourNews App*
"""
    
    return mock_results
