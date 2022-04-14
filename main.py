import random
from welcome_msg import cliff_hang
from end_game_q import end_game_q
import time 
from console_progressbar import ProgressBar
from cliff_hangers import game_body

pb = ProgressBar(total=100,prefix='', suffix='', decimals=3, length=50, fill='X', zfill='-')

cliff_hang()

print("""The contestant bids on three small prizes. 
For every dollar the contestant is away from the actual prices, 
a mountain climber takes one step up a mountain.
If the mountain climber does not exceed 25 steps after the contestant has bid on all three prizes, 
then the contestant wins a bonus prize.""")


item_1_price = random.randint(1, 5)
item_2_price = random.randint(1, 15)
item_3_price = random.randint(1, 10)
item_1 = ['Coffee: ', item_1_price]
item_2 = ['Steak: ', item_2_price]
item_3 = ['Beer: ' , item_3_price]

print("""
What would you like to do? Please select (1-4)""")
step_up = 0

game_body()