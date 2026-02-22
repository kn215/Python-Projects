my_foods = ['pizza', 'alfredo', 'cheesesteak']
friends_foods = my_foods[:]

my_foods.append('spaghetti')
friends_foods.append('ravioli')

print("My favorite foods are:")
print(my_foods)

print("My friends favorite foods are:")
print(friends_foods)

print("\nmy foods:")
for foods in my_foods:
    print(foods)

print("\n my friend's foods:")
for foods in friends_foods:
    print(foods)
