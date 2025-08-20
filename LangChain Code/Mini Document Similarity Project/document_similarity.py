from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
documents = [
    "Python is a popular programming language known for its simplicity and versatility in data science, AI, and web development.",
    "Elon Musk is an entrepreneur famous for leading companies like Tesla and SpaceX, focusing on innovation and space exploration.",
    "The Great Wall of China is an ancient structure built for protection, and it remains one of the greatest wonders of the world.",
    "The African Elephant is the largest land animal, known for its intelligence, memory, and strong social bonds.",
    "Pizza is an Italian dish that has become popular worldwide, loved for its variety of toppings and flavors."
]

query = "Which language is used for data science?"

doc_embedding = model.embed_documents(documents)
query_embedding = model.embed_query(query)

score = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted(list(enumerate(score)), key = lambda x:x[1])[-1]

print(documents[index])
print("Similarity score is: ", score)