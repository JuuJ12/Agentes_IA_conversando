import streamlit as st
import streamlit.components.v1 as comp
from streamlit_lottie import st_lottie
import json
import requests


def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json

st.title('Sobre Mim')
def formulario():
    col1,col2= st.columns([0.8,0.2], vertical_alignment='center')
    with col1:
        st.title('Escreva Sua Mensagem')
    with col2:
        comp.iframe("https://lottie.host/embed/0df7f51e-1a62-49e0-a831-e3606d1596c4/aNzoWwzTIq.lottie")
    formulario_de_contato = """
        <form action="https://formsubmit.co/juliovitortb99@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder ="Seu Nome" required>
        <input type="email" name="email" placeholder="Seu Email">
        <textarea name="message" placeholder="Escreva Sua Mensagem"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(formulario_de_contato, unsafe_allow_html=True)
    
def perfil():

    animacao1= load_lottiefile('pictures/animacao_1.json')

    col1,col2=st.columns([0.6,0.9], gap='small',vertical_alignment='center')

    with col1:
        st.image('pictures/perfil_foto.png', caption='Julio Vitor dos Santos')
        

    with col2:
            st_lottie(animacao1)
            st.write(''' 
                        - Técnico em Análise e Desenvolvimento de Sistemas.
                        - Cursando Bacharelado em Sistemas de Informação.
                     
                    ''')
                

    st.write("________________________________________________________________________")

    st.title("Experiências")

    col3,col4= st.columns([0.6,0.9], gap='small',vertical_alignment='center')
    with col3:

        animacao2= load_lottiefile('pictures/animacao_2.json')
        st_lottie(animacao2)
        
    with col4:

        st.write('''
                   - Análise e mineração de dados em bases diversas, como aquelas envolvendo filmes e séries, e dados médicos de pacientes com problemas cardíacos.
                  _____________________________________________________________________
                   - Aplicação modelos de Machine Learning para recomendações de filmes e séries, bem como para a previsão de doenças cardíacas.
                 _____________________________________________________________________
                   - Desenvolvimento de sistemas web utilizando o framework Streamlit, criando interfaces para operações CRUD.
                 _____________________________________________________________________
                   - Desenvolvimento de sistemas web utilizando o framework Streamlit, criando interfaces gráficas interativas para visualização de dados.
                 _____________________________________________________________________
                   - Criação de Agentes de AI para resolução de Problemas.
                 _____________________________________________________________________
                   - Modelagem de Banco de Dados.
                                                                          
                   ''')
    st.write("________________________________________________________________________")    
    col5,col6= st.columns([0.6,1], gap='small',vertical_alignment='center')    
    with col5:
        
        st.title("Certificados")
        animacao3= load_lottiefile('pictures/animacao_3.json')
        st_lottie(animacao3)

    with col6:
         
         st.write('''
                            - AWS Academy Graduate - AWS Academy Cloud Foundations.
                            _____________________________________________________________________
                            - AWS Academy Graduate - AWS Academy Machine Learning Foundations.
                            _____________________________________________________________________
                            - AWS Academy Graduate - AWS Academy Cloud Web Application Builder.
                            _____________________________________________________________________
                            - Programa Ganhe o Mundo(Idioma Inglês) - Nível Básico 1 e 2.
                            _____________________________________________________________________
                            - Programa Ganhe o Mundo(Idioma Inglês) - Nível Pré-Intermediário e Intermediário.
                            ''')
    st.write("________________________________________________________________________") 
    retangulo_com_titulo = """
            <style>
                .retangulo {
                    background-color: #E0FFFF;
                    padding: 20px;
                    border-radius: 8px;
                    text-align: center;
                }
                .titulo {
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 20px;
                    color: #333;
                }
                .icones-container {
                    overflow-x: auto;
                    white-space: nowrap;
                    padding-bottom: 10px;
                }
                .icones-container::-webkit-scrollbar {
                    height: 8px; /* Altura da barra de rolagem */
                }
                .icones-container::-webkit-scrollbar-thumb {
                    background-color: #007BFF; /* Cor da barra de rolagem */
                    border-radius: 4px; /* Arredondamento da barra */
                }
                .icones-container::-webkit-scrollbar-track {
                    background-color: #333; /* Cor do trilho */
                    border-radius: 4px;
                }
                .icones {
                    display: inline-flex;
                    justify-content: flex-start;
                    align-items: center;
                    gap: 25px; /* Aumentando o espaçamento entre os ícones */
                }
                .icones img {
                    display: inline-block;
                    width: 65px;
                    height: 65px;
                }
                .ai-icon {
                    display: inline-block;
                    width: 500px; /* Largura aumentada */
                    height: 100px; /* Altura aumentada */
                    background-color: #007BFF; /* Fundo azul */
                    color: white; /* Cor do texto */
                    font-size: 30px; /* Tamanho da fonte */
                    font-weight: bold; /* Texto em negrito */
                    text-align: center; /* Texto centralizado */
                    line-height: 90px; /* Alinhamento vertical */
                    border-radius: 50%; /* Ícone circular */
                }
            </style>

            <div class="retangulo">
                <div class="titulo">Tecnologias</div>
                <div class="icones-container">
                    <div class="icones">
                        <div class="ai-icon">AI</div>
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-plain-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/plotly/plotly-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-plain-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original-wordmark.svg" />
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original-wordmark.svg" />
                    </div>
                </div>
            </div>
        """
    st.markdown(retangulo_com_titulo, unsafe_allow_html=True)


    st.markdown("""
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
        """, unsafe_allow_html=True)

    st.markdown("""
            <link href="https://cdn.jsdelivr.net/npm/devicon@2.14.0/devicon.min.css" rel="stylesheet">
        """, unsafe_allow_html=True)

    button = st.button(":e-mail: Entre em Contato")
    if button:
        formulario()


def ler_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def build_page_me():
    perfil() 
    ler_css("style/formulario.css")

build_page_me()
