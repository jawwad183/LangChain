from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= 'google/gemma-2-2b-it',
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description="Fact 1 about the topic"),
    ResponseSchema(name='fact_2', description="Fact 2 about the topic"),
    ResponseSchema(name='fact_3', description="Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

temp = PromptTemplate(
    template= "Give me the name, age, and city of {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = temp.invoke({'topic': 'Politician'})
result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)