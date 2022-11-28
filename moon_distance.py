""" Let's say the Moon's orbit around planet 
Earth is a perfect circle, with a radius r (in km)""" 
from math import radians
r = 192500
# Travel distance of Moon over 12 degrees.
dist= radians(12)
dist *= r
print (dist)