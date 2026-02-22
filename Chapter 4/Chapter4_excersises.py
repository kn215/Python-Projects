my_pizzas = ['Pepperoni', 'Cheesesteak', 'Sausage']

friends_pizzas = my_pizzas[:]

my_pizzas.append('bbq chicken')
friends_pizzas.append('Brooklyn')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)

# for pizza in my_pizzas:
#     print(pizza)
    
# for pizza in pizzas:   
#     print(f"\n {pizza.title()} is one of my favorite kinds of pizza")

# print("\nI really love pizza it's one of my favorite foods")


# animals = ['eagle', 'penguin', 'duck']

# for animal in animals:
#     print(animal)

# for animal in animals:
#     print(f"A {animal.title()} is an animal that has a beak")

# print("\n All of these animals have a beak")

# for value in range(1, 21):
#     print(value)

# for value in range(1, 1000001):
#     print(value)

# numbers = list(range (1, 1000001))
# lowest = min(numbers)
# highest = max(numbers)
# total_numbers = sum(numbers)
# print(lowest)
# print(highest)
# print(total_numbers)

# odd_numbers = list(range(1, 22, 2))
# for numbers in odd_numbers:
#     print(numbers)

# threes = list(range(3, 31, 3))
# for number in threes:
#     print(number)

# cubes = []
# for value in range(1, 11):
#     cube = value**3
#     cubes.append(cube)

# for cube in cubes:
#     print(cube)

# cubes = [value**3 for value in range(1, 11)]

wow_classes = ['warrior', 'mage', 'hunter', 'warlock', 'rogue']

print("The first 3 classes are:")

for classes in wow_classes[:3]:
    print(classes.title())

print("\nThe middle 3 classes are:")
for classes in wow_classes[1:4]:
    print(classes)

print("\nThe last 3 classes are:")
for classes in wow_classes[2:]:
    print(classes)

print("\n", len(wow_classes))