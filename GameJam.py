from gasstation import *
from hp_checker import *
from teagether import *
bandage=0
hp=10
users_name = input("Hey, what's your name?: ")
friend1 = input("who will be your friend on this journey:")
friend2 = input(" who will be your friend on this journey:")
friend3 = input("who will be your friend on this journey:")
friend4 = input("who will be your friend on this journey:")

print(f"Welcome {users_name}! \nAt 1am you and a few friends take a train to go towards Bloomsbury amusment park "
      f"\nYou hear the conductor say have \"15 min before you're train reaches it destination.\" ")
print(
    f'You, {friend1},{friend2},{friend3},and {friend4} get off the train then leave the train station. Yall begin to walk towards the abandoned Bloomsbury amusment park')
print(f'While walking towards Bloomsbury {friend3} points out a rugged gas station')

gasinput = input("Will you enter the gas station?(yes or no)")
if gasinput == 'yes':
    print("You have entered the gas station with you friends, you suddenly remember you have $50 in your pocket")
    gas_station(options, capital, inventory)
    bandage = purchased_items.count('bandage')

elif gasinput == 'no':
    print(
        f'{friend1} says\"nah that place is creepy af\". \"you actin like we aint going to an abandoned park, rumored to be haunted, you\'re such a p###y\" sayed {friend4}')
    print("everyone laughs")
print("you finally arrive at the gate of the park")
print("\"you hear a homeless man saying come here little boys\"")
homeless = input("Would you like to approach the homeless guy?")
if homeless == 'yes':
    print(
        "you approach the homeless guy, then he reaches in his coat then rapidly wips out a apple, you look at him in confusion then he says\"ever wanted to see light?\"")
    hp -= 8
    print(f'then he pounces on you then and begins to vigerosly stab you all over (here is your hp:{hp})')
    hp_checker(hp, bandage)

elif homeless == 'no':
    print("you ignore the old homeless man you approach the gate of the park")

print(f'you and your friends enter the park then suddenly {friend1} says the most scooby-doo type s##t ever \"we should split up\" ' )
split = input("would you like to split up in groups (yes or no)")


if split == 'yes':
    print(f"you,{friend1}and{friend4}go togther while the other go there seperate ways")

elif split =='no':
    print("you say \"We aint doin that dumbass s##t,OK \"")


