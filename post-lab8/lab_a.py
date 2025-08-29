import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degrees = 180
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is {radians} radians")
