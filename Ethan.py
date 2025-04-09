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
# Introduction

print()
print("Welcome to ze stori game")
print()

time.sleep (1.5)

print("You wake up in an abandomed mental hospital, and your only goal is to survive the night!")

time.sleep (1.5)

# Investigate or stay in bed choice

print("Investigate soroundings (i) or go back to bed (b)")

time.sleep (1.5)

print()
choice = input("What do you wanna do? ").strip().lower()
print()

# choice indentier

while choice != "i":

  if choice == "b":

    print("Once again, you wake up in an abandomed mental hospital, and your only goal is to survive the night!")

    time.sleep (1.5)

    print("Investigate soroundings (i) or go back to bed (b)")

    time.sleep (1.5)

    print()
    choice = input("What do you wanna do? ").strip().lower()

  else:

    print("Seriosly now, you wake up in an abandomed mental hospital, and your only goal is to survive the night!")

    time.sleep (1.5)

    print("Investigate soroundings (i) or go back to bed (b)")

    time.sleep (1.5)

    print()
    choice = input("What do you wanna do? ").strip().lower()

OPEN_AI_KEY = "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"

print()
print("You spot a phone resting on your side table, but as you start to reach for it, it starts to ring -- someone is calling! Now is your chance to find out whats really going on, but the phone is almost dead!!")
print()
question = str(input(""))
print()

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

print()
question = str(input(""))
print()

client = OpenAI(api_key=OPEN_AI_KEY)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "you are calling somone inside a mental hospital, there has been an attack and a mysterious creature is inside, the hospital is now abandonded. but the person your calling does not know that. leave sutle hint about thier situation but keep it consice, and make sure they are quiet as the creature is close, and they are in danger. only anwser questions, and try to keep it vauge. btw you have already been talking for a while, your in the middle of the converataion rn."},
    {"role": "user", "content": question}
  ]
)

response = (completion.choices[0].message.content)
print(response)

print()
question = str(input(""))
print()

client = OpenAI(api_key=OPEN_AI_KEY)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "you are calling somone inside a mental hospital, there has been an attack and a mysterious creature is inside, the hospital is now abandonded. but the person your calling does not know that. leave sutle hint about thier situation but keep it consice, and make sure they are quiet as the creature is close, and they are in danger. only anwser questions, and try to keep it vauge. try to end off the conversation as the phone is going to cut off right after. btw you have already been talking for a while, your in the middle of the converataion rn."},
    {"role": "user", "content": question}
  ]
)

response = (completion.choices[0].message.content)
print(response)

print()
print("The phone has died")
print()
print('Do you fortify your room (f) or go out and explore (l)')
print()
choice = input("Whats your next move ").strip().lower()

#this is a while loop if you go down the wrong path
while choice !="l":
  
  if choice=="f":

    print()
    print("You decide to barricade the doors and hide. After a while you hear a loud banging Down the hall")
    print()

    choice = input("Do you leave the room to check out the noise (c) or do you Hide in the corner(h)").strip().lower()
    
    #While loop to prevent incorrect inputs
    while choice != "c":
    
      if choice =="h":
        print()
        print ("The noise get louder then stops abruptly followed by the sounds of faint murmur")
        print()
        #ADD GAME RIGHT HERE

        choice = input("Do you leave the room to check out the noise (c) or do you Hide in the corner(h)").strip().lower()

      else:
        print()
        choice = input("Ok buddy do you leave the room to check out the noise (c) or do you Hide in the corner(h)").strip().lower()
        print()

    if choice =="c":
      choice = "l"

  else:
    print('Hurry up you do mot have all day. Do you fortify your room (f) or go out and explore (l)')
    choice=input("Whats your next move ").strip().lower()

#If you choose to leave the room
if choice == "l":
  
  print()
  print("You step outside into a hallway filled with flickering lights and smashed glass")
  print()

#while loop to choose left or right
while choice != "r":
  print()
  choice=input("Do you head left (l) or right (r)").strip().lower()
  print()


#If you keep going down the wrong path this is the code for that
  if choice=="l":

    print()
    print ("as you start walking, the banging gets far louder, you start to question what you might find")
    print()

    #While loop  choice that keeps the choice from breaking from incorrect inputs
    while choice != "r":
      
      Choice2=input("Do you keep on walking(w) or do you turn around(t)").strip().lower()

      if Choice2=="w":

        print("You didn't think it possible but the banging gets louder")
        #Another game

      if Choice2=="t":
        choice = "r"

      else:

        print("that was not an option")
