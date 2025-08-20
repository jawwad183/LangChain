from langchain_huggingface import HuggingFaceEmbeddings

model = HuggingFaceEmbeddings(model = 'sentence-transformers/all-MiniLM-L6-v2')
doc = [
    "Islamabad is the capital of Pakistan.",
    "Lahore is the capital of Punjab",
    "Karachi is the capital of Sindh"
]

result = model.embed_documents(doc)
print(str(result))