from openai import OpenAI

import time


#Choice to fortify room
print()
print('Do you fortify your room (f) or go out and explore (l)')
print()

choice = input("Whats your next move ").strip().lower()

#this and while loop if you go down the wrong path
while choice !="l":
  if choice=="f":
    print("You decide to barricade the doors and hide. After a while you hear a loud banging Down the hall")

    choice = input("Do you leave the room to check out the noise (c) or do you Hide in the corner(h)").strip().lower()
  
    while choice =="h":
      print ("The noise get louder then stops abruptly followed by the sounds of faint murmur")
      #ADD GAME RIGHT HERE

    while choice =="c":
      choice = "l"

  else:
    print('Do you fortify your room (f) or go out and explore (l)')
    choice=input("Whats your next move ").strip().lower()

#If you choose to leave the room
if choice == "l":
  
  print("You step outside into a hallway filled with flickering lights and smashed glass")

#Hallway choice
  print()
  Choice=input("Do you head left (l) or right (r)").strip().lower()
  print()

"""

#If you keep going down the wrong path this is the code for that
if Choice=="l":
  print ("as you start walking, the banging gets far louder, you start to question what you might find")
  print()
  Choice2=input("Do you keep on walking(w) or do you turn around(t)").strip().lower()
  if Choice2=="w":
    print("You didn't think it possible but rthe banging gets louder")
    #Another game

#This is if you go the right way or turn back
if Choice== "r" or Choice2=="t":
 Choice=input("As you walk along the hallway you stop three rooms. a lab (l), a storage room (s) and a patient room (p). which room would you like to enter").strip().lower()

"""

