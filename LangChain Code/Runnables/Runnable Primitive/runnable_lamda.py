from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables=['topic']
)

model  = ChatOpenAI()

parser = StrOutputParser()

def word_count(text):
    return len(text.split())

prompt2 = PromptTemplate(
    template="Write the explanation of the joke {text} in 50 characters",
    input_variables=['text']
)
joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_chain,parallel_chain)

result = final_chain.invoke({'topic':'scholarship'})

print(result['joke'])
print(result['word_count'])