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
     st.write('Esse sistema tem como objetivo mostrar como  agentes de Inteligência Artificial(IA) podem conversar entre si,\
                e resolver problemas juntos. Para iniciar a conversa, você pode definir assunto da conversa.')
     
col1,col2 = st.columns([1.2,0.5], vertical_alignment='center')
with col1:
    global idioma
    idioma = st.selectbox(label='Idioma', options=['Português','Inglês','Japonês','Russo','Espanhol','Frânces','Italiano'])

    global assunto
    assunto = st.text_input(label='Assunto', help='Defina o assunto que os agentes irão gerar hipoteses e irão aplicar revisão, classificação,evolução,organização e meta-revisão para as hipoteses.',
                             placeholder=' Exemplo: Problema dos Três Corpos')
    button= st.button('Iniciar Conversa')


with col2:
    animacao = load_lottiefile('pictures/animacao_ia.json')
    
    st_lottie(animacao)

    

agente_1 = ConversableAgent(
    name='Agente-Gerador-Hipóteses',
    system_message=(f'Você vai responder sempre em {idioma} e será um gerador de hipóteses criativas e cientificamente embasadas sobre o tema fornecido. '),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)


agente_2 = ConversableAgent(
    name="Agente-Revisor",
    system_message=(f'Você vai responder sempre em {idioma} e vai revisar criticamente as hipóteses fornecidas, verificando sua novidade, correção e qualidade. '),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)

agente_3 = ConversableAgent(
    name="Agente-Classificador",
    system_message=(f'''Você vai responder sempre em {idioma} e vai 
                    classificar as hipóteses com base em critérios científicos, priorizando as mais promissoras.'''),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)


agente_4 = ConversableAgent(
    name="Agente-Evolucionador",
    system_message=(f'''Você vai responder sempre em ({idioma} e vai 
                    refinar as hipóteses mais bem classificadas, tornando-as mais inovadoras e viáveis.'''),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)


agente_5 = ConversableAgent(
    name="Agente-Organizador",
    system_message=(f'''Você vai responder sempre em {idioma} e vai 
                    agrupar hipóteses similares para facilitar a exploração eficiente.'''),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)

agente_6 = ConversableAgent(
    name="Agente-Metarevisor",
    system_message=(f'''Você vai responder sempre em {idioma} e vai 
                    analisar os feedbacks e proponha melhorias para aperfeiçoar o ciclo de geração e avaliação de hipóteses.'''),
    llm_config={
        "model": "llama3-70b-8192",
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)



def chat1(assunto):
        
        chat_result_1 = agente_1.generate_reply(messages=[{"role": "user", "content": f"Gere hipóteses sobre: {assunto}"}])
        hipoteses_geradas = chat_result_1['content']
        yield f"\n🧠**{agente_1.name}**\n respondeu : {hipoteses_geradas}"

        chat_result_2 = agente_2.generate_reply(messages=[{"role": "user", "content": f"Revise estas hipóteses: {hipoteses_geradas}"}])
        revisao = chat_result_2['content']
        yield f"\n✍️**{agente_2.name}** respondeu, {revisao} "

        
        chat_result_3 = agente_3.generate_reply(messages=[{"role": "user", "content": f"Classifique as hipóteses revisadas: {revisao}"}])
        classificacao = chat_result_3['content']
        yield f"\n📊**{agente_3.name}** respondeu , {classificacao}"

        chat_result_4 = agente_4.generate_reply(messages=[{"role": "user", "content": f"Refine as hipóteses mais bem classificadas: {classificacao}"}])
        refinacao = chat_result_4['content']
        yield f"\n🔬**{agente_4.name}** respondeu, {refinacao}"
        
        chat_result_5 = agente_5.generate_reply(messages=[{"role": "user", "content": f"Agrupe as hipóteses similares: {refinacao}"}])
        organizacao = chat_result_5['content']
        yield f"\n 👷‍♂️ **{agente_5.name}** respondeu, {organizacao}"

        chat_result_6 = agente_6.generate_reply(messages=[{"role": "user", "content": f"Analise os feedbacks: {organizacao}"}])
        meta_revisao = chat_result_6['content']
        yield f"\n🧐**{agente_6.name}** respondeu, {meta_revisao}"

        
        


if button:
    with st.spinner('Aguarde um momento, os agentes estão batendo um papo 🗣...'):
        resultado = chat1(assunto)

        for resultado in resultado:

                with st.chat_message('ai'):
                    st.write(resultado)
                    st.write("________")

