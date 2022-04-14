def end_game_q():
    b_guess = int(input('What is your guess for this bottle of Blanton\'s bourbon? '))
    price = 95
    if b_guess >= 85 and b_guess <= 100:
        print(f'The price is.. ${price}')
        print('You were within 5 dollars! You win all 3 prizes and the bonus prize!!')
    else:
        print(f'The price is.. ${price}')
        print('So sorry')
