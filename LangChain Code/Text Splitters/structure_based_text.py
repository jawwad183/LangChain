from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """The sun dipped below the horizon, painting the sky in fiery hues of orange and purple. A cool breeze swept through the fields, carrying the scent of cut grass. Crickets began their nightly chorus, a gentle serenade to the fading light. Stars emerged, one by one, a diamond-studded canvas unfolding above."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

result = splitter.split_text(text)

print(result)