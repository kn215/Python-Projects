class Restaurant:
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cuisine_type

    def describe_restaurant(self):
        """A method that describes a restaurant"""
        print(f"Our restaurant {self.restaurant_name.title()} serves delicious {self.cusine_type} food!")
    
    def open_restaurant(self):
        """A method that explains that the resturant is open"""
        print(f"{self.restaurant_name} is open for business today!")

restaurant1 = Restaurant('angelos', 'italian')
restaurant2 = Restaurant('mings', 'chinese')
restaurant3 = Restaurant('nueva dia', 'mexican')

# print(f"\nMy restaurants name is {restaurant1.restaurant_name.title()}")
# print(f"At our restaurant we server {restaurant1.cusine_type.title()} food")
# restaurant1.open_restaurant()

restaurant1.describe_restaurant()

restaurant2.describe_restaurant()

restaurant3.describe_restaurant()

