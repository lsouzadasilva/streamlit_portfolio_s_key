import streamlit as st


def streamlit():


    st.header("Relatorio em Streamlit & Plotly 📊", divider=True)

    image_path_plotly_strem = "image/stremlit_plotly.png"
    image_path_fifa = "image/stremlit.png"


    # st.sidebar.markdown("**Informações de contato.**")

    # st.sidebar.image("image/in.png", width=30)
    # st.sidebar.link_button("linkedin.",
    #                     "https://www.linkedin.com/in/leandro-souza-313136190?original_referer=")

    # st.sidebar.image("image/wh.png", width=30)
    # st.sidebar.link_button("Whatsapp.",
    #                    "https://wa.me/19994138086")
    

    col13, col14, col15 = st.columns(3)

    with col13:
        st.image(image_path_plotly_strem, caption="Relatorio de Faturamento", width=200)
        st.link_button("Acesse", 
                       "https://dashapp-test.streamlit.app/")
        

    with col14:
        st.image(image_path_plotly_strem, caption="Relatorio de Vendas", width=200)
        st.link_button("Acesse",
                       "https://dashappvendas.streamlit.app/")

    with col15:
        st.image(image_path_fifa, caption="Fifa Oficial Dataset", width=200)
        st.link_button("Acesse",
                       "https://appfifaproject.streamlit.app/")
        
    
