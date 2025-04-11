
import threading

import time

from openai import OpenAI

winner = "no"

def game():

  print()
  print("Welcome to ze stori game")

  time.sleep (1.5)

  print()
  print("You wake up in an abandomed mental hospital, and your only goal is to survive the night!")

  time.sleep (1.5)

  # Investigate or stay in bed choice
  
  print()
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

      print()
      print("Investigate soroundings (i) or go back to bed (b)")
      print()

      time.sleep (1.5)

      choice = input("What do you wanna do? ").strip().lower()
      print()

    else:

      print("Seriosly now, you wake up in an abandomed mental hospital, and your only goal is to survive the night!")

      time.sleep (1.5)

      print()
      print("Investigate soroundings (i) or go back to bed (b)")

      time.sleep (1.5)

      print()
      choice = input("What do you wanna do? ").strip().lower()
      print()

  """

  # ChatGpt conversation start

  OPEN_AI_KEY = "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"

  print()
  print("You spot a phone resting on your side table, but as you start to reach for it, it starts to ring -- someone is calling! Now is your chance to find out whats really going on, but the phone is almost dead!!")
  print()
  question = str(input(""))
  print()

  # ChatGpt first response

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

  # ChatGpt second response

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

  # ChatGpt third response

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

  """

  # Explore vs fortify

  print("Do you fortify your room (f) or go out and explore (e)")
  print()

  explore = input("Whats your next move ").strip().lower()

  while explore != "e":
    
    if explore == "f":

      print()
      print("You decide to barricade the doors and hide. After a while you hear a loud banging in the hall")
      print()

      fortify = input("Do you leave the room to check out the noise (c) or do you hide in the corner (h) ").strip().lower()
          
      while fortify != "c":
          
        if fortify == "h":

          print()
          print ("The noise get louder then stops abruptly, followed by the sounds of faint murmur")
          print()

          fortify = input("Do you leave the room to check out the noise (c) or do you hide in the corner (h) ").strip().lower()
              
        if fortify == "c":

          explore = "e"
          
        else:

          print()
          fortify = input("Ok buddy do you leave the room to check out the noise (c) or do you hide in the corner (h) ").strip().lower()

      if fortify == "c":

        explore = "e"

    else:

      print()
      print("Hurry up you do mot have all day. Do you fortify your room (f) or go out and explore (e)")
      print()

      explore = input("Whats your next move ").strip().lower()
  
  print()
  print("You step outside into a hallway filled with flickering lights and smashed glass")
  move = "l"
  Choice2 = "b"

  #while loop to choose left or right

  while move != "r":

    print()
    move = input("Do you head left (l) or right (r) ").strip().lower()

    #If you keep going down the wrong path this is the code for that

    if move == "l":

      print()
      print("as you start walking, the banging gets far louder, you start to question what you might find")

      #While loop  choice that keeps the choice from breaking from incorrect inputs

      while Choice2 != "t":
        
        print()
        Choice2 = input("Do you keep on walking (w) or do you turn around (t) ").strip().lower()

        if Choice2 == "w":
          
          print()
          print("You didn't think it possible but the banging gets louder")

        if Choice2=="t":
          move = "r"

        elif Choice2 != "w" and Choice2 != "t":

          print()
          print("That was not an option")
  
  if  move == "r":

    print()
    print("As you walk along the hallway, you find three rooms. a lab, a storage room and a patient room.")

  else:

    print()
    print("That was not an option")

  #Matthew codeeee

  global winner
  winner = "yes"

  # Timer code, credit Joey

def timer():
    
    for i in range(120,-1,-10):
        
        print("\n"+str(i))
        
        if i == 0:
            print("you lost")
            exit(0)
        elif winner == "yes":
            print("You win!")
            exit(0)
        else:
            time.sleep(10)

thread1 = threading.Thread(target=game)
thread2 = threading.Thread(target=timer)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

#need to athour code, do read me, input matthew section, get new chatgpt api code.