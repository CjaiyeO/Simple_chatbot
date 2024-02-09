import openai

#before runing enter your api key
openai.api_key = "sk-"

question = input("How can I help you today?\n")

response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt=question,
    temperature=0.7,       # Decides the randomness ranges from 0-1 (low = logical response; high = creative response)
    max_tokens=150         # Max number of words in your response
)
print(response.choices[0].text.strip())

