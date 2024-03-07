import draft_Lali
import GameJam_Idris
def intro():
      #ask user for name
      users_name=input("Hey, what's your name?: ")
      #welcoming user and describing setting
      print(f"Welcome {users_name}! \nYou are at currently at the train station. "
            f"\nYou have 15 min before you're train arrives. "
            f"\nThe train you're about to take is headed for Bloomsbury Park, NC. ")
      #while the variable "begin" = "yes", game will play, entering "no" will end the game
      begin=input("\n\nAre you ready to begin? y/n:  ").lower()
      while begin == "y" or begin == "yes":
            pass
      if begin == "n" or "no":
            print("You exited the game. Goodbye.")
#after the user chooses to split up, they confront a mirror maze
if "variable for users choice on splitting up or going as a group" == "yes":
      #explains setting
      print(f"You and {GameJam_Idris.friend2} decide to buddy up.")
      print("As you walk, you come up to the entrance to an older, battered building.")
      print(f"You and {GameJam_Idris.friend2} enter the building.\n")
      print("You are surrounded by mirrors. A mirror maze.")
      print("The only light in the building is coming from a lightbulbs")
      print(f"Both you and {GameJam_Idris.friend2} carefully move through the maze.")
      print(f"Suddenly, a mirror mysteriously combusts causing {GameJam_Idris.friend2} to get seriously injured. ")
      #use of an if statement: if they have bandages and they want to use it, the friend lives. Otherwise, the friend dies.
      friend_cut_by_mirror=input(f"{GameJam_Idris.friend2} is seriously hurt, will you use bandages to heal their wounds?").lower()
      if draft_Lali.bandages >= 1:
            if friend_cut_by_mirror == "yes" or friend_cut_by_mirror == "y":
                  print("You have used 1 of your bandages.")
                  print(f"You have {draft_Lali.bandages} bandages left.")
                  friend_alive=True
            elif friend_cut_by_mirror == "no" or friend_cut_by_mirror == "n":
                  print(f"You decided not to use your bandages.\n{GameJam_Idris.friend2} dies.")
                  friend_alive=False
      else:
            print(f"You don't have any bandages to use.\n{GameJam_Idris.friend2} dies.")
            

