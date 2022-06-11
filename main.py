import math
from math import sin
from math import cos
from math import sqrt
from math import pi

#Projectile motion calculator

print("Welcome to the projectile motion simulator.")
print("This calculates the range of a projectile given initial velocity and angle data. Uses g = 9.8 m/s/s. Assumes air resistance is negligible.")


v = int(input("Enter the initial velocity, in meters per second: "))
D = int(input("Enter the angle of elevation with respect to the horizontal, in degrees: "))


def range1(v, D):
  return v * math.cos((D * (math.pi / 180))) * ((v * math.sin((D * (math.pi / 180))) / 4.9))

print("The horizontal range is " + str(range1(v,D)) + " meters.")



