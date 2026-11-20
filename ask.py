from dotenv import load_dotenv
import anthropic

load_dotenv()  # loads your key from .env

client = anthropic.Anthropic()

question = "In two sentences, what is the EU AI Act?"

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=500,
    messages=[{"role": "user", "content": question}],
)

print(response.content[0].text)