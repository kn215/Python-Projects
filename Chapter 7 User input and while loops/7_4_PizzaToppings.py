# prompt = "What type of topping would you like on your pizza?: "
# prompt += "\nType 'quit' to quit program: "

# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"I will add {topping} to your pizza")
#     else:
#         break


# prompt = "What type of topping would you like on your pizza?: "
# prompt += "\nType 'quit' to quit program: "

# active = True

# while active:
#     topping = input(prompt)
    
#     if topping == 'quit':
#         active = False
#     else:
#         print(f"I will add {topping} to your pizza!")

prompt = "\nWhat type of topping would you like on your pizza?: "
prompt += "\nType 'quit' to quit program: "

topping = ""

while topping != 'quit':
    topping = input(prompt)
    
    if topping != 'quit':
        print(f"I will add {topping} to your pizza!")

 