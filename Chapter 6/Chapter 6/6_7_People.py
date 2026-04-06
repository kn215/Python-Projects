people = {
    'sbradley' : {
        'first_name' : 'steve', 
        'last_name': 'bradley', 
        'age': 30, 'city': 
        'doylestown',
    },
'mryan' : {
    'first_name' : 'mike', 
    'last_name': 'ryan', 
    'age': 24, 'city': 
    'philadelphia',
    },

'bclark' : {
    'first_name' : 'bob', 
    'last_name': 'clark', 
    'age': 30, 'city': 
    'ottawa',
    },
}


for person, user_info in people.items():
    # print(f"\nPerson: {person}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['city']
    age = user_info['age']

    # print(f"\tFull Name: {full_name.title()}")
    # print(f"\tAge: {age}")
    # print(f"\tLocation: {location.title()}")

    print(f"{full_name.title()} of {location.title()} is {age}")
    