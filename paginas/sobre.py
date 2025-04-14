import streamlit as st
import webbrowser 

def pagina_inicial():

    st.header('Sobre', divider=True)

    # st.sidebar.markdown("**Informações de contato.**")

    # st.sidebar.image("image/in.png", width=30)

    # st.sidebar.link_button("linkedin.",
    #            "https://br.linkedin.com/in/leandro-souza-313136190")

    # st.sidebar.image("image/wh.png", width=30)
    # st.sidebar.link_button("Whatsapp.",
    #                    "https://wa.me/19994138086")


    st.markdown(
        """ 
        Especialista em Análise de Dados e Soluções Logísticas

        Sou apaixonado por transformar dados em insights estratégicos e criar soluções que otimizam 
        processos logísticos e análises de dados.
        
        Na Mobly, desenvolvi e implementei melhorias nos processos de inventário e controle de 
        estoque, aumentando a eficiência operacional. Já na Indecx, elaborei relatórios detalhados e 
        análises mercadológicas de veículos comerciais e leves para clientes como Localiza, Mercedes-Benz, 
        Movida, Unidas, LM Transportes, VW, BYD, Addiante Locação e outros. Além disso, 
        estruturei métricas de NPS e CSAT para o Tribanco, orientando decisões baseadas em dados.
        
        Mais recentemente, atuei na Hagens em um contrato temporário, sendo responsável pela 
        coleta, análise e visualização de dados, utilizando ferramentas como Power BI e Looker para 
        gerar insights acionáveis e apoiar estratégias empresariais.
        
        💡 Minhas principais habilidades incluem:
        
        * Ferramentas: Power BI, Looker, Power Query, Excel, Figma, GA4, BigQuery.
        
        * Linguagens de Programação: Python, SQL, DAX.
        
        * Python: Automação com bots, técnicas CRUD para gestão de dados, criação de Web e Apps com Streamlit.
        
        * IA e Machine Learning: Implementação da técnica RAG (Retrieval-Augmented Generation) para assistentes de IA, como o ChatOpenAI.
        
        * Análise de Dados: Desenvolvimento de dashboards interativos e relatórios avançados.
        
        * Otimização de Processos: Criação de bots de automações de processos.
        
        Estou sempre em busca de criar soluções inovadoras, traduzindo dados em decisões 
        estratégicas e contribuindo para o crescimento sustentável das organizações.""")
    
    st.divider()

    st.markdown("**Informações de contato.**")

    col1, col2 = st.sidebar.columns(2)

    with col1:
        st.markdown("""
            <a href="https://github.com/seu-usuario" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="50" style="border-radius: 50%; padding: 10px; background-color: #333;">
            </a>
            """, unsafe_allow_html=True)

    # WhatsApp
    with col2:
        st.markdown("""
            <a href="https://wa.me/19994138086" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="50" style="border-radius: 50%; padding: 10px; background-color: #25D366;">
            </a>
            """, unsafe_allow_html=True)

