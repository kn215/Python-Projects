prompt = "\nWelcome to Regal, how old are you?: "
prompt += "\nType 'quit' to quit program: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print ("You get in free")
    elif age < 13:
        print("Your cost is $10")
    else:
        print("Your cost is $15")