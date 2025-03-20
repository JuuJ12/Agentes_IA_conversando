import os
from autogen import ConversableAgent
from dotenv import load_dotenv
import streamlit as st
from streamlit_lottie import st_lottie
from paginas.me import load_lottiefile

load_dotenv()
animacao2 = load_lottiefile('pictures/animacao_ia2.json')
st.title('Agentes de Inteligência Artificial')

with st.expander('Sobre o Projeto'):
    st.write('Esse sistema tem como objetivo mostrar como  agentes de Inteligência Artificial(IA) podem conversar entre si\
                e resolver problemas juntos. Para iniciar a conversa, você pode definir assunto da conversa.')


with st.expander('Ajustando seus Agentes'):
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Função dos Agentes')

        st.write('Os agentes já vem com funções definidas porém, você pode alterar como você quiser!')

        global funcao_agente1, funcao_agente2, funcao_agente3,funcao_agente4,funcao_agente5,funcao_agente6
        funcao_agente1 = st.text_input(label='Função do Agente 1', help='Por padrão o Agente 1 é um Gerador de Hipóteses.',
                             placeholder=' Exemplo: Planejador Estratégico') or 'Gerador de Hipóteses e escolherá algum assunto para gerar hipoteses.'
        funcao_agente2 = st.text_input(label='Função do Agente 2', help='Por padrão o Agente 2 é um Revisor.',
                             placeholder=' Exemplo: Analista de Tendêcnias') or 'Revisor'
        funcao_agente3 = st.text_input(label='Função do Agente 3', help='Por padrão o Agente 3 é um Classficador.',
                             placeholder=' Exemplo: Assistente de Aprendizado') or 'Classificador'
        funcao_agente4 = st.text_input(label='Função do Agente 4', help='Por padrão o Agente 4 é um  Evolucionador.',
                             placeholder=' Exemplo: Simulador de Cenários') or 'Evolucionador'
        funcao_agente5 = st.text_input(label='Função do Agente 5', help='Por padrão o Agente 5 é um  Organizador.',
                             placeholder=' Exemplo: Especialista em Criatividade') or 'Organizador'
        funcao_agente6 = st.text_input(label='Função do Agente 6', help='Por padrão o Agente 6 é um Meta Revisor.',
                             placeholder=' Exemplo: Medidor de Conflitos') or 'Meta Revisor'
    with col2:
        st.subheader('Modelos de IA')

        st.write('Por padrão os Agentes já vem com o modelo llama3-70b-8192.')

        global modelo_agente_1,modelo_agente_2,modelo_agente_3,modelo_agente_4,modelo_agente_5,modelo_agente_6
        modelo_agente_1 = st.selectbox('Selecione o Modelo do Agente 1',options=['llama3-70b-8192',
                                                                                 'gemma2-9b-it','mistral-saba-24b']) or 'llama3-70b-8192'
       
        modelo_agente_2 = st.selectbox('Selecione o Modelo do Agente 2',options=['llama3-70b-8192',
                                                                                 'gemma2-9b-it','mistral-saba-24b'])or 'llama3-70b-8192'
        
        modelo_agente_3 = st.selectbox('Selecione o Modelo do Agente 3',options=['llama3-70b-8192',
                                                                                 'gemma2-9b-it','mistral-saba-24b'])or 'llama3-70b-8192'
        
        modelo_agente_4 = st.selectbox('Selecione o Modelo do Agente 4',options=['llama3-70b-8192',
                                                                                 'gemma2-9b-it','mistral-saba-24b'])or 'llama3-70b-8192'
        
        modelo_agente_5 = st.selectbox('Selecione o Modelo do Agente 5',options=['llama3-70b-8192',
                                                                                 'gemma2-9b-it','mistral-saba-24b'])or 'llama3-70b-8192'
        
        modelo_agente_6 = st.selectbox('Selecione o Modelo do Agente 6',options=['llama3-70b-8192',
                                                                                 'gemma2-9b-it','mistral-saba-24b'])or 'llama3-70b-8192'

col1,col2 = st.columns([1.2,0.5], vertical_alignment='center')
with col1:
    global idioma
    idioma = st.selectbox(label='Idioma', options=['Português','Inglês','Japonês','Russo','Espanhol','Frânces','Italiano'], help='Idioma que os Agentes irão responder')

    global assunto
    assunto = st.text_input(label='Assunto', help='Escreva o que você deseja, uma duvida, um problema, qualquer coisa !',
                             placeholder=' Exemplo: Eu tenho uma abordagem X para o problema P vs NP')
    button= st.button('Iniciar Conversa')


