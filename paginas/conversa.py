import os
from autogen import ConversableAgent
from dotenv import load_dotenv
import streamlit as st
from streamlit_lottie import st_lottie
from paginas.me import load_lottiefile
load_dotenv()
animacao2 = load_lottiefile('pictures/animacao_ia2.json')


col1,col2 = st.columns([1.2,0.5], vertical_alignment='center')
with col1:
    idioma = st.selectbox(label='Idioma', options=['Português','Inglês','Japonês','Russo','Espanhol','Frânces','Italiano'])

    agente1=st.text_input(label='Função do Agente 1', help='Defina Qual Será a Especialidade do Agente 1.', 
                          placeholder='Ex: Profissional de Logística', key='agente1')

    agente2=st.text_input(label='Função do Agente 2', help='Defina Qual Será a Especialidade do Agente 2.', 
                          placeholder='Ex: Profissional de Engenharia')

    assunto = st.text_input(label='Assunto', help='Defina Sobre o que os Agentes Irão Falar ou o que Irão Resolver.',
                             placeholder='Como podemos unir a engenharia e logística?')

    button= st.button('Iniciar Conversa')


with col2:
    animacao = load_lottiefile('pictures/animacao_ia.json')
    
    st_lottie(animacao)
    

student_agent = ConversableAgent(
    name="Agente 1",
    system_message=(f'Você vai responder sempre em {idioma} e será {agente1}'),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":5
    },
)


teacher_agent = ConversableAgent(
    name="Agente 2",
    system_message=(f' Você vai responder sempre em {idioma} e será {agente2}'),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":5  
    },
)


def chat(assunto):
    chat_result = student_agent.initiate_chat(
        teacher_agent,
        message=assunto,
        max_turns=4
    )
    return chat_result

if button:
    with st.spinner('Aguarde um momento, os agentes estão batendo um papo 🗣...'):
        
        
        resultado = chat(assunto)
    for turn in resultado.chat_history:
            with st.chat_message('ai'):
                st.write(f"{turn['name']}: {turn['content']}")
                st.write("__________________________________")
    
