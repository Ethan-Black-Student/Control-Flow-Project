from openai import OpenAI

import time


#Choice to fortify room
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
if choice== "r":
  win = "false"
while win == "false": 
  choice=input("As you walk along the hallway you stop three rooms. a lab (l), a storage room (s) and a patient room (p). which room would you like to enter ").strip().lower()
 
  if choice=="l":

    print()
    print("You enter a labratory filled with smashed beakers and bubbling liquid flowing all over the floor. At the back is a locked door requiring a four digit code")
    print()

    choice=input("Do you leave the room (l) or input the code (i)")
    if choice != "i":
      if choice== "r":
         win = "false"
      while win == "false": 
        choice=input("As you walk along the hallway you stop three rooms. a lab (l), a storage room (s) and a patient room (p). which room would you like to enter ").strip().lower()
 
      

      
    if choice=="i":
      while exit != "y":

        print("What is the four digit code")
      # The place to input code to escape the while loop to win
      code=input()

      #What the correct code is
      if code=="4379":
        win = "true"
        
      #If you dont input the correct code
      else:
         print("Incorrect code")

        #Allows exit of the Four digit code loop
      exit=input("Do you want to exit the room yes (y) or no (n) ").strip().lower()

    print("Congradulations you have exscpaed outside of the mental hospital, you win for now")

  if choice =="s":
      print()
      print ("you walk into a storage room full of boxes. You notice on the wall written in some sticky red liqiud a four nuber code (4379)")
      print()
      print("You leave the room")
    
  if choice=="p":
    print()
    print("You walk into a room filled with corpses littering the floor. One of them sits up and looks at you. Mabye you should ask it a question")
    print()

    OPEN_AI_KEY="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"

    question = str(input(""))
    print()

    client = OpenAI(api_key=OPEN_AI_KEY)

    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      store=True,
      messages=[
        {"role": "system", "content": "You are a talking corpse with a witty attitude and a cruel sense of humor."},
        {"role": "user", "content": question}
      ]
    )

    response = (completion.choices[0].message.content)
    print(response)
