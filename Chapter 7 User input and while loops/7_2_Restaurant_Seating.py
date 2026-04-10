seats = input("How many people are in your part?: ")
seats = int(seats)
if seats >= 8:
    print("Sorry you will have to wait for a table!")
else:
    print("We can seat you right now!")