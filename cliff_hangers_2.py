import random
# GAME DESCRIPTION
"""The contestant bids on three small prizes. 
For every dollar the contestant is away from the actual prices, 
a mountain climber takes one step up a mountain.
If the mountain climber does not exceed 25 steps after the contestant has bid on all three prizes, 
then the contestant wins a bonus prize."""
# def dif_price():

item_1_price = random.randint(1, 5)
item_2_price = random.randint(1, 15)
item_3_price = random.randint(1, 10)
item_1 = ['Coffee: ', item_1_price]
item_2 = ['Steak: ', item_2_price]
item_3 = ['Beer: ' , item_3_price]

print("""<<< ~ Welcome to Cliff Hangers!! ~ >>>
What would you like to do? Please select (1-4)""")
while True:
    user_select = int(input(f"""
1. Guess on {item_1[0]}
2. Guess on {item_2[0]}
3. Guess on {item_3[0]}
4. To quit the game \nSelection: """))
    step_up = 0
    total_item_price = 0
    max_steps = 25
    if step_up == 25:
        print('Game is over!!!!!')
    if user_select == 1:
        user_select_1 = int(input(f'What is the price for {item_1[0]}?: '))
        if user_select_1 != item_1_price:
            if user_select_1 > item_1_price:
                diff_1 = user_select_1 - item_1_price
                step_up += diff_1
                print(f'Incorrect guess for {item_1[0]} Mountain Man is on step {step_up}!')
            elif user_select_1 < item_1_price:
                diff_2 = item_1_price - user_select_1
                step_up += diff_2
                print(f'Incorrect guess for {item_1[0]} Mountain Man is on step {step_up}!')
        else:
            print(step_up)
    elif user_select == 2:
        user_select_2 = int(input(f'What is the price for {item_2[0]}?: '))
        if user_select_2 != item_2_price:
            if user_select_2 > item_2_price:
                diff_1 = user_select_2 - item_2_price
                step_up += diff_1
                print(f'Incorrect guess for {item_2[0]} Mountain Man is on step {step_up}!')
            elif user_select_2 < item_2_price:
                diff_2 = item_2_price - user_select_2
                step_up += diff_2
                print(f'Incorrect guess for {item_2[0]} Mountain Man is on step {step_up}!')
        else:
            print(step_up)
    elif user_select == 3:
        user_select_3 = int(input(f'What is the price for {item_3[0]}?: '))
        if user_select_3 != item_3_price:
            if user_select_3 > item_3_price:
                diff_1 = user_select_3 - item_3_price
                step_up += diff_1
                print(f'Incorrect guess for {item_3[0]} Mountain Man is on step {step_up}!')
            elif user_select_3 < item_3_price:
                diff_2 = item_3_price - user_select_3
                step_up += diff_2
                print(f'Incorrect guess for {item_3[0]} Mountain Man is on step {step_up}!')
        else:
            print(step_up)
    elif user_select == 4:
        print('Quitting the game!')
        break
    else:
        print('That is not a valid selection choice!')
    if step_up >= 25:
        print('Game over!!!!')
    
