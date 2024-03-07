from gasstation import *

def hp_checker(hp,bandage):
    if hp <= 2 and bandage >= 1:
        print("you start are feeling the affects of all your injuries.")
        hp_input = input("would you like to use bandages?(yes or no)")
        if hp_input == 'yes':
            hp = 10
            print(hp)
        elif hp_input == 'no':
            print("womp womp you dumb arnt you")
    elif hp <= 2:
        print("you are feeling the affects of all your injuries better find bandages")


