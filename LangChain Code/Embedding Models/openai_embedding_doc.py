from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
doc = [
    "Islamabad is the capital of Pakistan.",
    "Lahore is the capital of Punjab",
    "Karachi is the capital of Sindh"
]
result = model.embed_documents(doc)
print(str(result))