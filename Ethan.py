#print("hello world")
import time

from openai import OpenAI

"""

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

response = (completion.choices[0].message.content)
print(response)

"""

print()
print("Welcome to ze stori game")
print()

time.sleep (1.5)

print("You wake up in an abandomed mental hospital, and your only goal is to survive the night!")

time.sleep (1.5)

print("Investigate soroundings (i) or go back to bed (b)")

time.sleep (1.5)

choice = input("What do you wanna do? ").strip().lower()

while choice != "i":

  if choice == "b":

    print("Once again, you wake up in an abandomed mental hospital, and your only goal is to survive the night!")

    time.sleep (1.5)

    print("Investigate soroundings (i) or go back to bed (b)")

    time.sleep (1.5)

    choice = input("What do you wanna do? ").strip().lower()

  else:

    print("Seriosly now, you wake up in an abandomed mental hospital, and your only goal is to survive the night!")

    time.sleep (1.5)

    print("Investigate soroundings (i) or go back to bed (b)")

    time.sleep (1.5)

    choice = input("What do you wanna do? ").strip().lower()


print ("yayyy")