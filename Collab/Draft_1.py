
capital = 50

#status
knife = 0
bandages = 0
food = 4
water = 2
battery_pack = 0
crowbar = 0

#Gas station options with prices
options = {'knife':'16', 'bandage':'10', 'snack':'5', 'battery':'11', 'crowbar':'20', "water":'2'}



#to print the menu without brackets:
#for loop to get the keys and values of the dictionary
def gas_station(choices, money):

    print("Gas Station Menu:")
    print("-----------------------")
    for key, value in options.items():
        print(f'{key}:${value}')
    print("-----------------------")



    item_choice = input("What would you like to buy? (q to quit): ")
    money -= int(options[item_choice])
    print(f'Remaining money: ${money}')

    while item_choice != 'q':
        item_choice = input("What would you like to buy? (q to quit): ")



        if int(options[item_choice]) > money:
            print("Not enough money")



        elif int(options[item_choice]) < money:
            money -= int(choices[item_choice])
            print(f"Remaining money: ${money}")



gas_station(options, capital)