import os
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv()



student_agent = ConversableAgent(
    name="agente_estudante",
    system_message="Você é um estudante de música disposto a aprender.",
    llm_config={
        "model": "llama3.1:latest",
        "base_url": "http://127.0.0.1:11434/v1",
        "api_key": "ollama",
        "temperature":2
    },
)

teacher_agent = ConversableAgent(
    name="agente_professor",
    system_message="Você é um professor de música disposto a ensinar.",
    llm_config={
        "model": "llama3-70b-8192",
        #"base_url": 'https://api.groq.com/openai/v1',  
        "api_key": os.getenv("GROQ_API_KEY"),
        "api_type": "groq",
        "temperature":1  
    },
)

teacher_agent = ConversableAgent(
    name="agente_professor",
    system_message="Você é um professor de música disposto a ensinar.",
    llm_config={
        "model": "llama3.1:latest",
        "base_url": "http://127.0.0.1:11434/v1",  
        "api_key": "ollama",
        "temperature":1  
    },
)

chat_result = student_agent.initiate_chat(
    teacher_agent,
    message="Me ensine os fundamentos da música como se estivesse explicando para uma criança?",
    max_turns=2
)