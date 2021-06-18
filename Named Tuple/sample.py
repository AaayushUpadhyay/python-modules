from collections import namedtuple

color=(55,155,255) #(r,g,b) #this is a tuple

Color = namedtuple('Color',['red','green','blue'])

color=Color(55,155,255)
white=Color(255,255,255)
# Color(red=55, green=155, blue=255)

# print(color[0])
print(color.red)
print(white.blue)