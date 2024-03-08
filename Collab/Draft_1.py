import random
'''
In other programs, to find the inventory count for the different items:
bandageCount = purchased_items.count("bandages")
'''
capital = 50

#status

inventory = [0, 0, 0, 0, 0, 0]
purchased_items = []


#Gas station options with prices
options = {'knife':'16', 'bandage':'10', 'snack':'5', 'battery':'11', 'crowbar':'20', "water":'2'}
options_list = ['knife', 'bandages', 'snack', 'battery', 'crowbar', 'water']





#this function takes in the amount of money you have, the inventory you already have
#and the menu, and outputs your final inventory after the gas station
def gas_station(choices, money, inventory):
    #iterates through the dictionary and outputs the menu
    #with the prices

    print("Gas Station Menu:")
    print("-----------------------")
    # to print the menu without brackets:
    # for loop to get the keys and values of the dictionary
    for key, value in options.items():
        print(f'{key}:${value}')
    print("-----------------------")


    item_choice = input("What would you like to buy? (q to quit): ")

    #double checking if q is
    #entered before loop is entered



    #Loop to repeatedly prompt until a valid input is given such as q or a menu item
    while True:
        if item_choice != 'q':

            if item_choice not in choices:
                print("Item not on menu, please try again")
                item_choice = input("What would you like to buy? (q to quit): ")

            #calculating the total money left if they didnt type Q and if its in the mnenu
            else:
                money -= int(options[item_choice])
                print(f'Remaining money: ${money}')
                purchased_items.append(item_choice)
                break

        else:
            break

    #while the item choice is not quit:
    while item_choice != 'q':

        item_choice = input("What would you like to buy? (q to quit): ")

        if item_choice == 'q':
            break


        if item_choice not in choices:
            print("Item not on menu, please try again")


        elif int(options[item_choice]) > money:
            print("Not enough money")



        elif int(options[item_choice]) == money:
            money -= int(choices[item_choice])
            print(f"Remaining money: ${money}")
            purchased_items.append(item_choice)
        #adding their purchased item after making sure they have enough money
        #subtracting the cost amount from total


        elif int(options[item_choice]) < money:
            money -= int(choices[item_choice])
            print(f"Remaining money: ${money}")
            purchased_items.append(item_choice)



    print("You've left the gas station. ")
    print()
    print()


    for i in purchased_items:
        if i in options_list:
            inventory[options_list.index(i)] += 1


#outputs the inventory by iterating through their purchased items

    print('INVENTORY')

    print("-----------------------")
    printed = []
    for i in purchased_items:
        if i in printed:
            continue

        else:
            print(f'{i}:{purchased_items.count(i)}')
            printed.append(i)


#function to return true or false for randomness
def randomness():
    tf = [True, False]

    returned = random.choice(tf)
    return returned

