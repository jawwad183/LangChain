from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

# temperature is a parameter that controls the randomness of a language model’s output. 
# It affects how creative or deterministic the responses are.
#
# Lower values (0.0 – 0.3) → More deterministic and predictable.
# Higher values (0.7 – 1.0 or up to 2.0) → More random, creative, and diverse.


model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke('What is the QS ranking of KFUPM?')

print(result.content)