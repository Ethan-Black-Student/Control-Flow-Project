#print("hello world")

from openai import OpenAI

OPEN_AI_KEY = "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"

print("Welcome")
print("Let's ask ChatGPT something within our code:")
question = str(input("You wake up in a cold dark school, what do you wanna do? "))

client = OpenAI(api_key=OPEN_AI_KEY)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "You are a dnd like gamemaster, narrating what the outcomes of choices are in only a short sentance, be creative anything is on the table and make sure you leave room for a next action!"},
    {"role": "user", "content": question}
  ]
)
print(completion.choices[0].message.content)