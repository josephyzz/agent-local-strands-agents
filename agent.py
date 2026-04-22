import logging

from strands import Agent
from strands.models.ollama import OllamaModel

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
agent = Agent(model=qwen_model, tools=[])

agent('Que dia é hoje e quando será daqui a 5 dias?')
