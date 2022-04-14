import random
from welcome_msg import cliff_hang
from end_game_q import end_game_q
# import os
# system.os('clear')
# import time from console_progressbar 
# import ProgressBar

import time 
from console_progressbar import ProgressBar
def game_body():
    pb = ProgressBar(total=25,prefix='', suffix='🗣 🗣  🏔', decimals=3, length=50, fill='X', zfill='-')
    # pb.print_progress_bar(2)
    # time.sleep(5)
    # pb.print_progress_bar(25)
    # time.sleep(5)
    # pb.print_progress_bar(50)
    # time.sleep(5)
    # pb.print_progress_bar(95)
    # time.sleep(5)
    # pb.print_progress_bar(100)


    # print("""The contestant bids on three small prizes. 
    # For every dollar the contestant is away from the actual prices, 
    # a mountain climber takes one step up a mountain.
    # If the mountain climber does not exceed 25 steps after the contestant has bid on all three prizes, 
    # then the contestant wins a bonus prize.""")


    item_1_price = random.randint(1, 5)
    item_2_price = random.randint(1, 15)
    item_3_price = random.randint(1, 10)
    item_1 = ['Coffee: ', item_1_price]
    item_2 = ['Steak: ', item_2_price]
    item_3 = ['Beer: ' , item_3_price]

    print("""
    What would you like to do? Please select (1-4)""")
    step_up = 0


    while True:

        user_select = int(input(f"""
    1. Guess on {item_1[0]}
    2. Guess on {item_2[0]}
    3. Guess on {item_3[0]}
    4. To quit the game \nSelection: """))
        # if step_up >= 25:
        #     print('Sorry, Yodely guy fell off!! You lose. :(')
        #     break
        if user_select == 1:
            while True:
                try:
                    user_select_1 = int(input(f'What is the price for {item_1[0]}'))
                except:
                    print('That is not a number!')
                    continue
                if user_select_1 not in range(1, 500):
                    print('invalid selection!')                 ####################### 
                    continue
                if user_select_1 == item_1_price:
                    print('You got that correct!! Play on..')
                    break
                if user_select_1 != item_1_price:
                    if user_select_1 > item_1_price:
                        diff_1 = user_select_1 - item_1_price
                        step_up += diff_1
                        print(f'Incorrect guess for {item_1[0]}Actual price is ${item_1_price}')
                    elif user_select_1 < item_1_price:
                        diff_2 = item_1_price - user_select_1
                        step_up += diff_2
                        print(f'Incorrect guess for {item_1[0]}Actual price is ${item_1_price}')
                    break
            if step_up != 0:
                print(f'Yodely Guy is on step {step_up}!!')
                pb.print_progress_bar(step_up)
                print(' ')
            if step_up >= 25:
                print('Sorry, Yodely guy fell off!! You lose. :(')
                break
            
        elif user_select == 2:
            user_select_2 = int(input(f'What is the price for {item_2[0]}'))
            if user_select_2 == item_2_price:
                print('You got that correct!! Play on..')
            if user_select_2 != item_2_price:
                if user_select_2 > item_2_price:
                    diff_1 = user_select_2 - item_2_price
                    step_up += diff_1
                    print(f'Incorrect guess for {item_2[0]}Actual price is ${item_2_price}')
                elif user_select_2 < item_2_price:
                    diff_2 = item_2_price - user_select_2
                    step_up += diff_2
                    print(f'Incorrect guess for {item_2[0]}Actual price is ${item_2_price}')
            if step_up != 0:
                print(f'Yodely Guy is on step {step_up}!!')
                pb.print_progress_bar(step_up)
                print(' ')
            if step_up >= 25:
                print('Sorry, Yodely guy fell off!! You lose. :(')
                break
        
        elif user_select == 3:
            user_select_3 = int(input(f'What is the price for {item_3[0]}'))
            if user_select_3 == item_3_price:
                print('You got that correct!!')
            if user_select_3 != item_3_price:
                if user_select_3 > item_3_price:
                    diff_1 = user_select_3 - item_3_price
                    step_up += diff_1
                    print(f'Incorrect guess for {item_3[0]} Actual price is ${item_3_price}')
                elif user_select_3 < item_3_price:
                    diff_2 = item_3_price - user_select_3
                    step_up += diff_2
                    print(f'Incorrect guess for {item_3[0]} Actual price is ${item_3_price}')
            if step_up != 0:
                print(f'Yodely Guy is on step {step_up}!!')
                pb.print_progress_bar(step_up)
                print(' ')
            if step_up > 25:
                print('Sorry, Yodely guy fell off!! You lose. :(')
                break
            if step_up <= 25:
                gam_q = input('Congratulations!! You win and you also win the bonus prize of a bottle of whiskey! The only catch is you have to guess within 5 dollars of how much it cost. If you loose then you do not win anything. Want to continue? Type "yes" or "no" ')
                if gam_q == 'yes':
                    end_game_q()
                elif gam_q == 'no':
                    print('Ok cool, you win the 3 prizes')
            if step_up < 25:
                    print("""You win!!!! \nGame is over and will exit. \nIf you wish to play again, select play again.""")
            elif step_up > 25:
                print('Sorry, Yodely guy fell off!! You lose. :(') 
            break
        elif user_select == 4:
            print('Quitting the game!')
            break
        else:
            print('That is not a valid selection choice!')
        
    if step_up >= 25:
        print('Game over!!!!')
# elif step_up < 25:
#     print("""You win!!!! \nGame is over and will exit. \nIf you wish to play again, select play again.""")

