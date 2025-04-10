import streamlit as st
from streamlit_lottie import st_lottie
import json

# Função para carregar animação Lottie
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


animacao = load_lottiefile("pictures/animacao_ia2.json")



st.title("🧠 Experiência com Agentes de Inteligência Artificial")

# Seções da apresentação
st.header("1. Quem Sou Eu e o Projeto")
st.markdown("""
- Julio Vitor dos Santos.
- Graduando Bacharelador em Sistemas de Informação.
- Sistema com **Agentes de IA com foco em simular debates e colaboração entre sí na resolução de problemas.**.
- Aplicação prática: **geração e refinamento de hipóteses científicas**.
""")

st.header("2. O que Tive que Aprender")

with st.expander('Redes Neurais Artificiais'):
    st.subheader('Apenas o entendimento básico')
    st.markdown(""" Para dar inicio a essa jornada, foi necessário uma estudo sobre as redes neurais e seu funcionamento. Foi utilizado o proprio curso do google de Machine 
                Learning  e Redes Neurais para esse estudo.
                Não se preocupem em virar os mestres das redes neurais apenas aprendam os conceitos
                 gerais e como tempo peguem o resto.  """)
    st.markdown(""" Link para curso do [Google](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework?hl=pt-br) """)

with st.expander('Large Language Models'):
    st.subheader('Apenas o entendimento básico')
    st.markdown(""" Aqui está o coração desse sistema, os Largue Language Models(Modelos de Linguagem Grandes). Os Large Language Models (LLMs) são inteligências artificiais treinadas com enormes quantidades de texto para entender e gerar linguagem humana, são como “cérebros de texto” gigantes treinados para conversar e ajudar.
                Novamente foi utilizado o site do google para este estudo.""")

    st.markdown("""
                - Embedings.
                - Janelas de Contexto.
                """)
    st.markdown(""" Link para curso do [Google](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework?hl=pt-br) """)

with st.expander(' APIs '):
    st.subheader('Se Conectando com uma API')
    st.markdown(""" Para que possa possível se conectar com os modelos de IA temos utilizar uma API. Uma API é uma ponte que permite que dois programas conversem entre si. Para esse sistema foi utlizada a API do Groq.""")

    st.markdown("""
        É como fazer um pedido em um restaurante:
        - Você (o programa) fala com o garçom (a GroqAPI).
        - O garçom leva seu pedido até a cozinha (Groq).
        - A cozinha prepara a comida e o garçom traz de volta. """)
    
    st.markdown(""" Link para o [Groq](https://console.groq.com/home) """)

with st.expander(' Orquestradores Agentes '):
    st.subheader('Aprendendo a Usar o AutoGen')
    st.markdown(""" Os agente precisam ser criados e administrado por um Orquestrador, para esse sistema foi utilizado o AutoGen. O Autogen é uma ferramenta da Microsoft que permite criar agentes de IA que conversam entre si.""")
    st.header(" Exemplo de Código")
    st.code('''
    def criar_agente(nome, funcao, modelo):
        return ConversableAgent(
            name=nome,
            system_message=f"Você é um agente com a função: {funcao}.",
            llm_config={
                "model": modelo,
                "api_key": os.getenv("GROQ_API_KEY"),
                "api_type": "groq",
            }
        )
    ''', language="python")
    st.markdown(""" Link para a documentação do [AutoGen](https://autogenhub.github.io/autogen/docs/tutorial/introduction/). Link para uma [playlist](https://www.youtube.com/watch?v=V2qZ_lgxTzg&list=PLp9pLaqAQbY2vUjGEVgz8yAOdJlyy3AQb) do autogen. """)

with st.expander(' Streamlit '):
    st.subheader('Aprendendo a Utilizar o Streamlit')
    st.markdown(""" Streamlit é uma ferramenta que permite criar interfaces web (apps) em Python de forma rápida e fácil, sem precisar saber front-end.""")
    st.markdown(""" Comumente usado para:      
    - Visualizar dados.
    - Criar dashboards.
    - Fazer protótipos de IA e machine learning.
            """)
    st.markdown(""" Link para a documentação do [Streamlit](https://docs.streamlit.io/). 
                Link para um [vídeo](https://www.youtube.com/watch?v=NsjA-c8596k) introdutório sobre Streamlit.""")


st.header("3. Aplicações em Biometria e Estatística")
st.markdown("""
- Automatizar geração e revisão de hipóteses.
- Auxílio na interpretação de resultados estatísticos.
- Interface de apoio para times de pesquisa.
- Possibilidade de simular revisores com vieses diferentes.
""")

st.header("4. Links e Recursos Úteis")
st.markdown("""
- [LangChain](https://www.langchain.com/)
- [Q-learning e Bellman Equation explicada](https://www.geeksforgeeks.org/q-learning-in-python/)
""")

st_lottie(animacao)