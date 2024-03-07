
capital = 50

#status
inventory = [0, 0, 0, 0, 0, 0]



purchased_items = []


#Gas station options with prices
options = {'knife':'16', 'bandage':'10', 'snack':'5', 'battery':'11', 'crowbar':'20', "water":'2'}
options_list = ['knife', 'bandages', 'snack', 'battery', 'crowbar', 'water']

print(options['knife'])

#to print the menu without brackets:
#for loop to get the keys and values of the dictionary
def gas_station(choices, money, inventory):

    print("Gas Station Menu:")
    print("-----------------------")
    for key, value in options.items():
        print(f'{key}:${value}')
    print("-----------------------")


    item_choice = input("What would you like to buy? (q to quit): ")

    if item_choice != 'q':

        money -= int(options[item_choice])
        print(f'Remaining money: ${money}')
        purchased_items.append(item_choice)

    while item_choice != 'q':
        item_choice = input("What would you like to buy? (q to quit): ")

        if item_choice == 'q':
            break


        if item_choice not in choices:
            print("Item not on menu, please try again")


        if int(options[item_choice]) > money:
            print("Not enough money")

        if int(options[item_choice]) == money:
            money -= int(choices[item_choice])
            print(f"Remaining money: ${money}")
            purchased_items.append(item_choice)


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

    print('INVENTORY')
    print("-----------------------")
    printed = []
    for i in purchased_items:
        if i in printed:
            continue
        else:
            print(f'{i}:{purchased_items.count(i)}')
            printed.append(i)


gas_station(options, capital, inventory)
