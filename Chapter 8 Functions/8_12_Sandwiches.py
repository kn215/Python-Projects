def build_sandwiches(*toppings):
    """Make a sandwich"""
    print(f"\nIm making you a great sandwich, with the following items:")
    for topping in toppings:
        print(f"Adding -{topping}")
    print("Your sandwich is ready!")

build_sandwiches('steak', 'onions', 'cheddar', 'mayo')
build_sandwiches('ham', 'mustard', 'pork')
build_sandwiches('meatballs', 'provolone', 'marinara')