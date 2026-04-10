sandwich_orders = ['cheesesteak', 'cheeseburger', 'chicken parm', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

#Verify each sandwich until there are no more sandwich orders
print("Im sorry were all of of pastrami today")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Making {current_sandwich.title()} right now!")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())

#Print Test to verify order list is cleared
print(f"All orders have been complete the list is empty! {sandwich_orders}")
print(finished_sandwiches)
