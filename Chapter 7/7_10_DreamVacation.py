user_prompt = "\nWhat's your name? "
vacation_prompt = "\nIf you could visit anywhere in the world where would you go? "
repeat_prompt = "\nWould you like someone else to answer this poll (yes or no)? "

answers = {}

while True:
    name = input(user_prompt)
    place = input(vacation_prompt)

    # Store their answer
    answers[name] = place

    repeat = input(repeat_prompt)
    if repeat == 'no':
        break

#Prompt results
print("\nHere are the results of our survey!:")
for name,place in answers.items():
    print(f"{name.title()} wants to go to {place.title()}")
