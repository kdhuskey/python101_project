def end_game_q():
    b_guess = int(input('What is your guess for this bottle of Blanton\'s bourbon? '))
    price = 95
    if b_guess >= 90 and b_guess <= 100:
        print(f'The price is.. ${price}')
        print('You were within 5 dollars! You win all 3 prizes and the bonus prize!!')
        print("""
____    ____  ______    __    __    ____    __    ____  __  .__   __.  __   __  
\   \  /   / /  __  \  |  |  |  |   \   \  /  \  /   / |  | |  \ |  | |  | |  | 
 \   \/   / |  |  |  | |  |  |  |    \   \/    \/   /  |  | |   \|  | |  | |  | 
  \_    _/  |  |  |  | |  |  |  |     \            /   |  | |  . `  | |  | |  | 
    |  |    |  `--'  | |  `--'  |      \    /\    /    |  | |  |\   | |__| |__| 
    |__|     \______/   \______/        \__/  \__/     |__| |__| \__| (__) (__) 
                                                                                
        """)
    else:
        print(f'The price is.. ${price}')
        print('So sorry but you lose. Game over!!')

                    # print("""You win!!!! \nGame is over and will exit. \nIf you wish to play again, select play again.""")