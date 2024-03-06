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