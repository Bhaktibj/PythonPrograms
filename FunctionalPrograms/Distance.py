# Write a program Distance that takes two integer command-line arguments x and y
# and prints the Euclidean distance from the point (x, y) to the origin (0, 0).
# The formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
import math
import sys

x = int(input(sys.argv[0]))  # Command Line arguments x
y = int(input(sys.argv))
dist = math.sqrt(x * x + y * y)
print("distance is=", dist)
