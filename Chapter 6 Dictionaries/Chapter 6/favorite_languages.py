favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(f"\n{name.title()}")

language = favorite_languages['sarah'].title()
print(f"\nSarah's favorite language is {language}")   

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
else:
    print("Thank you everyone for taking the poll")

print("\nSorted Name list")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

coders= ['jen', 'ken', 'gift', 'edward']

for coder in coders:
    if coder in favorite_languages.keys():
        print(f"{coder.title()} thank you for taking our poll")
    else:
        print(f"{coder.title()} what is your favorite language")

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
          print(f"\t{language.title()}")