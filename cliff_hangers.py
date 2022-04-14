import random
from welcome_msg import cliff_hang
from end_game_q import end_game_q
# import os
# system.os('clear')
# import time from console_progressbar 
# import ProgressBar

import time 
from progress import pb

def step_1(step_up, item_name, item_price):

    while True:
        try:
            user_select_1 = int(input(f'What is the price for {item_name}'))
        except:
            print('That is not a number!')
            continue
        if user_select_1 not in range(1, 500):
            print('invalid selection!')                 ####################### 
            continue
        if user_select_1 == item_price:
            print('You got that correct!! Play on..')
            break
        if user_select_1 != item_price:
            if user_select_1 > item_price:
                diff_1 = user_select_1 - item_price
                step_up += diff_1
                print(f'Incorrect guess for {item_name}Actual price is ${item_price}')
            elif user_select_1 < item_price:
                diff_2 = item_price - user_select_1
                step_up += diff_2
                print(f'Incorrect guess for {item_name}Actual price is ${item_price}')
            break
    if step_up != 0:
        print(f'Yodely Guy is on step {step_up}!!')
        pb.print_progress_bar(step_up)
        print(' ')
    if step_up >= 25:
        print('Sorry, Yodely guy fell off!! You lose. :(')
    return step_up



def game_body():
    

    item_1_price = random.randint(1, 5)
    item_2_price = random.randint(1, 15)
    item_3_price = random.randint(1, 10)
    item_1 = ['Coffee: ', item_1_price]
    item_2 = ['Steak: ', item_2_price]
    item_3 = ['Beer: ' , item_3_price]

    print("""
    What would you like to do? Please select (1-4)""")
    step_up = 0

    item_1_guessed = False
    item_2_guessed = False
    item_3_guessed = False

    while True:
        if item_1_guessed and item_2_guessed and item_3_guessed:
            
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

        if item_1_guessed == False:
            print(f'1. Guess on {item_1[0]}')
        if item_2_guessed == False:
            print(f'2. Guess on {item_2[0]}')
        if item_3_guessed == False:
            print(f'3. Guess on {item_3[0]}')
        print(f'4. To quit the game ')
        user_select = int(input('Selection: '))
        
        if user_select == 1 and item_1_guessed == False:
            item_1_guessed = True
            step_up = step_1(step_up, item_1[0], item_1[1])        
        elif user_select == 2 and item_2_guessed == False:
            item_2_guessed = True
            step_up = step_1(step_up, item_2[0], item_2[1])
            
        
        elif user_select == 3 and item_3_guessed == False:
            item_3_guessed = True
            step_up = step_1(step_up, item_3[0], item_3[1])
            
        #     if step_up <= 25:
        #         gam_q = input('Congratulations!! You win and you also win the bonus prize of a bottle of whiskey! The only catch is you have to guess within 5 dollars of how much it cost. If you loose then you do not win anything. Want to continue? Type "yes" or "no" ')
        #         if gam_q == 'yes':
        #             end_game_q()
        #         elif gam_q == 'no':
        #             print('Ok cool, you win the 3 prizes')
        #     if step_up < 25:
        #             print("""You win!!!! \nGame is over and will exit. \nIf you wish to play again, select play again.""")
        #     elif step_up > 25:
        #         print('Sorry, Yodely guy fell off!! You lose. :(') 
        #     break
        elif user_select == 4:
            print('Quitting the game!')
            break
        else:
            print('That is not a valid selection choice!')
        
    if step_up >= 25:
        print('Game over!!!!')
# elif step_up < 25:
#     print("""You win!!!! \nGame is over and will exit. \nIf you wish to play again, select play again.""")

