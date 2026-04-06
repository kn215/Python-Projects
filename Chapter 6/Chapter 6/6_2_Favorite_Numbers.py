favorite_numbers = {
    'gift': [7, 11],
    'ken': [7, 18],
    'joe': [44, 3],
    'dad': [44, 5],
    'aj': [5, 48],
}
num = favorite_numbers['gift']
print(favorite_numbers['gift'])


for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")


num = favorite_numbers['ken']
# print(f"Ken's favorite numbers are: {num}")

# num = favorite_numbers['joe']
# print(f"Joe's favorite numbers are: {num}")

# num = favorite_numbers['dad']
# print(f"Dad's favorite numbersare are: {num}")

# num = favorite_numbers['aj']
# print(f"Aj's favorite numbers are: {num}")
