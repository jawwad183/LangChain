from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use the correct parameter name
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

# Invoke the LLM
result = llm.invoke("What is the QS ranking of KFUPM?")

print(result)
