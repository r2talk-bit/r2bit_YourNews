# YourNews Streamlit Application 📰

> **Para iniciantes em programação**: Este é um projeto que usa inteligência artificial para buscar e resumir notícias sobre qualquer assunto que você quiser!

YourNews é uma aplicação web construída com **Streamlit** (uma biblioteca Python para criar interfaces web de forma simples) e **CrewAI** (um framework para criar equipes de agentes de IA que trabalham juntos). A aplicação permite que você busque, analise e visualize notícias sobre qualquer assunto, tudo de forma automatizada.

## O que é o YourNews? 🤔

YourNews é uma aplicação amigável para iniciantes que usa inteligência artificial para:

1. **Buscar notícias** sobre qualquer assunto na internet
2. **Analisar o conteúdo** dessas notícias para encontrar as mais importantes
3. **Criar newsletters bem formatadas** com resumos e análises

É como ter uma equipe de jornalistas trabalhando para você, só que usando IA!

### Para quem é útil? 👤

- **Estudantes** aprendendo sobre eventos atuais
- **Profissionais** que precisam se manter atualizados sobre notícias do setor
- **Programadores iniciantes** que querem aprender como integrar IA em projetos
- **Qualquer pessoa** interessada em obter notícias resumidas sobre tópicos específicos

## Como Funciona o YourNews 🔍

O YourNews usa uma equipe de agentes de IA (chamada de "crew" no CrewAI) que trabalham juntos como uma verdadeira equipe de jornalismo:

### Nossa Equipe Virtual de Notícias 💻

1. **Pesquisador de Notícias** 🔎
   - **Função**: Busca na internet as notícias mais recentes sobre o seu assunto
   - **Como faz isso**: Usa ferramentas de busca na web (SerperDev) e extração de conteúdo de sites
   - **Resultado**: Uma lista de notícias relevantes com links e descrições

2. **Curador/Analista de Notícias** 📈
   - **Função**: Seleciona as notícias mais importantes e escreve análises detalhadas
   - **Como faz isso**: Lê o conteúdo coletado pelo Pesquisador e identifica as tendências e histórias mais relevantes
   - **Resultado**: Análises aprofundadas das notícias mais importantes

3. **Editor de Newsletter** 📝
   - **Função**: Formata tudo em uma newsletter profissional e fácil de ler
   - **Como faz isso**: Revisa e edita o conteúdo para garantir clareza, precisão e boa formatação
   - **Resultado**: Uma newsletter completa e bem estruturada

### Fluxo de Trabalho 📊

```
Você digita um assunto → Pesquisador busca notícias → Curador analisa → Editor formata → Você recebe a newsletter
```

> **Conceito-chave para iniciantes**: Este projeto demonstra como diferentes "agentes" de IA podem trabalhar juntos em uma sequência, cada um realizando uma tarefa específica e passando o resultado para o próximo.

## Estrutura do Projeto 📚

Para programadores iniciantes, entender a estrutura de um projeto é fundamental. Aqui está como nosso projeto está organizado:

```
/pasta-raiz-do-projeto
│
├── .streamlit/        # Arquivos de configuração do Streamlit
│   └── secrets.toml   # Chaves secretas e configurações (nunca compartilhe!)
│
├── assets/            # Imagens e outros recursos estáticos
│
├── example/           # Arquivos de exemplo e templates
│
├── utils/             # Funções auxiliares e módulos
│   └── wnews/         # Implementação da equipe de notícias
│       ├── config/    # Arquivos de configuração para agentes e tarefas
│       └── crew.py    # Implementação principal da equipe
│
├── .dockerignore      # Arquivos a serem excluídos das builds Docker
├── .env               # Variáveis de ambiente (chaves de API, configurações)
├── .env.example       # Exemplo de arquivo de variáveis de ambiente
├── .gitignore         # Arquivos a serem ignorados pelo git
├── Dockerfile         # Instruções para construir o container Docker
├── README.md          # Este arquivo de documentação
├── requirements.txt   # Dependências Python (bibliotecas necessárias)
└── streamlit_app.py   # Arquivo principal da aplicação
```

