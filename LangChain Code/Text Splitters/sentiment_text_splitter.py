from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

splitter = SemanticChunker(
    OpenAIEmbeddings(),breakpoint_threshold_type='standard_deviation',breakpoint_threshold_amount=1
)

text = """The bustling city street was a symphony of sounds: car horns blared, vendors called out their wares, and the chatter of pedestrians created a constant hum. Amidst the chaos, a street artist meticulously painted a vibrant mural on a brick wall, bringing a splash of color to the otherwise gray urban landscape. The scent of roasted peanuts mingled with exhaust fumes, a strange but familiar perfume of city life. Meanwhile, in a quiet suburban garden, a hummingbird hovered near a bright red feeder, its wings a blur of motion as it sipped nectar. The gentle rustle of leaves was the only sound, a stark contrast to the clamor of the city.

The concept of a black hole continues to fascinate and challenge our understanding of physics. These cosmic phenomena are regions in spacetime where gravity is so strong that nothing—not even light—can escape. Formed from the collapse of massive stars at the end of their lives, their immense density and gravitational pull warp the fabric of spacetime around them."""

docs = splitter.create_documents([text])
print(len(docs))
print(docs)