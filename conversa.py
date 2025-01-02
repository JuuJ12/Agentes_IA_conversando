import os
from autogen import ConversableAgent
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

agente1=st.text_input('Digite o que o agente1 será')

student_agent = ConversableAgent(
    name="Agente 1",
    system_message=(f'Você vai responder sempre em português e será :{agente1}'),
    llm_config={
        "model": "llama3-70b-8192",
        #"base_url": 'https://api.groq.com/openai/v1',  
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":5
    },
)


agente2=st.text_input('Digite o que o agente2 será')

teacher_agent = ConversableAgent(
    name="Agente 2",
    system_message=(f' Você vai responder sempre em português e será :{agente2}'),
    llm_config={
        "model": "llama3-70b-8192",
        #"base_url": 'https://api.groq.com/openai/v1',  
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":5  
    },
)


assunto = st.text_input('Digite sobre qual assunto os agentes irão conversar')
button= st.button('enviar')


def chat(assunto):
    chat_result = student_agent.initiate_chat(
        teacher_agent,
        message=assunto,
        max_turns=4
    )
    return chat_result

if button:
    resultado = chat(assunto)
    # Iterar sobre o histórico da conversa
    col1,col2= st.columns(2)
    with col1:
        with st.chat_message('ai'):
            for i, turn in enumerate(resultado.chat_history):
                if turn['name'] == "Agente 1":
                    
                    st.write(f" {turn['name']} :")
                    st.write(f"Mensagem: {turn['content']}")
    with col2:
        with st.chat_message('ai'):
            for i, turn in enumerate(resultado.chat_history):
                if turn['name'] == "Agente 2":
                        
                        st.write(f"{turn['name']} :")
                        st.write(f"Mensagem: {turn['content']}")
            