import math
my_float = 32.108963275734920398756647147648349
conversion_factor = 100 / 6
dice_roll = math.ceil(((my_float ** 9) % 1 * 100) / conversion_factor)
print(dice_roll)