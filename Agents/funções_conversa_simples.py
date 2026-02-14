import os
from autogen import ConversableAgent
from dotenv import load_dotenv


load_dotenv()
# Configurações iniciais

def criando_agentes(idioma : str, função :str, nome: str) -> tuple:

    agente = ConversableAgent(
        name= nome,
        system_message=(f'Você vai responder sempre no idioma {idioma} e será {função}'),
        llm_config={
            "model": "groq/compund",
            
            "api_key": os.getenv("GROQ_API_KEY"),
            "api_type": "groq",
            "temperature":1
        },
    )

    return agente


def chat(agente1,agente2,assunto, turnos):
        chat_result = agente1.initiate_chat(
            agente2,
            message=assunto,
            max_turns=turnos
        )
        return chat_result
