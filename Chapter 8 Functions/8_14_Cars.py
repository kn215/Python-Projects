def make_car(manufacturer, model, **features):
    """A function for creating a car"""
    car_dict = {
        'manufacturer' : manufacturer.title(),
        'model' : model.title(),
        }
    
    for feature, value in features.items():
        car_dict[feature] = value
    
    return car_dict

my_crv = make_car('honda','crv',type= 'hybrid',mode= 'sport')
print(my_crv)

my_accord = make_car('honda', 'accord',features= 'moonroof')
print(my_accord)
