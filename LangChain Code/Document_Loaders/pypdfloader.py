from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Bitcoin-lightning-network.pdf')

docs = loader.load()

print(docs[2])