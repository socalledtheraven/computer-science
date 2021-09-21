import math, re

#procedures
def cube(side):
    return side^3

def square_pyramid(base_edge, height):
    return (base_edge^2)*height/3

def cone(radius, height):
    return math.pi*(radius^2)*height/3

#main code

user_inp = int(input("What would you like to calculate? (1 for cube, 2 for pyramid, 3 for cone)"))

if user_inp == 1:
    user_inp = input("What is the side of the cube?")
    user_inp = int(re.sub(r'[a-z]+', '', user_inp, re.I))
    print("The cube has a volume of {:.3f}".format(cube(user_inp)))
elif user_inp == 2:
    user_inp = input("What is the side of the pyramid?")
    user_inp = int(re.sub(r'[a-z]+', '', user_inp, re.I))
    pyramid_height = input("What is the height of the pyramid?")
    pyramid_height = int(re.sub(r'[a-z]+', '', pyramid_height, re.I))
    print("The pyramid has a volume of {:.3f}".format(square_pyramid(user_inp, pyramid_height)))
else:
    user_inp = input("What is the radius of the cone?")
    user_inp = int(re.sub(r'[a-z]+', '', user_inp, re.I))
    cone_height = input("What is the height of the cone?")
    cone_height = int(re.sub(r'[a-z]+', '', cone_height, re.I))
    print("The pyramid has a volume of {:.3f}".format(cone(user_inp, cone_height)))