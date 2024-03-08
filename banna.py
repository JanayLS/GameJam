from beginner import *
from Draft_1 import *
def trapper():
    print("you guys decide to enter the halls of mirrors")
    print("the moment  yall enter you feel an uneasy precense")
    print(f'you then hear two of your freinds voices fade, you turn around and see {friend1} and {friend4} have suddenly dissapered')
    print(f'{friend2} and you scream in utter terror after realizing your friends bodies were on the ceiling')
    print(f'{friend3}  he begins to curl up and begins to lose his sanity you and {friend2} are the only ones still alive/ sain')
    print(f'{friend2} lunges at you with a rusty the rusty crowbar and hits you in the head yall used to break in, you look in his eyes and a nothingness void ')

    if purchased_items.count("knife") >= 1:
        print('INVENTORY')
        print("-----------------------")
        printed = []
        for i in purchased_items:
            if i in printed:
                continue
            else:
                print(f'{i}:{purchased_items.count(i)}')
                printed.append(i)
        knifeguy= input("would you like to use knife? (yes or no)")

        if knifeguy == 'yes':
            purchased_items.remove('knife')
            print("you stab your friend in the eye but it gets stuck")
            run_or_nah = input("would you like to run?(yes or no)")
            if run_or_nah == 'yes':
                print(f'you  shrugged {friend2} off you and you started to run towards the exit')
                print(f'you make it out of the hall of mirrors but {friend2} if still chasing after you')
                print("you see the exit gate in the distance, even though you legs are begging to fail you persist on")
                print("you run out of the exit gate and the homeless man pounces from the corner and stab you in the neck")
                print("you die")
            else:
                print("you swing at the monster taking over your friends but he was unphased then he shoves his fist in your mouth and crushes your skull")
        else:
            print(f'should have used the knife, {friend2} rips a deep hole into your stomach and begins to devour your inside while you were still conscious')
            print("you died")
            quit()
    else:
        print(f'should have purchased a knife, {friend2} rips a deep hole into your stomach and begins to devour your inside while you were still conscious')
        print("guess what you died")
        quit()

