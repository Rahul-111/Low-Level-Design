import random
class Dice:

    # class methods
    min = 1
    max = 6

    def __init__(self, diceCount: int) -> None:
        self.diceCount = diceCount


    def rollDice(self):
        totalSum = 0
        diceUsed = 0

        while diceUsed < self.diceCount:

            totalSum += random.randint(Dice.min, Dice.max)
            diceUsed +=1

        return totalSum

