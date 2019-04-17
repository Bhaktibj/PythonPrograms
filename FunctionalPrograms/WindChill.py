# Prints the Windchill
import sys
import math

t = float(input(sys.argv[0]))
v = float(input(sys.argv))
if t < 50:
    if v > 120 or v < 3:
        w = 35.74 + 0.6215 + (0.4275 * t - 35.75) * math.pow(v, 0.16)
        print("Given Temperature T is=", t)
        print("Given wind Speed V is=", v)
        print("Wind chill is=", w)
    else:
        print(" The formula is not valid")
else:
    print("The formula is not valid")
