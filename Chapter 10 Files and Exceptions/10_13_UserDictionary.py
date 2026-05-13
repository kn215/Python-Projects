from pathlib import Path
import json

def get_stored_userinfo(path):
    """Greet user by name if available."""
    if path.exists():
        contents = path.read_text()
        user_dictionary = json.loads(contents)
        return user_dictionary
    else:
        return None
        
def get_new_userinfo(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    team = input("What is your favorite football team? ")
    player = input("Who is your favorite nfl player? ")

    user_dictionary = {
        'username': username,
        'team' : team,
        'player': player,
    }

    contents = json.dumps(user_dictionary)
    path.write_text(contents)
    return user_dictionary

def greet_user():
    """Greet the user by name."""
    path = Path('user_info.json')
    user_dictonary = get_stored_userinfo(path)
    if user_dictonary:
        print(f"Welcome back, {user_dictonary['username']}!")
        print(f"Have you watched any {user_dictonary['team']} games this season?")
        print(f"How has {user_dictonary['player']} been playing this season?")
    else:
        user_dictonary = get_new_userinfo(path)
        print(f"We'll remember you when you come back, {user_dictonary['username']}!")

greet_user()