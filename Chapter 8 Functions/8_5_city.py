def describe_city(city, country= 'the united states'):
    """Function for describing a city"""
    print(f"\n{city.title()} is a city in {country.title()}")
    print(f"Would you like to visit {city.title()} someday?")

describe_city('oakland')
describe_city('boston')
describe_city('paris', 'france')
describe_city(country= 'japan', city= 'osaka')