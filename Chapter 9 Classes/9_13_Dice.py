from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

dice_6 = Die()

results = []
for rolls in range(10):
    result = dice_6.roll_die()
    results.append(result)
print("10 rolls of a six sided die")
print(results) 

dice_10 = Die(sides= 20)
results = []
for rolls in range(10):
    result = dice_10.roll_die()
    results.append(result)
print("10 rolls of a ten sided die")
print(results) 

