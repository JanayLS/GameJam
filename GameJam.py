from beginner import friend2



def clues(one,two,three,four):
      print("You can look: ")
      print("\n1) behind the mirror on your right")
      print("\n2) under the door mat")
      print(f"\n3) check {friend2}'s pocket")
      print("\n4) check your own pocket")
      clue=int(input("\n\nWhere do you want to check first? Enter the digit: "))
      print("\n")

      if clue == 4:
            print("You have a slip of paper in your pocket.")
            print("On the paper is this riddle: ")
            print("\n\nI am the key to a secret door,\n",
                  "Four numbers hold the code, nothing more.\n",
                  "In sequence they stand, easy to see,\n",
                  "Unlock the mystery, and you'll be free.\n")
            print(f"\n\n\nCode:{one,two,three,four}")
      while clue != 4:
            print("You don't find anything there.")
            clue = int(input("\n\nWhere do you want to check first? Enter the digit: "))


