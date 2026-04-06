pets = []

pet = {
    'name' : 'amber',
    'type' : 'dog',
    'food' : 'chicken'
}
pets.append(pet)

pet = {
    'name' : 'drumstick',
    'type' : 'turkey',
    'food' : 'seeds'
}
pets.append(pet)

pet = {
    'name' : 'gordon',
    'type' : 'duck',
    'food' : 'fish'
}
pets.append(pet)
for pet in pets:
    print(f"Heres what i know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")


