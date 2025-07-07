# YourNews App - Aplicação de busca de notícias
# Este aplicativo usa o framework Streamlit para criar uma interface web simples
# que permite aos usuários buscar notícias sobre um assunto específico.

# Streamlit é um framework Python que permite criar aplicações web interativas
# com código Python puro, sem necessidade de conhecer HTML, CSS ou JavaScript.
# Saiba mais em: https://streamlit.io/

# Importação das bibliotecas necessárias
import os  # Biblioteca padrão para interagir com o sistema operacional
import streamlit as st  # Framework Streamlit para criar a interface web
from dotenv import load_dotenv  # Biblioteca para carregar variáveis de ambiente de um arquivo .env

# Importamos a função search_news do nosso módulo personalizado
# Esta função será responsável por buscar as notícias na internet
from utils.searchnews import search_news

# Carregamos as variáveis de ambiente do arquivo .env
# Isso é útil para armazenar informações sensíveis como chaves de API
load_dotenv()

# Acessamos a variável de ambiente APP_NAME
# Se ela não existir, usamos "YourNews App" como valor padrão
app_name = os.getenv("APP_NAME", "YourNews App")

# Configuramos a página da aplicação Streamlit
# Esta deve ser a primeira função Streamlit a ser chamada no script
st.set_page_config(
    page_title=app_name,  # Título que aparecerá na aba do navegador
    page_icon="📰",     # Ícone que aparecerá na aba do navegador (emoji de jornal)
    layout="wide"       # Layout amplo para melhor utilização do espaço da tela
)

# Ocultamos elementos padrão do Streamlit usando CSS personalizado
# Isso inclui o menu principal, o rodapé e o botão de Deploy
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}  /* Oculta o menu principal */
footer {visibility: hidden;}     /* Oculta o rodapé */
.stDeployButton {display:none;}  /* Oculta o botão de Deploy */
</style>
"""
# Aplicamos o CSS personalizado usando markdown com HTML
# O parâmetro unsafe_allow_html=True permite usar tags HTML no markdown
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Adicionamos o título principal da aplicação
st.title("Your News")

# Criamos um layout de duas colunas para organizar a interface
# A proporção [1, 2] significa que a coluna da direita será duas vezes mais larga que a da esquerda
left_col, right_col = st.columns([1, 2])

# Começamos a definir o conteúdo da coluna da esquerda
with left_col:
    # Criamos um campo de entrada de texto para o usuário digitar o assunto da busca
    # O valor digitado será armazenado na variável 'subject'
    # Limitamos o campo a 20 caracteres
    subject = st.text_input("Enter a subject to search for news about:", max_chars=20)
    
    # Adicionamos um botão para iniciar a busca
    # Quando clicado, search_button será True, caso contrário será False
    search_button = st.button("Search for News")
    
    # Usamos o session_state do Streamlit para armazenar os resultados da busca
    # O session_state permite manter dados entre as execuções do script
    # (O Streamlit reexecuta todo o script a cada interação do usuário)
    if "news_results" not in st.session_state:
        st.session_state.news_results = ""  # Inicializa com uma string vazia se não existir
    
    # Verificamos se o botão foi clicado E se há um assunto digitado
    if search_button and subject:
        # Mostramos um indicador de carregamento (spinner) enquanto a busca é realizada
        with st.spinner(f"Searching for news about {subject}..."):
            # Chamamos a função search_news e armazenamos o resultado no session_state
            st.session_state.news_results = search_news(subject)

# Agora definimos o conteúdo da coluna da direita
with right_col:
    # Verificamos se já temos resultados de busca armazenados
    if not st.session_state.news_results:
        # Se não há resultados, mostramos instruções para o usuário
        # A função st.info cria uma caixa de informação com fundo azul
        st.info("### Instructions\n\nEnter a subject in the text box on the left and click 'Search for News' to see the latest news about your topic.\n\nThe results will appear here.")
        
        # Criamos um container vazio para futuros resultados
        # Um container é uma área onde podemos adicionar elementos Streamlit
        st.container()
        
        # Adicionamos texto formatado usando markdown
        # O Streamlit suporta a sintaxe markdown para formatação de texto
        st.markdown("### Results will appear here")
        st.markdown("---")  # Linha horizontal
        st.markdown("*Waiting for your search query...*")  # Texto em itálico
    else:
        # Se há resultados, exibimos o conteúdo formatado como markdown
        # Os resultados já estão formatados como markdown pela função search_news
        st.markdown(st.session_state.news_results)

# Adicionamos um rodapé à página, fora das colunas
# Isso aparecerá na parte inferior da página
st.markdown("---")  # Linha horizontal para separar o conteúdo do rodapé
st.markdown(" 2025 YourNews App | Created with Streamlit")  # Texto de copyright
