from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """The sun dipped below the horizon, painting the sky in fiery hues of orange and purple. A cool breeze swept through the fields, carrying the scent of cut grass. Crickets began their nightly chorus, a gentle serenade to the fading light. Stars emerged, one by one, a diamond-studded canvas unfolding above."""

loader = PyPDFLoader('Bitcoin-lightning-network.pdf')

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

docs = loader.load()
result = splitter.split_documents(docs)

print(result[0].page_content)