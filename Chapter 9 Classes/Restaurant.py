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