from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="write a 50 character summmary on {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': docs[0].page_content})

print(result)