import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'sausage', 'extra cheese')

from pizza import make_pizza

make_pizza(18, 'ham')

from pizza import make_pizza as mp

mp(20, 'salami')

import pizza as p
p.make_pizza(16, 'buffalo chicken')

from pizza import *
make_pizza(16, 'chicken alfredo')