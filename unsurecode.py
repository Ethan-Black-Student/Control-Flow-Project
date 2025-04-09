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

#If you havent won it will keep reapting this part with a while loop