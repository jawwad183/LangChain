from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import Field, BaseModel
from typing import Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= 'google/gemma-2-2b-it',
    task = 'text-generation'
)

model1 = ChatHuggingFace(llm=llm)

class Review(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Return the review sentiment as positive or negative.")

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Review)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

sentiment_chain = prompt1 | model1 | parser2

conditional_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model1 | parser1),
    (lambda x:x.sentiment=='negative', prompt3 | model1 | parser1),
    (RunnableLambda(lambda x: "could not find sentiment"))
)

chain = sentiment_chain | conditional_chain

result = chain.invoke({'feedback': 'This is a beautiful phone'})

print(result)











