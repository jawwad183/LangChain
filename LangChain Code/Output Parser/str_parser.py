from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

temp1 = PromptTemplate(
    template= 'Write content on the following {topic}',
    input_variables= ['topic']
)


temp2 = PromptTemplate(
    template= 'Write a 5 line summary on the following {text}',
    input_variables= ['text']
)

parser = StrOutputParser()

# First chain: topic → content
chain1 = temp1 | model | parser

# Second chain: content → summary
chain2 = temp2 | model | parser

# Run chain1 first
content = chain1.invoke({'topic': 'Cricket'})

# Then pass result to chain2
summary = chain2.invoke({'text': content})

print("Generated Content:\n", content)
print("\nSummary:\n", summary)