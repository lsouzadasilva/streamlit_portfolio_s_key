import streamlit as st

def chatbot():


    st.header("🤖J.A.R.V.I.S", divider=True)


    image_path_openai= "image/stremlit_openai.png"
    image_path_openai_groq = "image/stremlit_openai_groq.png"


    # st.sidebar.markdown("**Informações de contato.**")

    # st.sidebar.image("image/in.png", width=30)
    # st.sidebar.link_button("linkedin.",
    #                     "https://www.linkedin.com/in/leandro-souza-313136190?original_referer=")

    # st.sidebar.image("image/wh.png", width=30)
    # st.sidebar.link_button("Whatsapp.",
    #                    "https://wa.me/19994138086")
    

    col15, col16, col17, col18 = st.columns(4)


    with col15:
        st.image(image_path_openai, caption="Chat Bot com OpenAI", width=200)
        st.link_button("Acesse",
                       "https://sreamlitopenai.streamlit.app/") 
    
    with col16:
        st.image(image_path_openai, caption= "Transcrição de audio e video (MP3, MP4)", width=200)
        st.link_button("Acesse",
                       "https://transcriptprojet.streamlit.app/")
        
    with col17:
        st.image(image_path_openai, caption="Assistants com OpenAI", width=200)
        st.link_button("Acesse",
                 "https://assistant-insight-openai.streamlit.app/")

    with col18:
        st.image(image_path_openai, caption="Chat Bot de leitura PDF", width=200)
        st.link_button("Acesse",
                       "https://assistants-read-pdf.streamlit.app/")


    st.divider()

    col19, = st.columns(1)

    with col19:
        st.image(image_path_openai_groq, caption="Oraculo", width=200)
        st.link_button("Acesse",
                       "https://publicoraculo.streamlit.app/")
        
