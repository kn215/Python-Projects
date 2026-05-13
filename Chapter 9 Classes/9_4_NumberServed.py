class Restaurant:
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cuisine_type
        self.number_served = 0
        

    def describe_restaurant(self):
        """A method that describes a restaurant"""
        print(f"Our restaurant {self.restaurant_name.title()} serves delicious {self.cusine_type} food!")
    
    def open_restaurant(self):
        """A method that explains that the resturant is open"""
        print(f"{self.restaurant_name} is open for business today!")

    def customers_served(self, number_served):
        """sets number of custoemrs served"""
        self.number_served = number_served

    def increment_customer_served(self, increment_served):
        """Increases customers served"""
        self.number_served += increment_served

my_restaurant = Restaurant('angelos', 'italian')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# Equals 0
print(f"\nCustomer's Served: {my_restaurant.number_served}")

my_restaurant.number_served = 500
print(f"\nCustomer's Served: {my_restaurant.number_served}")

my_restaurant.customers_served(1000)
print(f"\nCustomer's Served: {my_restaurant.number_served}")

my_restaurant.increment_customer_served(250)
print(f"\nCustomer's Served: {my_restaurant.number_served}")






# print(f"\nMy restaurants name is {my_restaurant.restaurant_name.title()}")
# print(f"At our restaurant we server {my_restaurant.cusine_type.title()} food")