with col2:
    animacao = load_lottiefile('pictures/animacao_ia.json')
    
    st_lottie(animacao)

    

agente_1 = ConversableAgent(
    name= 'Agente-1',
    system_message=(f'Você vai responder sempre em {idioma}, sempre vai atacar e tentar resolver o problema e sua função é {funcao_agente1}. '),
    llm_config={
        "model": modelo_agente_1,
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)


agente_2 = ConversableAgent(
    name="Agente-2",
    system_message=(f'Você vai responder sempre em {idioma}, sempre vai atacar e tentar resolver o problema e sua função é {funcao_agente2} '),
    llm_config={
        "model": modelo_agente_2,
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)

agente_3 = ConversableAgent(
    name="Agente-3",
    system_message=(f'''Você vai responder sempre em {idioma}, sempre vai atacar e tentar resolver o problema e sua função é {funcao_agente3}.'''),
    llm_config={
        "model": modelo_agente_3,
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)


agente_4 = ConversableAgent(
    name="Agente-4",
    system_message=(f'''Você vai responder sempre em {idioma}, sempre vai atacar e tentar resolver o problema e sua função é {funcao_agente4}.'''),
    llm_config={
        "model": modelo_agente_4,
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)


agente_5 = ConversableAgent(
    name="Agente-5",
    system_message=(f'''Você vai responder sempre em {idioma}, sempre vai atacar e tentar resolver o problema e sua função é {funcao_agente5}.'''),
    llm_config={
        "model": modelo_agente_5,
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)

agente_6 = ConversableAgent(
    name="Agente-6",
    system_message=(f'''Você vai responder sempre em {idioma}, sempre vai atacar e tentar resolver o problema e sua função é {funcao_agente6}.'''),
    llm_config={
        "model": modelo_agente_6,
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)



def chat1(assunto):
        
        chat_result_1 = agente_1.generate_reply(messages=[{"role": "user", "content": f"{assunto}"}])
        resposta_agente_1 = chat_result_1['content']
        st.write(f'**Modelo Utilizado** **{modelo_agente_1}**')
        yield f"\n🧠**{agente_1.name}**\n respondeu : {resposta_agente_1}"

        chat_result_2 = agente_2.generate_reply(messages=[{"role": "user", "content": f"{resposta_agente_1}"}])
        resposta_agente_2 = chat_result_2['content']
        st.write(f'**Modelo Utilizado** **{modelo_agente_2}**')
        yield f"\n✍️**{agente_2.name}** respondeu, {resposta_agente_2} "

        
        chat_result_3 = agente_3.generate_reply(messages=[{"role": "user", "content": f" {resposta_agente_2}"}])
        resposta_agente_3 = chat_result_3['content']
        st.write(f'**Modelo Utilizado** **{modelo_agente_3}**')
        yield f"\n📊**{agente_3.name}** respondeu , {resposta_agente_3}"

        chat_result_4 = agente_4.generate_reply(messages=[{"role": "user", "content": f"{resposta_agente_3}"}])
        resposta_agente_4 = chat_result_4['content']
        st.write(f'**Modelo Utilizado** **{modelo_agente_4}**')
        yield f"\n🔬**{agente_4.name}** respondeu, {resposta_agente_4}"
        
        chat_result_5 = agente_5.generate_reply(messages=[{"role": "user", "content": f" {resposta_agente_4}"}])
        resposta_agente_5 = chat_result_5['content']
        st.write(f'**Modelo Utilizado** **{modelo_agente_5}**')
        yield f"\n 👷‍♂️ **{agente_5.name}** respondeu, {resposta_agente_5}"

        chat_result_6 = agente_6.generate_reply(messages=[{"role": "user", "content": f" {resposta_agente_5}"}])
        resposta_agente_6 = chat_result_6['content']
        st.write(f'**Modelo Utilizado** **{modelo_agente_6}**')
        yield f"\n🧐**{agente_6.name}** respondeu, {resposta_agente_6}"

        
        


if button:
    with st.spinner('Aguarde um momento, os agentes estão batendo um papo 🗣...'):
        resultado = chat1(assunto)

        for resultado in resultado:

                with st.chat_message('ai'):
                    st.write(resultado)
                    st.write("________")

