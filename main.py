import random
from welcome_msg import cliff_hang
from end_of_game_q import end_game_q
import time 
from game_body import game_body
space_divider = """ """
cliff_hang()

print("""The contestant bids on three small prizes. 
For every dollar the contestant is away from the actual prices, 
a mountain climber takes one step up a mountain.
If the mountain climber does not exceed 25 steps after the contestant has bid on all three prizes, 
then the contestant wins a bonus prize.""")
print(space_divider)
print(space_divider)


enter_or_not = input("Do you want to play? Select (y/n): " )
print(space_divider)
print(space_divider)

if enter_or_not == 'y':
    game_body()
else:
    print('Ok bye!')

