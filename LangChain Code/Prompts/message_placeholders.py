
from langchain_core.prompts import ChatPromptTemplate


chat_temp = ChatPromptTemplate([
    ('system', 'you are an customer support agent'),
    ('human', '{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines()) 

print(chat_history)
prompt = chat_temp.invoke({'chat_history': chat_history, 'query': 'When I will get my refund?'})

print(prompt)
