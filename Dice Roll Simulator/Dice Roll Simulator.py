import random


CharValues = [1,2,3,4,5,6]


roll_dice = 0
for i in CharValues:
    roll_dice += random.randint(CharValues, b="")

print(roll_dice)
