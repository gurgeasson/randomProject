import math
my_float = 1.28885352996826
conversion_factor = 100 / 6
dice_roll = (my_float * (10 ** 6) % 1 * 100) / (100 / 6)
# dice_roll = math.ceil(((my_float ** 9) % 1 * 100) / conversion_factor)
print(dice_roll)