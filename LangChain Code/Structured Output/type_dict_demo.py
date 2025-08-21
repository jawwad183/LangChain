from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key theme discussed in the review"]
    summary: Annotated[str, "Write the summary of the review"]
    sentiment: Annotated[str, "Return the sentiment of the review either prositive, negative or neutral"]
    pros: Annotated[list[str], "Write the pros from the review"]
    cons: Annotated[list[str], "Write the cons from the review"]

struct = model.with_structured_output(Review)

result = struct.invoke('After two weeks with the device, I can say the performance is impressive for the price point. Multitasking is smooth, the display is vibrant even under sunlight, and the camera handles low-light surprisingly well. I did notice some minor heating during extended gaming, but nothing too concerning. Battery life easily gets me through the day with moderate use. Overall, a well-balanced phone with premium features where it counts.')

print(result)
print(result['summary'])
print(result['sentiment'])
print(result['key_themes'])
print(result['pros'])
print(result['cons'])