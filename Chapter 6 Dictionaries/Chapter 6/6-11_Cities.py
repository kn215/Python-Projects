cities = {
    'philadelphia' : {
        'country' : 'united states',
        'population': '1,600,000',
        'fact' : 'where the declaration of independence was signed',
    },
    'dublin' : {
        'country': 'ireland',
        'population': '1,450,000',
        'fact': 'they dont have snakes!',
    },
    'paris' : {
        'country': 'france',
        'population': '2,000,000',
        'fact': 'It is known as the city of love',
    },
}

for city, info in cities.items():
    print(f"\nHere are some facts about {city.title()}: ")
    for key, value in info.items():
        print(f"{key.title()}: {value.capitalize()}")