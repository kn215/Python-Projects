from car import Car
from electric_car import ElectricCar

my_porsche =  Car('porsche', '911 turbo', 2025)
print(my_porsche.get_descriptive_name())
my_tesla = ElectricCar('Tesla', 'Model 3', 2025)
print(my_tesla.get_descriptive_name())