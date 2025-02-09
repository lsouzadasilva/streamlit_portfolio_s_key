import streamlit as st
from paginas.sobre import pagina_inicial
from paginas.projetosbi import bi
from paginas.streamlit import streamlit
from paginas.chatbot import chatbot
from paginas.chatbot_huggingface import chatbot_huggingface
import streamlit_option_menu 
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title='Home',
    page_icon= '⚡',
    layout='wide'
)



st.sidebar.title("Navegação")
st.sidebar.divider()

        
    # https://icons.getbootstrap.com/ - > icon
with st.sidebar:
    paginas = option_menu(
    menu_title = "Menu",
    options = ["Sobre", "Projetos em Power BI", "Projetos em Streamlit & Plotly", "Projetos OpenAI", "Projetos huggingface"],
    icons = ["envelope-at-fill", "bar-chart-fill", "graph-up-arrow", "robot", "emoji-wink-fill"],
    menu_icon ="cast",
    default_index = 0
    # orientation = "horizontal"  < - Agora
)

st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Leandro Souza](https://br.linkedin.com/in/leandro-souza-313136190)")


if paginas == "Sobre":
    pagina_inicial()
elif paginas == "Projetos em Power BI":
    bi()
elif paginas == "Projetos em Streamlit & Plotly":
    streamlit()
elif paginas == "Projetos OpenAI":
    chatbot()
elif paginas == "Projetos huggingface":
    chatbot_huggingface()
