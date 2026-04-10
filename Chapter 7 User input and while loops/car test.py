
class Car:
    # Class attribute (shared by all instances)
    species = "Vehicle"

    def __init__(self, color, mileage):
        """
        The constructor method, called when a new object is created.
        'self' refers to the specific instance being created.
        """
        self.color = color   # Instance attribute
        self.mileage = mileage # Instance attribute

    def drive(self, distance):
        """
        An instance method that operates on the object's attributes.
        """
        self.mileage += distance
        return f"The {self.color} car has driven {distance} miles. Total mileage: {self.mileage}."

    def __str__(self):
        """
        A special 'dunder' method to provide a human-readable string representation.
        """
        return f"The {self.color} car has {self.mileage:,} miles."

# Create objects (instances) of the Car class
blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

# Access attributes and call methods
print(blue_car.species)
print(blue_car.drive(500))
print(red_car)