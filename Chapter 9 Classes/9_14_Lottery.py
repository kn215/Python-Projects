from random import choice

value_choices = [1,2,3,4,5,6,7,8,9,11, 'b', 'g', 'x', 'd', 'k']

winning_prize = []

while len(winning_prize) < 4:
    picked_value = choice(value_choices)

    if picked_value not in winning_prize:
        print(f"We pulled a : {picked_value}")
        winning_prize.append(picked_value)

print(f"The winning ticket is {winning_prize}")

