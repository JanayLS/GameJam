from Draft_1 import *
import random
from beginner import friend2
from janay import *



def split_up():
#after the user chooses to split up, they confront a mirror maze
      #explains setting
      print(f"You and {friend2} decide to buddy up.\nAs you walk, you come up to the entrance to an older, battered building.",)
      print(f"\nYou and {friend2} enter the building.\n")
      print("You are surrounded by mirrors. A mirror maze.")
      print("The only light in the building is coming from a lightbulbs")
      print(f"Both you and {friend2} carefully move through the maze.")
      print(f"Suddenly, a mirror mysteriously combusts causing {friend2} to get seriously injured. ")


      #use of an if statement: if they have bandages and they want to use it, the friend lives. Otherwise, the friend dies.
      friend_cut_by_mirror=input(f"{friend2} is seriously hurt, will you use bandages to heal their wounds?").lower()
      if "bandages" in purchased_items and purchased_items >= 1:
            print('INVENTORY')
            print("-----------------------")
            printed = []
            for i in purchased_items:
                  if i in printed:
                        continue
                  else:
                        print(f'{i}:{purchased_items.count(i)}')
                        printed.append(i)
            if friend_cut_by_mirror == "yes" or friend_cut_by_mirror == "y":
                  print("You have used 1 of your bandages.")
                  print(f"You have {purchased_items} bandages left.")
                  friend_alive=True
            elif friend_cut_by_mirror == "no" or friend_cut_by_mirror == "n":
                  print(f"You decided not to use your bandages.\n{friend2} dies.")
                  friend_alive=False
      else:
            print(f"You don't have any bandages to use.\n{friend2} dies.")
            friend_alive=False

      print("As you continue on, you stumble across a door.","\nThe door is locked.")
      print("The door needs a passcode to enter consisting of 4 digits.")
      print("Maybe there are some clues hidden around.")
      digits = [0, 1, 2, 3, 4, 5, 6, 7, 8]
      digit1 = random.choice(digits)
      digit2 = random.choice(digits)
      digit3 = random.choice(digits)
      digit4 = random.choice(digits)
      clues(digit1,digit2,digit3,digit4)
      luck = randomness()
      if luck == True:
            print("You enter the code.")
            print("Code was successful. You were able to escape.")
      while luck == False:
            print("You enter the code.")
            print("You accidentally input the wrong code. The code reset. You now have to find the new code.")
            clues(digit1,digit2,digit3,digit4)
            luck = randomness()
            if luck == True:
                  print("You enter the code.")
                  print("Code was successful. You were able to escape.")

