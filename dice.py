import random


class Dice:

    def roll(self):
      
        face = random.randrange(1, 7, 1)
        return face


dice = Dice()
print(dice.roll())