### Arquivos Principais para Iniciantes 🔍

Se você está começando, foque nestes arquivos:

1. **`streamlit_app.py`** - O arquivo principal que cria a interface web
2. **`utils/searchnews.py`** - Contém a função que busca notícias
3. **`utils/wnews/crew.py`** - Define a equipe de agentes de IA
4. **`utils/wnews/config/`** - Arquivos YAML que configuram os agentes e tarefas
5. **`.env`** - Onde você coloca suas chaves de API (nunca compartilhe este arquivo!)

## Configurando o Projeto 🔧

### Desenvolvimento Local (Passo a Passo para Iniciantes)

#### 1. Preparando seu Ambiente Python

Primeiro, precisamos criar um "ambiente virtual" - um espaço isolado para instalar as bibliotecas do projeto sem afetar o resto do seu computador.

```bash
# Crie um ambiente virtual chamado "venv"
python -m venv venv
```

> **O que isso faz?** 🤔 Cria uma pasta chamada "venv" que contém uma cópia isolada do Python e suas ferramentas.

#### 2. Ativando o Ambiente Virtual

Agora precisamos "ativar" esse ambiente para usá-lo:

**No Windows:**
```bash
venv\Scripts\activate
```

**No Mac ou Linux:**
```bash
source venv/bin/activate
```

> **Como saber se funcionou?** 🔍 Você verá `(venv)` no início da linha de comando.

#### 3. Instalando as Bibliotecas Necessárias

Agora vamos instalar todas as bibliotecas que o projeto precisa:

```bash
pip install -r requirements.txt
```

> **O que isso faz?** 📚 Lê a lista de bibliotecas no arquivo `requirements.txt` e instala todas elas no seu ambiente virtual.

#### 4. Configurando as Chaves de API

O projeto precisa de chaves de API para funcionar corretamente:

1. Copie o arquivo de exemplo para criar seu próprio arquivo de configuração:
   ```bash
   copy .env.example .env   # No Windows
   # OU
   cp .env.example .env     # No Mac/Linux
   ```

2. Abra o arquivo `.env` em um editor de texto e adicione suas chaves de API:
   ```
   SERPER_API_KEY=sua_chave_aqui
   OPENAI_API_KEY=sua_chave_aqui
   ```

