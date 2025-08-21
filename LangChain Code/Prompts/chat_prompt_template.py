from langchain_openai import chat_models
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

chat_temp = ChatPromptTemplate([
    ('system', 'you are an {domain} expert'),
    ('human', 'write in easy words about {topic}')
])

prompt = chat_temp.invoke({'domain': 'sports', 'topic': 'football'})

print(prompt)
