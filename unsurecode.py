from openai import OpenAI

import time

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
