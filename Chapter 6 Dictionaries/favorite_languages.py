favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# for name, language in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite language is {language.title()}")

# for name in favorite_languages.keys():
#     print(f"\n{name.title()}")

# language = favorite_languages['sarah'].title()
# print(f"\nSarah's favorite language is {language}")   

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
else:
    print("Thank you everyone for taking the poll")