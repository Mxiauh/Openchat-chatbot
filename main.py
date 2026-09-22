from ollama import chat

prompt = input("Enter your prompt: ")

response = chat(
    model='gemma3:latest',
    messages=[{'role': 'user', 'content': prompt}],
)
print(response.message.content)