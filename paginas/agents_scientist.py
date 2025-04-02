import os
from autogen import ConversableAgent
from dotenv import load_dotenv
import streamlit as st
from streamlit_lottie import st_lottie
from paginas.me import load_lottiefile
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
animacao2 = load_lottiefile('pictures/animacao_ia2.json')

# Função para calcular a similaridade de cosseno entre duas strings

def distance(state, goal_state):
    try:
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([state, goal_state])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        dist = 1 - similarity  # Quanto maior a similaridade, menor a distância
        return dist
    except Exception as e:
        print(f"Erro ao calcular a distância: {e}")
        return 1.0  # Distância máxima em caso de erro

# Função para calcular a recompensa
def calculate_reward(state, goal_state):
    try:
        dist = distance(state, goal_state)
        reward = -dist  # Quanto menor a distância, maior a recompensa (valor negativo)
        return reward
    except Exception as e:
        print(f"Erro ao calcular a recompensa: {e}")
        return -np.inf  # Penalidade alta em caso de erro

# Função para atualizar valor Q com tratamento de NaN
q_table = {}

def update_q_value(state, action, reward, next_state, alpha=0.1, gamma=0.9):
    try:
        state_action = (state, action)
        
        # Inicializa valor Q se não existir
        if state_action not in q_table:
            q_table[state_action] = 0.0
            
        # Valor Q atual
        current_q = q_table[state_action]
        
        # Melhor valor Q para o próximo estado
        next_q_values = [q_table.get((next_state, a), 0.0) for a in range(6)]
        max_next_q = max(next_q_values) if next_q_values else 0.0

        # Atualização de Q-Valor com verificação de NaN
        new_q = current_q + alpha * (reward + gamma * max_next_q - current_q)
        if np.isnan(new_q):
            print("Valor Q resultante é NaN. Ignorando atualização.")
            return

        q_table[state_action] = new_q
    except Exception as e:
        print(f"Erro ao atualizar valor Q: {e}")

# Função para obter a melhor ação usando epsilon-greedy
# Função para obter a melhor ação usando epsilon-greedy
epsilon = 0.1

def get_best_action(state):
    # Exploração: escolher uma ação aleatória com probabilidade epsilon
    if random.uniform(0, 1) < epsilon:
        return "Exploração Aleatória"  # Uma indicação clara de exploração

    # Obter as ações registradas no estado atual
    q_values = {action: q_value for (s, action), q_value in q_table.items() if s == state}
    
    if q_values:
        # Seleciona a melhor ação pelo valor Q máximo
        best_action = max(q_values, key=q_values.get)
        return f"Ação mais promissora: {best_action[:100]}..."  # Mostra um resumo da ação
    else:
        return "Nenhuma ação registrada"

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
        modelo_agente_7 = st.selectbox('Selecione o Modelo do Agente Sintetizador',options=['llama3-70b-8192',
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

agente_7 = ConversableAgent(
    name="Agente-7-Sintetizador",
    system_message=(f'''Você vai responder sempre em {idioma}, sua função será 
                    Ler todas as soluções finais dos debatedores
                    e consolidar uma solução final abrangente para o problema elencando as melhores ideias dos debatedores no debate realizado'''),
    llm_config={
        "model": modelo_agente_7,
          
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1
    },
)

        
def chat(assunto):
    state = "inicio"
    previous_response = assunto
    agentes = [agente_1, agente_2, agente_3, agente_4, agente_5, agente_6]
    respostas = []

    for idx, agente in enumerate(agentes):
        chat_result = agente.generate_reply(messages=[{"role": "user", "content": previous_response}])
        resposta = chat_result['content']
        next_state = f"debate-{idx+1}"
        
        # Calcula a recompensa com base na resposta
        goal_state = "objetivo"  # Defina um estado objetivo apropriado
        reward = calculate_reward(resposta, goal_state)
        update_q_value(state, resposta, reward, next_state)
        best_action = get_best_action(state)

        respostas.append(resposta)
        previous_response = resposta
        st.write(f"**Modelo Utilizado:** {agente.llm_config.config_list[0]['model']}")
        st.write(f"💡 Ação recomendada com base na Equação de Bellman: **{best_action}**")
        yield f"\n🤖 **{agente.name}** respondeu: {resposta}"
        st.write("________")
        state = next_state

    resposta_sintetizada = agente_7.generate_reply(messages=[{"role": "user", "content": " ".join(respostas)}])
    resposta_final = resposta_sintetizada['content']
    st.write(f"**Modelo Utilizado:** {agente_7.llm_config.config_list[0]['model']}")
    yield f"\n📝 **{agente_7.name}** sintetizou: {resposta_final}"




if button:
    with st.spinner('Aguarde um momento, os agentes estão batendo um papo 🗣...'):
        resultado = chat(assunto)

        for resultado in resultado:

                with st.chat_message('ai'):
                    st.write(resultado)
                    st.write("________")

