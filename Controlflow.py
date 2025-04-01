#print("hello world")

from openai import OpenAI

import time

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

OPEN_AI_KEY = "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"

print("You spot a phone resting on your side table, but as you start to reach for it, it starts to ring -- someone is calling! Now is your chance to find out whats really going on, but the phone is almost dead!!")
question = str(input(""))

client = OpenAI(api_key=OPEN_AI_KEY)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "you are calling somone inside a mental hospital, there has been an attack and a mysterious creature is inside, the hospital is now abandonded. but the person your calling does not know that. leave sutle hint about thier situation but keep it consice, and make sure they are quiet as the creature is close, and they are in danger. only anwser questions, and try to keep it vauge."},
    {"role": "user", "content": question}
  ]
)

response = (completion.choices[0].message.content)
print(response)

question = str(input(""))

client = OpenAI(api_key=OPEN_AI_KEY)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "you are calling somone inside a mental hospital, there has been an attack and a mysterious creature is inside, the hospital is now abandonded. but the person your calling does not know that. leave sutle hint about thier situation but keep it consice, and make sure they are quiet as the creature is close, and they are in danger. only anwser questions, and try to keep it vauge."},
    {"role": "user", "content": question}
  ]
)

response = (completion.choices[0].message.content)
print(response)

question = str(input(""))

client = OpenAI(api_key=OPEN_AI_KEY)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "you are calling somone inside a mental hospital, there has been an attack and a mysterious creature is inside, the hospital is now abandonded. but the person your calling does not know that. leave sutle hint about thier situation but keep it consice, and make sure they are quiet as the creature is close, and they are in danger. only anwser questions, and try to keep it vauge. try to end offf the conversation as the phone is going to cut off right after. try to continue the convo"},
    {"role": "user", "content": question}
  ]
)

response = (completion.choices[0].message.content)
print(response)

print()
print("The phone has died")

print()
print('Do you fortify your room (F) or go out and explore (L)')
print()

choice = input("Whats your next move ").strip().lower()

if choice=="f":
  
  print("You decide to barricade the doors and hide. After a while you hear a loud banging Down the hall")

  choice2=input("Do you leave the room to check out the noise(C) or do you Hide in the corner(H)").strip().lower()
  
  while choice2 =="h":
    print ("The noise get louder then stops abruptly followed by the sounds of faint murmur")
    #ADD GAME RIGHT HERE

if choice == "l" or choice2 or "c":
  
  print("You step outside into a hallway filled with flickering lights and smashed glass")