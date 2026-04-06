rivers = {
    'nile' : 'egypt',
    'delaware' : 'united states',
      'amazon' : 'brazil',
    }


for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(f"\n{country}")

for river, country in rivers.items():
    print(f"The {river} is a river in {country}")