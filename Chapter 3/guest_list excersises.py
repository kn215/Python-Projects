guests = ['lincoln', 'napoleon', 'jesus']

name = guests[0].title()
print(f"\n{name}, will you please come to dinner")

name = guests[1].title()
print(f"{name}, will you please come to dinner")

name = guests[2].title()
print(f"{name}, will you please come to dinner")

name = guests[1].title()
print(f"\nSorry {name} cant make it lets find a new person to invite")

#Napoleon cant make it
del (guests[1])
guests.insert( 1, 'Jefferson')

name = guests[0].title()
print(f"\n{name}, will you please come to dinner")

name = guests[1].title()
print(f"{name}, will you please come to dinner")

name = guests[2].title()
print(f"{name}, will you please come to dinner")

#Inserting more guests
print("\nWe got a bigger table!")
guests.insert(0, 'ghenghis khan')
guests.insert(2, 'Reagan')
guests.append('mcnabb')

name = guests[0].title()
print(f"\n{name}, will you please come to dinner")

name = guests[1].title()
print(f"{name}, will you please come to dinner")

name = guests[2].title()
print(f"{name}, will you please come to dinner")

name = guests[3].title()
print(f"{name}, will you please come to dinner")

name = guests[4].title()
print(f"{name}, will you please come to dinner")

name = guests[5].title()
print(f"{name}, will you please come to dinner")

 # print(f"\n{guests}")

# We didnt get the table
print("\nSorry everyone we actually didn't get the big table!, we can only invite two people")

#Uninvite guests
name = guests.pop()
print(f"\n{name}, Sorry we dont have enough room")

name = guests.pop()
print(f"{name}, Sorry we dont have enough room")

name = guests.pop()
print(f"{name}, Sorry we dont have enough room")

name = guests.pop()
print(f"{name}, Sorry we dont have enough room")


print(guests)

name = guests[0].title()
print(f"\n{name}, can you still come to dinner?")

name = guests[1].title()
print(f"\n{name}, can you still come to dinner?")

#del(guests[0])
#del(guests[0])

print(guests)

num_guests = len(guests)
print(f"\nI am inviting {num_guests} people to dinner tonight")