> **Onde conseguir as chaves?** 🔑
> - Para a SERPER_API_KEY: Registre-se em [SerperDev](https://serper.dev)
> - Para a OPENAI_API_KEY: Registre-se em [OpenAI](https://platform.openai.com)

#### 5. Executando a Aplicação

Agora você pode iniciar a aplicação:

```bash
streamlit run streamlit_app.py
```

> **O que acontecerá?** 🌐 O Streamlit iniciará um servidor web local e abrirá automaticamente seu navegador com a aplicação YourNews.

### Usando Docker (Para Usuários Mais Avançados) 📦

Docker é uma tecnologia que permite empacotar a aplicação e todas as suas dependências em um "container" isolado. É como uma caixa que contém tudo o que a aplicação precisa para funcionar.

> **Nota para iniciantes:** Se você nunca usou Docker antes, recomendamos seguir o método de desenvolvimento local acima. Docker é uma ferramenta mais avançada.

#### 1. Construindo a Imagem Docker

```bash
# Isso cria uma "imagem" - um template para o container
docker build -t yournews-app .
```

> **O que isso faz?** 🏠 Lê as instruções no arquivo `Dockerfile` e cria uma imagem chamada "yournews-app".

#### 2. Executando o Container

```bash
# Isso inicia um container baseado na imagem que criamos
docker run -p 8501:8501 yournews-app
```

> **O que isso faz?** 🚀 Inicia a aplicação dentro de um container e conecta a porta 8501 do container à porta 8501 do seu computador.

#### 3. Acessando a Aplicação

Abra seu navegador e acesse:
```
http://localhost:8501
```

## Configuração do Projeto ⚙️

### Arquivos de Configuração Importantes

#### 1. Variáveis de Ambiente (`.env`)

Este arquivo contém configurações que podem mudar dependendo do ambiente onde a aplicação está sendo executada.

```
# Exemplo de arquivo .env
SERPER_API_KEY=sua_chave_aqui
OPENAI_API_KEY=sua_chave_aqui
```

> **Por que usar um arquivo .env?** 🔐 É uma prática de segurança! Mantém informações sensíveis (como chaves de API) fora do código-fonte e evita que sejam compartilhadas acidentalmente.

#### 2. Segredos do Streamlit (`.streamlit/secrets.toml`)

O Streamlit tem seu próprio sistema para gerenciar segredos, especialmente útil quando você implanta a aplicação na nuvem.

```toml
# Exemplo de arquivo secrets.toml
[api_keys]
serper = "sua_chave_aqui"
openai = "sua_chave_aqui"
```

### Chaves de API Necessárias

Para que a aplicação funcione corretamente, você precisa de duas chaves de API:

1. **`SERPER_API_KEY`**: 
   - **O que é?** Chave para a ferramenta de busca SerperDev, que permite buscar notícias na web
   - **Como obter?** Registre-se em [SerperDev](https://serper.dev) e obtenha uma chave gratuita ou paga

2. **`OPENAI_API_KEY`**: 
   - **O que é?** Chave para os serviços da OpenAI (como GPT-4) usados pelo CrewAI
   - **Como obter?** Registre-se em [OpenAI](https://platform.openai.com) e crie uma chave de API

> **Dica para iniciantes:** Ambas as plataformas oferecem opções gratuitas ou de teste que são suficientes para começar a usar o YourNews.

## Recursos da Aplicação ✨

### Integração com CrewAI 🤖

O YourNews usa o framework CrewAI para criar fluxos de trabalho inteligentes baseados em agentes para busca e análise de notícias:

![Diagrama do CrewAI](https://raw.githubusercontent.com/joaomdmoura/crewAI/main/docs/diagram.png)

- **Busca de Notícias**: Busca artigos de notícias sobre qualquer assunto usando a ferramenta SerperDev
- **Análise de Conteúdo**: Agentes de IA analisam e resumem o conteúdo das notícias
- **Geração de Newsletter**: Gera automaticamente newsletters bem formatadas com base nos resultados da busca

### Funções e Objetivos dos Agentes 👨‍💻

A aplicação usa uma equipe de agentes de IA especializados, cada um com funções específicas:

#### 1. Pesquisador de Notícias 🔎

```python
# Trecho de código que define o agente pesquisador
@agent
def news_researcher(self) -> Agent:
    return Agent(
        config=self.agents_config['news_researcher'],
        tools=[SerperDevTool(), ScrapeWebsiteTool()],  # Ferramentas que o agente pode usar
        verbose=True
    )
```

- **Objetivo**: Buscar na internet notícias detalhadas e relevantes sobre o seu tópico
- **O que ele faz**: Identifica as principais notícias, filtra por relevância e prioriza as mais importantes
- **Saída**: Coleta pelo menos 30 notícias significativas com links e comentários sobre sua relevância

#### 2. Curador/Analista de Notícias 📈

```python
# Trecho de código que define o agente curador
@agent
def news_curator_analyst(self) -> Agent:
    return Agent(
        config=self.agents_config['news_curator_analyst'],
        verbose=True
    )
```

- **Objetivo**: Transformar a pesquisa em análises significativas
- **O que ele faz**: Seleciona as 10 histórias mais impactantes e escreve análises detalhadas (300-400 palavras cada)
- **Saída**: Explicações claras sobre a importância e o impacto potencial de cada notícia

#### 3. Editor de Newsletter 📝

```python
# Trecho de código que define o agente editor
@agent
def newsletter_editor(self) -> Agent:
    return Agent(
        config=self.agents_config['newsletter_editor'],
        verbose=True
    )
```

- **Objetivo**: Criar uma newsletter polida e profissional
- **O que ele faz**: Revisa e edita todo o conteúdo para garantir precisão, clareza e gramática correta
- **Saída**: Uma newsletter bem estruturada com um título atraente, introdução, análises detalhadas e links para recursos adicionais

> **Conceito-chave para iniciantes**: Cada agente é como um "especialista" em uma tarefa específica. Juntos, eles formam uma equipe que pode realizar tarefas complexas que seriam difíceis para um único modelo de IA.

## Como Usar o YourNews (Guia para Iniciantes) 👍

### Usando a Interface Streamlit (Método Mais Fácil) 👌

![Exemplo de Interface Streamlit](https://raw.githubusercontent.com/streamlit/streamlit/master/examples/assets/screenshot.png)

1. **Inicie a aplicação** (siga as instruções de Configuração acima)
2. **Digite um termo de busca** na caixa de pesquisa (como "mudanças climáticas" ou "inteligência artificial")
3. **Clique no botão de busca** e aguarde os agentes de IA trabalharem
   - Você verá uma barra de progresso enquanto os agentes trabalham
   - Isso pode levar alguns minutos, dependendo do assunto
4. **Veja seus resultados** - uma newsletter completa será gerada para você!
   - Os resultados são formatados em Markdown para fácil leitura
   - Você pode copiar o conteúdo ou compartilhá-lo diretamente

### Usando o Código Python (Para Programadores em Aprendizado) 👨‍💻

Se você está aprendendo programação, pode usar o YourNews em seu código Python. Aqui está um exemplo simples:

```python
# Uso básico - apenas importe e chame a função de busca
from utils.searchnews import search_news

# Busque notícias sobre um assunto específico
resultados = search_news("inteligência artificial")

# Exiba os resultados
print(resultados)
```

> **O que este código faz?** 🤔
> 1. Importa a função `search_news` do módulo `utils.searchnews`
> 2. Chama essa função com o assunto "inteligência artificial"
> 3. Armazena os resultados na variável `resultados`
> 4. Exibe os resultados no console

### Uso Avançado (Conforme Você Aprende Mais) 💯

À medida que você se torna mais confortável com programação, pode personalizar como a equipe de agentes funciona:

```python
# Importa a classe Wnews do módulo crew
from utils.wnews.crew import Wnews

# Inicializa a equipe de agentes
equipe_noticias = Wnews()

# Executa a equipe com seu tópico
resultado = equipe_noticias.crew().kickoff(inputs={"topic": "inteligência artificial"})

# Exibe o resultado
print(resultado)
```

> **Explicação do código avançado:** 🔍
> - `Wnews()` cria uma instância da classe que define a equipe de agentes
> - `.crew()` configura a equipe com todos os agentes e tarefas
> - `.kickoff()` inicia o processo de busca com o tópico especificado
> - O parâmetro `inputs` é um dicionário que contém os dados de entrada para a equipe

### Entendendo o Processo Passo a Passo 📝

Quando você executa o YourNews, aqui está o que acontece nos bastidores:

1. O **Pesquisador de Notícias** busca pelo menos 30 notícias recentes sobre seu tópico
   - Ele usa a API SerperDev para buscar na web
   - Também pode extrair conteúdo de sites específicos

2. O **Curador/Analista de Notícias** seleciona as 10 histórias mais importantes e escreve análises detalhadas
   - Ele lê os resultados do Pesquisador
   - Identifica tendências e padrões nas notícias
   - Escreve análises aprofundadas sobre cada notícia importante

3. O **Editor de Newsletter** formata tudo em uma newsletter profissional
   - Ele revisa o conteúdo para garantir clareza e precisão
   - Adiciona títulos, introdução e conclusão
   - Formata o conteúdo em Markdown para fácil leitura

Tudo isso acontece automaticamente - você só precisa fornecer o tópico!

## Personalizando o YourNews (Conforme Você Aprende Mais) 🔧

À medida que você se torna mais confortável com programação, pode personalizar o YourNews de várias maneiras:

### 1. Modificando o Comportamento dos Agentes 👨‍💻

Edite os arquivos YAML em `utils/wnews/config/` para alterar como os agentes trabalham:

**Exemplo de `agents.yaml`:**
```yaml
news_researcher:
  role: "News Researcher"
  goal: "Buscar notícias detalhadas e relevantes sobre o tópico solicitado"
  backstory: "Você é um pesquisador experiente especializado em encontrar informações..."
```

**Exemplo de `tasks.yaml`:**
```yaml
news_research_task:
  description: "Buscar notícias detalhadas e relevantes sobre: {topic}"
  expected_output: "Uma lista de pelo menos 30 notícias relevantes..."
  agent: "news_researcher"
```

### 2. Adicionando Novas Ferramentas 🔧

Em `crew.py`, você pode adicionar mais ferramentas aos agentes:

```python
@agent
def news_researcher(self) -> Agent:
    return Agent(
        config=self.agents_config['news_researcher'],
        # Adicione novas ferramentas aqui
        tools=[SerperDevTool(), ScrapeWebsiteTool(), SuaNovaFerramenta()],
        verbose=True
    )
```

> **Dica para iniciantes:** As ferramentas são classes que implementam funcionalidades específicas que os agentes podem usar, como busca na web, extração de conteúdo, etc.

### 3. Criando Novos Agentes 👨‍🎓

1. Adicione definições de novos agentes ao arquivo `agents.yaml`
2. Crie métodos para eles em `crew.py`

```python
@agent
def seu_novo_agente(self) -> Agent:
    return Agent(
        config=self.agents_config['seu_novo_agente'],
        tools=[...],  # Ferramentas que o agente pode usar
        verbose=True
    )
```

### 4. Alterando o Fluxo de Trabalho 📈

Modifique as dependências de tarefas em `crew.py` para alterar como as informações fluem entre os agentes:

```python
@task
def sua_nova_tarefa(self) -> Task:
    return Task(
        config=self.tasks_config['sua_nova_tarefa'],
        output_file='resultado.txt',
        # Defina quais tarefas devem ser concluídas antes desta
        context=[self.news_research_task(), self.news_curator_analyst_task()]
    )
```

## Problemas Comuns para Iniciantes 🚫

### Erros de Chave de API 🔑

**Problema:** Mensagens de erro sobre chaves de API ausentes ou inválidas.

**Solução:** 
- Verifique se você criou o arquivo `.env` corretamente
- Confirme se as chaves de API estão corretas e não contêm espaços extras
- Exemplo correto: `SERPER_API_KEY=sua_chave_aqui` (sem espaços ao redor do sinal de igual)

### Erros de Importação 📦

**Problema:** Mensagens como "ModuleNotFoundError: No module named 'crewai'"

**Solução:**
- Verifique se você instalou todas as dependências com `pip install -r requirements.txt`
- Confirme se o ambiente virtual está ativado (deve aparecer `(venv)` no terminal)
- Se necessário, instale pacotes específicos: `pip install crewai crewai_tools`

### Sem Resultados 👎

**Problema:** A busca não retorna resultados ou retorna resultados vazios.

**Solução:**
- Verifique se seu termo de busca é específico o suficiente
- Confirme se sua conexão com a internet está funcionando
- Verifique os logs para ver se há erros nas chamadas de API

### Desempenho Lento ⏳

**Problema:** A aplicação demora muito para retornar resultados.

**Solução:**
- Os agentes de IA levam tempo para trabalhar - seja paciente!
- Buscas mais específicas geralmente são mais rápidas
- Considere ajustar os parâmetros de busca para limitar o número de resultados

## Licença 📜

MIT License - Você pode usar, modificar e distribuir este código livremente, desde que mantenha a atribuição original.
