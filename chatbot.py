import openai

#before runing enter your api key
openai.api_key = "sk-"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "What is neural network"}])
print(completion.choices[0].message.content)
