from openai import OpenAI

import time

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

          fortify = input("Do you leave the room to check out the noise (c) or do you hide in the corner(h) ").strip().lower()
              
        if fortify == "c":

          explore = "e"
          
        else:

          print()
          fortify = input("Ok buddy do you leave the room to check out the noise (c) or do you hide in the corner(h) ").strip().lower()

      if fortify == "c":

        explore = "e"

    else:

      print()
      print('Hurry up you do mot have all day. Do you fortify your room (f) or go out and explore (e)')
      print()

      explore = input("Whats your next move ").strip().lower()

print("yayyyy")
