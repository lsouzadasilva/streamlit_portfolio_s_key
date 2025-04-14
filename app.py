import streamlit as st
from paginas.sobre import pagina_inicial
from paginas.projetosbi import bi
from paginas.streamlit import streamlit
from paginas.chatbot import chatbot
from paginas.chatbot_huggingface import chatbot_huggingface
from paginas.certificados import certificados_skills
from streamlit_option_menu import option_menu
from paginas.machine_learnig import machine


st.set_page_config(
    page_title='Portfólio',
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


image_path_eu = "image/eu.jpg"

st.sidebar.markdown(f"""
    <div style="width: 120px; height: 120px; border-radius: 50%; overflow: hidden; 
                 margin: 0 auto 20px auto; border: 2px solid #ccc;">
        <img src="{image_path_eu}" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
""", unsafe_allow_html=True)

# st.sidebar.title("Navegação")
st.sidebar.divider()


    # https://icons.getbootstrap.com/ - > icon
with st.sidebar:
    paginas = option_menu(
    menu_title = "Menu",
    options = ["Sobre mim", "Projetos em Power BI", "Projetos em Streamlit & Plotly", "Projetos OpenAI", "Projetos Scikit-learn", "Projetos huggingface", "Certificados & Skills"],
    icons = ["envelope-at-fill", "bar-chart-fill", "graph-up-arrow", "robot", "cpu", "emoji-wink-fill", "award"],
    menu_icon ="cast",
    default_index = 0
    # orientation = "horizontal"  < - Agora
)



st.sidebar.divider()
st.sidebar.markdown("**Informações de contato.**")
col1, col2, col3 = st.sidebar.columns(3)

with col1:
    st.markdown("""
        <a href="https://github.com/lsouzadasilva" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="50" style="border-radius: 50%; padding: 10px; background-color: white;">
        </a>
        """, unsafe_allow_html=True)

with col2: 
    st.markdown("""
        <a href="https://wa.me/19994138086" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="50" style="border-radius: 50%; padding: 10px; background-color: #25D366;">
        </a>
        """, unsafe_allow_html=True)


with col3:
    st.markdown("""
        <a href="https://www.linkedin.com/in/leandro-souza-bi" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="50" style="border-radius: 50%; padding: 5px; background-color: white; border: 2px solid #0A66C2;">
        </a>
        """, unsafe_allow_html=True)




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
elif paginas == "Projetos Scikit-learn":
    machine()
