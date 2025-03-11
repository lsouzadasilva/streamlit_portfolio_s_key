import streamlit as st
from paginas.sobre import pagina_inicial
from paginas.projetosbi import bi
from paginas.streamlit import streamlit
from paginas.chatbot import chatbot
from paginas.chatbot_huggingface import chatbot_huggingface
from paginas.certificados import certificados_skills
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title='Home',
    page_icon= '⚡',
    layout='wide'
)

# --- Ocult menus ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



st.sidebar.title("Navegação")
st.sidebar.divider()

        
    # https://icons.getbootstrap.com/ - > icon
with st.sidebar:
    paginas = option_menu(
    menu_title = "Menu",
    options = ["Sobre mim", "Projetos em Power BI", "Projetos em Streamlit & Plotly", "Projetos OpenAI", "Projetos huggingface", "Certificados & Skills"],
    icons = ["envelope-at-fill", "bar-chart-fill", "graph-up-arrow", "robot", "emoji-wink-fill", "award"],
    menu_icon ="cast",
    default_index = 0
    # orientation = "horizontal"  < - Agora
)

st.sidebar.divider()
st.sidebar.markdown("Desenvolvido por [Leandro Souza](https://br.linkedin.com/in/leandro-souza-313136190)")


if paginas == "Sobre mim":
    pagina_inicial()
elif paginas == "Projetos em Power BI":
    bi()
elif paginas == "Projetos em Streamlit & Plotly":
    streamlit()
elif paginas == "Projetos OpenAI":
    chatbot()
elif paginas == "Projetos huggingface":
    chatbot_huggingface()
elif paginas == "Certificados & Skills":
    certificados_skills()
