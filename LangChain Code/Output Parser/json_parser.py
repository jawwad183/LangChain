from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= 'google/gemma-2-2b-it',
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm, max_output_tokens=10)

parser = JsonOutputParser()

temp = PromptTemplate(
    template= 'Give me name, age, city of a fiction person {input_format}',
    input_variables=[],
    partial_variables={'input_format': parser.get_format_instructions()}
)

prompt = temp.format()

result = model.invoke(prompt)

parsed_result = parser.parse(result.content)

print(parsed_result)
print(type(parsed_result))
