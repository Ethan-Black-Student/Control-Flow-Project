import time

from openai import OpenAI



print()
print("Welcome to ze stori game")
print()

time.sleep (1.5)

print("You wake up in an abandomed mental hospital, and your only goal is to survive the night!")

time.sleep (1.5)

print("Investigate soroundings (i) or go back to bed (b)")

time.sleep (1.5)

choice = input("What do you wanna do? ").strip().lower()

if choice == "b":
    
  while choice == "b":

    print("Once again, you wake up in an abandomed mental hospital, and your only goal is to survive the night!")

    time.sleep (1.5)

    print("Investigate soroundings (i) or go back to bed (b)")

    time.sleep (1.5)

    choice = input("What do you wanna do? ").strip().lower()

else:
    
  print("")



print('Do you fortify your room (F) or go out and explore (L)')

choice = input("Whats your next move ").strip().lower()

if choice=="f":
  
  print("You decide to barricade the doors and hide. After a while you hear a loud banging Down the hall")

  choice2=input("Do you leave the room to check out the noise(C) or do you Hide in the corner(H)").strip().lower()
  
  while choice2 =="h":
    print ("The noise get louder then stops abruptly followed by the sounds of faint murmur")
    #ADD GAME RIGHT HERE

if choice == "l" or choice2 or "c":
  
  print("You step outside into a hallway filled with flickering lights and smashed glass")