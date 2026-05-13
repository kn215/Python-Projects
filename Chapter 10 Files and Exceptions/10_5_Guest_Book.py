from pathlib import Path

path = Path('Guest_Book.txt')

prompt = '\nHello what is your name?'
prompt += '\nPlease press quit if you would like to leave the program:  '

guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"Thank you {name} we will add you to the guest book!")
    guest_names.append(name)

# file_string = ''
# for name in guest_names:
#     file_string += f"{name.title()}\n"

# path.write_text(file_string)