import streamlit as st


def streamlit():


    st.header("Relatorio em Streamlit & Plotly 📊", divider=True)

    image_path_fifa = "image/stremlit_kaggle.png"
    image_path_streamlit_plotly_pandas = "image/stremlit_plotly_pandas.png"


    # st.sidebar.markdown("**Informações de contato.**")

    # st.sidebar.image("image/in.png", width=30)
    # st.sidebar.link_button("linkedin.",
    #                     "https://www.linkedin.com/in/leandro-souza-313136190?original_referer=")

    # st.sidebar.image("image/wh.png", width=30)
    # st.sidebar.link_button("Whatsapp.",
    #                    "https://wa.me/19994138086")
    

    col13, col14, col15, col16 = st.columns(4)

    with col13:
        st.image(image_path_streamlit_plotly_pandas, caption="Relatorio de Faturamento", width=200)
        st.link_button("Acesse", 
                       "https://dashapp-test.streamlit.app/")
        
    with col14:
        st.image(image_path_streamlit_plotly_pandas, caption="Relatorio de Vendas", width=200)
        st.link_button("Acesse",
                       "https://dashappvendas.streamlit.app/")

    with col15:
        st.image(image_path_fifa, caption="Fifa Oficial Dataset", width=200)
        st.link_button("Acesse",
                       "https://appfifaproject.streamlit.app/")
        
    with col16:
        st.image(image_path_streamlit_plotly_pandas, caption="Relatório de Análise de Veículos Elétricos — 2023", width=200)
        st.link_button("Acesse",
                       "https://appdashveiculareletricos.streamlit.app/")
        
    st.divider()
    
    col17, = st.columns(1)
    
    with col17:
        st.image(image_path_fifa, caption="Geradr de dados fake", width=200)
        st.link_button("Acesse.",
                       "https://manager-data-fake.streamlit.app/")
        
    
