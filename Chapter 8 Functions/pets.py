def describe_pet(animal_type, pet_name):
    """Function for telling pet type / name"""
    print(f"\nI have a {animal_type.title()}")
    print(f"Their name is {pet_name.title()}")

describe_pet('dog', 'molly')
describe_pet('parrot', 'petey')
describe_pet('steve', 'monkey')



def sport_info(team_name, sport_name):
    """Function for describing a sports team"""
    print(f"\nThe {team_name.title()}'s are a {sport_name.title()} team")

sport_info(team_name= 'philadelphia eagle', sport_name='football')
sport_info(team_name= 'philadelphia flyer', sport_name='ice hockey')
sport_info(team_name= 'philadelphia phillies', sport_name='baseball')


def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()
    
