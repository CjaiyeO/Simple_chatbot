import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "What is neural network"}])
print(completion.choices[0].message.content)