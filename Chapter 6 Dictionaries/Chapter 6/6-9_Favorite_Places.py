favorite_places = {
    'ken': ['the poconos','thailand','washington,dc'],
    'gift': ['thailand', 'new york', 'hmart'],
    'joe': ['hawaii', 'philadelphia', 'seattle']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes going to these places:")
    for place in places:
        print(f"-{place.title()}")