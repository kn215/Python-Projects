print("Enter 'q' to stop processing")

while True:
    try:
        a = input("Tell me the first number: " )
        if a == 'q':
            break

        a = int(a)

        b = input("Tell me the second number: ")
        if b == 'q':
            break

        b = int(b)
        
    except ValueError:
        print("Sorry number must be in integer form")
    else:
        total = a + b
        print(f"The total of {a} and {b} is: {total} ")


              