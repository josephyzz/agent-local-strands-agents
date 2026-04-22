import logging

from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator, file_read
from utils import change_language_voice, get_user_current_day_time, speak

# Enables Strands debug log level
logging.getLogger('strands').setLevel(logging.DEBUG)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format='%(levelname)s | %(name)s | %(message)s',
    handlers=[logging.StreamHandler()],
)

qwen_model = OllamaModel(
    host='http://localhost:11434',  # Ollama server address
    model_id='qwen2.5:0.5b',  # Specify which model to use
)


# inicia o agente
agent = Agent(
    model=qwen_model,
    tools=[
        change_language_voice,
        calculator,
        file_read,
        get_user_current_day_time,
    ],
)
response = agent(
    'could you change the language to portuguese and tell me the current date and time?'
)
speak(str(response))
