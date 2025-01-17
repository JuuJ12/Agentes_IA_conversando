import os
from autogen import ConversableAgent
from dotenv import load_dotenv
import streamlit as st
from streamlit_lottie import st_lottie
from paginas.me import load_lottiefile

load_dotenv()
animacao2 = load_lottiefile('pictures/animacao_ia2.json')
st.title('Agentes de IA')

with st.expander('Sobre o Projeto'):
     st.write('Esse sistema tem como objetivo mostrar como dois agentes de Inteligência Artificial(IA) podem conversar entre si,\
                e resolver problemas juntos. Para iniciar a conversa, você pode definir o idioma,\
                a função de cada agente e o assunto da conversa.')
     
col1,col2 = st.columns([1.2,0.5], vertical_alignment='center')
with col1:
    idioma = st.selectbox(label='Idioma', options=['Português','Inglês','Japonês','Russo','Espanhol','Frânces','Italiano'])

    agente1=st.text_input(label='Função do Agente 1', help='Defina Qual Será a Especialidade do Agente 1 . ', 
                          placeholder='Ex: Profissional de Logística', key='agente1')

    agente2=st.text_input(label='Função do Agente 2', help='Defina Qual Será a Especialidade do Agente 2.', 
                          placeholder='Ex: Profissional de Engenharia')

    assunto = st.text_input(label='Assunto', help='Defina Sobre o que os Agentes Irão Falar ou o que Irão Resolver.',
                             placeholder='Como podemos unir a engenharia e logística?')
    escolha = st.radio('Escolha quem irá iniciar a conversa', options=["Agente 1","Agente 2"])

    turnos = st.slider('Quantidade de Turnos', min_value=1, max_value=6, value=2)
    with st.expander('Nota Sobre os Turnos'):
        st.warning('Os agentes irão conversar pela quantidade de turnos escolhida. Mas lembre-se mais turnos geram um tempo de espera um pouco maior.')
    button= st.button('Iniciar Conversa')


with col2:
    animacao = load_lottiefile('pictures/animacao_ia.json')
    
    st_lottie(animacao)
    

agente_1 = ConversableAgent(
    name='Agente1',
    system_message=(f'Você vai responder sempre em {idioma} e será {agente1}'),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)


agente_2 = ConversableAgent(
    name="Agente2",
    system_message=(f' Você vai responder sempre em {idioma} e será {agente2}'),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)


def chat1(assunto):
        chat_result = agente_1.initiate_chat(
            agente_2,
            message=assunto,
            max_turns=turnos
        )
        return chat_result


def chat2(assunto):
        chat_result = agente_2.initiate_chat(
            agente_1,
            message=assunto,
            max_turns=turnos
        )
        return chat_result

if button:
    with st.spinner('Aguarde um momento, os agentes estão batendo um papo 🗣...'):
        if escolha == 'Agente 1':
        
            resultado = chat1(assunto)

        else:
             resultado = chat2(assunto)

    for turn in resultado.chat_history:
            with st.chat_message('ai'):
                st.write(f"{turn['name']}: {turn['content']}")
                st.write("__________________________________")
    
