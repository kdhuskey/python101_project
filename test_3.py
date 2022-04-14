import random
# import time from console_progressbar 
# import ProgressBar

# def dif_price():

item_1_price = random.randint(1, 5)
item_2_price = random.randint(1, 15)
item_3_price = random.randint(1, 10)
item_1 = ['Coffee: ', item_1_price]
item_2 = ['Steak: ', item_2_price]
item_3 = ['Beer: ' , item_3_price]

print("""<<< ~ Welcome to Cliff Hangers!! ~ >>>
What would you like to do? Please select (1-4)""")
step_up = 0
max_steps = 25
#while True:        #step_up < max_steps:
def cliff_hanger_3():
    step_up = 0
    max_step = 25
    user_select = int(input(f"""
3. Guess on {item_3[0]}
4. To quit the game \nSelection: """))

    if user_select == 3:
        user_select_3 = int(input(f'What is the price for {item_3[0]}'))
        if user_select_3 == item_3_price:
            print('You got that correct!!')
        if user_select_3 != item_3_price:
            if user_select_3 > item_3_price:
                diff_1 = user_select_3 - item_3_price
                step_up += diff_1
                print(f'Incorrect guess for {item_3[0]} Actual price is {item_3_price}')
            elif user_select_3 < item_3_price:
                diff_2 = item_3_price - user_select_3
                step_up += diff_2
                print(f'Incorrect guess for {item_3[0]} Actual price is {item_3_price}')
        print(f'Yodely Guy is on step {step_up}!!')
    elif user_select == 4:
        print('Quitting the game!')
        # break
    else:
        print('That is not a valid selection choice!')
    if step_up >= 25:
        print('Game over!!!!')
    elif step_up < max_steps:
        print('You win!!!!!!!!')    


cliff_hanger_3()
step_up = 0
max_step = 25