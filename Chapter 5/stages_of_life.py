age = int(input("Enter your age: "))

if age < 2:
    print("you are a baby")

elif age < 4:
    print("you are a toddler")
elif age < 13:
    print("you are a kid")
elif age < 20:
    print("you are an teenage")
elif age < 65:
    print("you are an adult")
else:
    print("Your an elder")