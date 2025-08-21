from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key theme discussed in the review")
    summary: str = Field(description="Write the summary of the review")
    sentiment: Literal ["pos", "neg", "neu"] = Field(description="Return the sentiment of the review either prositive, negative or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write the pros from the review")
    cons: Optional[list[str]] = Field(default=None, description="Write the cons from the review")

struct = model.with_structured_output(Review)

result = struct.invoke('After two weeks with the device, I can say the performance is impressive for the price point. Multitasking is smooth, the display is vibrant even under sunlight, and the camera handles low-light surprisingly well. I did notice some minor heating during extended gaming, but nothing too concerning. Battery life easily gets me through the day with moderate use. Overall, a well-balanced phone with premium features where it counts.')

print(result.summary)