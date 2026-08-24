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
animacao2 = load_lottiefile('pictures/animacao_ia.json')

# Inicialização dos valores no session_state
defaults = {
    'funcao_agente1': 'Gerador de Hipóteses, explorando a literatura e usando técnicas como debates simulados e identificação iterativa de suposições para propor hipóteses de pesquisa. Escolha uma Hipótese caso não receba uma.',
    'funcao_agente2': 'Revisor, avaliando criticamente hipóteses quanto à novidade, correção e qualidade, baseando-se em pesquisas na web e literatura científica, faça sua revisão lembrando que ela será passada para um organizador que utilizando um sistema de torneio baseado em Elo para classificar hipóteses com base em debates científicos e feedbacks de revisão, priorizando ideias promissoras.',
    'funcao_agente3': 'Classificador, utilizando um sistema de torneio baseado em Elo para classificar hipóteses com base em debates científicos e feedbacks de revisão, priorizando ideias promissoras, faça sua classificação lembrando que ela será passada para um evololucionador que vai refinar as hipóteses mais bem classificadas ao incorporar novos insights, simplificar conceitos e explorar abordagens não convencionais.',
    'funcao_agente4': 'Evolucionador,refinando as hipóteses mais bem classificadas ao incorporar novos insights, simplificar conceitos e explorar abordagens não convencionais, faça sua refinação lembrando que ela será passada para um organizador que vai agrupar hipóteses com base em similaridade para gerenciar o espaço de hipóteses e facilitar a exploração eficiente .',
    'funcao_agente5': 'Organizador,  agrupando hipóteses com base em similaridade para gerenciar o espaço de hipóteses e facilitar a exploração eficiente, faã sua organização lembrando que ela será passada para um meta revisor que vai sintetizar feedbacks de todas as revisões e torneios para identificar problemas recorrentes e orientar a melhoria do sistema, criando efetivamente um ciclo de autoaperfeiçoamento..',
    'funcao_agente6': 'Meta Revisor,sintetizando feedbacks de todas as revisões e torneios para identificar problemas recorrentes e orientar a melhoria do sistema, criando efetivamente um ciclo de autoaperfeiçoamento.',
    'modelo_agente_1': 'openai/gpt-oss-120b',
    'modelo_agente_2': 'openai/gpt-oss-120b',
    'modelo_agente_3': 'openai/gpt-oss-120b',
    'modelo_agente_4': 'openai/gpt-oss-120b',
    'modelo_agente_5': 'openai/gpt-oss-120b',
    'modelo_agente_6': 'openai/gpt-oss-120b',
    'modelo_agente_7': 'openai/gpt-oss-120b',
    'idioma': 'Português',
    'assunto': '',
    'resposta_sintetizador': "",
    'respostas_agentes': []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

for i in range(1, 8):
    mkey = f'modelo_agente_{i}'
    if mkey in st.session_state:
        if not isinstance(st.session_state[mkey], str) or not st.session_state[mkey].startswith('groq/'):
            st.session_state[mkey] = 'openai/gpt-oss-120b'
    else:
        st.session_state[mkey] = 'openai/gpt-oss-120b'

# Funções auxiliares
def distance(state, goal_state):
    try:
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([state, goal_state])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return 1 - similarity
    except Exception as e:
        print(f"Erro ao calcular a distância: {e}")
        return 1.0

def calculate_reward(state, goal_state):
    try:
        dist = distance(state, goal_state)
        return -dist
    except Exception as e:
        print(f"Erro ao calcular a recompensa: {e}")
        return -np.inf

q_table = {}
epsilon = 0.1

def update_q_value(state, action, reward, next_state, alpha=0.1, gamma=0.9):
    try:
        state_action = (state, action)
        if state_action not in q_table:
            q_table[state_action] = 0.0
        current_q = q_table[state_action]
        next_q_values = [q_table.get((next_state, a), 0.0) for a in range(6)]
        max_next_q = max(next_q_values) if next_q_values else 0.0
        new_q = current_q + alpha * (reward + gamma * max_next_q - current_q)
        if not np.isnan(new_q):
            q_table[state_action] = new_q
    except Exception as e:
        print(f"Erro ao atualizar valor Q: {e}")

def get_best_action(state):
    if random.uniform(0, 1) < epsilon:
        return "Exploração Aleatória"
    q_values = {action: q_value for (s, action), q_value in q_table.items() if s == state}
    if q_values:
        best_action = max(q_values, key=q_values.get)
        return f"Ação mais promissora no estado '{state}'"
    else:
        return "Nenhuma ação registrada"

# UI
st.title('Agentes de Inteligência Artificial')

with st.expander('Sobre o Projeto'):
    st.write('Esse sistema tem como objetivo mostrar como agentes de Inteligência Artificial (IA) podem conversar entre si e resolver problemas juntos. Para iniciar a conversa, você pode definir assunto da conversa.')

with st.expander('Ajustando seus Agentes'):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Função dos Agentes')
        st.write('Os agentes já vem com funções definidas porém, você pode alterar como você quiser!')
        st.session_state.funcao_agente1 = st.text_input('Função do Agente 1', help='Por padrão o Agente 1 é um Gerador de Hipóteses.', value=st.session_state.funcao_agente1) or 'Gerador de Hipóteses, explorando a literatura e usando técnicas como debates simulados e identificação iterativa de suposições para propor hipóteses de pesquisa. Escolha uma Hipótese caso não receba uma.'
        st.session_state.funcao_agente2 = st.text_input('Função do Agente 2', help='Por padrão o Agente 2 é um Revisor.', value=st.session_state.funcao_agente2) or 'Revisor, avaliando criticamente hipóteses quanto à novidade, correção e qualidade, baseando-se em pesquisas na web e literatura científica.'
        st.session_state.funcao_agente3 = st.text_input('Função do Agente 3', help='Por padrão o Agente 3 é um Classficador.', value=st.session_state.funcao_agente3) or'Classificador, utilizando um sistema de torneio baseado em Elo para classificar hipóteses com base em debates científicos e feedbacks de revisão, priorizando ideias promissoras.'
        st.session_state.funcao_agente4 = st.text_input('Função do Agente 4', help='Por padrão o Agente 4 é um  Evolucionador.', value=st.session_state.funcao_agente4) or 'Evolucionador,refinando as hipóteses mais bem classificadas ao incorporar novos insights, simplificar conceitos e explorar abordagens não convencionais.'
        st.session_state.funcao_agente5 = st.text_input('Função do Agente 5', help='Por padrão o Agente 5 é um  Organizador.', value=st.session_state.funcao_agente5) or 'Organizador,  agrupando hipóteses com base em similaridade para gerenciar o espaço de hipóteses e facilitar a exploração eficiente.'
        st.session_state.funcao_agente6 = st.text_input('Função do Agente 6', help='Por padrão o Agente 6 é um Meta Revisor.', value=st.session_state.funcao_agente6) or 'Meta Revisor,sintetizando feedbacks de todas as revisões e torneios para identificar problemas recorrentes e orientar a melhoria do sistema, criando efetivamente um ciclo de autoaperfeiçoamento.'
    with col2:
        st.subheader('Modelos de IA')
        st.write('Por padrão os Agentes já vem com o modelo openai/gpt-oss-120b.')
        modelos = ['openai/gpt-oss-120b','groq/compound-mini','openai/gpt-oss-safeguard-20b']
        for i in range(1, 8):
            key = f'modelo_agente_{i}'
            # Guard against invalid session values by falling back to default index
            try:
                idx = modelos.index(st.session_state[key])
            except ValueError:
                idx = 0
                st.session_state[key] = modelos[0]
            st.session_state[key] = st.selectbox(f'Modelo do Agente {i if i < 7 else "Sintetizador"}', modelos, index=idx)

col1, col2 = st.columns([1.2, 0.5])
with col1:
    st.session_state.idioma = st.selectbox('Idioma', ['Português', 'Inglês', 'Japonês', 'Russo', 'Espanhol', 'Frânces', 'Italiano'], index=['Português', 'Inglês', 'Japonês', 'Russo', 'Espanhol', 'Frânces', 'Italiano'].index(st.session_state.idioma))
    st.session_state.assunto = st.text_input('Assunto',  help='Escreva o que você deseja, uma duvida, um problema, qualquer coisa !',value=st.session_state.assunto)
    button = st.button('Iniciar Conversa')

with col2:
    st_lottie(animacao2)

# Criação dos agentes
def criar_agente(nome, funcao, modelo):
    return ConversableAgent(
        name=nome,
        system_message=(f'Você vai responder sempre em {st.session_state.idioma}, sempre vai atacar e tentar resolver o problema e sua função é {funcao}.'),
        llm_config={
            "model": modelo,
            "api_key": os.getenv("GROQ_API_KEY"),
            "api_type": "groq",
            "temperature": 0,
            'max_tokens': 500
        }
    )

agentes = [criar_agente(f'Agente-{i+1}', st.session_state[f'funcao_agente{i+1}'], st.session_state[f'modelo_agente_{i+1}']) for i in range(6)]

agente_7 = ConversableAgent(
    name="Agente-7-Sintetizador",
    system_message=(f'''Você vai responder sempre em {st.session_state.idioma}. Sua função será:
        1. Ler todas as soluções finais dos debatedores.
        2. Consolidar uma solução final abrangente.
        3. Elencar as melhores ideias dos debatedores.
        4. Finalizar com uma conclusão.
        5. Reescrever o texto inicial.'''),
    llm_config={
        "model": st.session_state.modelo_agente_7,
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature": 0
    }
)

# Chat
def chat(assunto):
    state = "inicio"
    previous_response = assunto
    respostas = []

    for idx, agente in enumerate(agentes):
        chat_result = agente.generate_reply(messages=[{"role": "user", "content": previous_response}])
        resposta = chat_result['content']
        next_state = f"debate-{idx+1}"
        reward = calculate_reward(resposta, "objetivo")
        update_q_value(state, resposta, reward, next_state)
        best_action = get_best_action(state)

        respostas.append(resposta)
        previous_response = resposta

        # Salvando a resposta no session_state
        st.session_state.respostas_agentes.append({
            "modelo": agente.llm_config.config_list[0]['model'],
            "nome": agente.name,
            "resposta": resposta,
            "acao": best_action
        })

        yield f"\n🤖 **{agente.name}** respondeu: {resposta}"
        state = next_state

    resposta_sintetizada = agente_7.generate_reply(messages=[{"role": "user", "content": " ".join(respostas)}])
    st.session_state.resposta_sintetizador = resposta_sintetizada['content']
    yield f"\n📝 **{agente_7.name}** sintetizou: {resposta_sintetizada['content']}"


# Execução
if button:
    # Resetar respostas antigas
    st.session_state.respostas_agentes = []
    st.session_state.resposta_sintetizador = ""

    with st.spinner('Aguarde um momento, os agentes estão batendo um papo 🗣...'):
        for resultado in chat(st.session_state.assunto):
            with st.chat_message('ai'):
                st.write(resultado)

if 'respostas_agentes' in st.session_state and st.session_state.respostas_agentes:
    st.subheader("💬 Respostas anteriores dos agentes:")
    for resposta in st.session_state.respostas_agentes:
        st.write(f"**{resposta['nome']}** (modelo: {resposta['modelo']})")
        st.write(f"🗣 Resposta: {resposta['resposta']}")
        st.markdown("---")


if 'resposta_sintetizador' in st.session_state and st.session_state.resposta_sintetizador:
    st.subheader("📝 Resposta do Agente Sintetizador:")
    st.write(st.session_state.resposta_sintetizador)

