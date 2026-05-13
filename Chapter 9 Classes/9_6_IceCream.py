class Restaurant:
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cuisine_type

    def describe_restaurant(self):
        """A method that describes a restaurant"""
        print(f"Our restaurant {self.restaurant_name.title()} serves delicious {self.cusine_type}!")
    
    def open_restaurant(self):
        """A method that explains that the resturant is open"""
        print(f"{self.restaurant_name} is open for business today!")

class IceCreamStand(Restaurant):
    """A child class of restaurant called IceCreamStand"""
    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']
    
    def available_flavors(self):
        """A method that prints available flavors"""
        print(f"\nWe have the following flavors available: ")
        for flavor in self.flavors:
            print(f"{flavor}")

        

    

my_restaurant = Restaurant('angelos', 'italian')


# print(f"\nMy restaurants name is {my_restaurant.restaurant_name.title()}")
# print(f"At our restaurant we server {my_restaurant.cusine_type.title()} food")

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

my_ice_cream = IceCreamStand('Kennys')
my_ice_cream.describe_restaurant()
my_ice_cream.open_restaurant()
my_ice_cream.available_flavors()
