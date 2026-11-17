
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

prompt = input("Enter your prompt: ")

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=100
)

print("Generated Text:")
print(response.choices[0].text.strip())
