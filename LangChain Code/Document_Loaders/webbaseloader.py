from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

user_agent = os.getenv("USER_AGENT")

url = 'https://jawad.dev-drift.com/'

loader = WebBaseLoader(url, requests_kwargs={"headers": {"User-Agent": user_agent}})

docs = loader.load()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="write the asnwer of the \n {question} from the following \n {text}",
    input_variables=['question','text']
)

parser = StrOutputParser()

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question':'What services this developer provide?','text':docs[0]})

print(result)