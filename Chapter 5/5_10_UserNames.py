current_users = ['ken', 'gift', 'joe', 'mike', 'amanda', 'john']
new_users = ['ken', 'gift', 'steve', 'bob', 'JOHN']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user} username is already take, please enter a new one")
    else:
        print(f" Hello {new_user} welcome to the group")

print("Please grab a name tag")