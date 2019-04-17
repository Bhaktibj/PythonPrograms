# Write a program Quadratic.
# Python to find the roots of the equation a*x*x + b*x + c.
# Since the equation is x*x, hence there are 2 roots.
# The 2 roots of the equation can be found using a formula
import math

a = int(input("Enter The Input a"))
b = int(input("Enter The Input b"))
c = int(input("Enter the Input c"))
if a == 0:
    print("invalid")
else:
    delta = b * b - 4 * a * c
    sqrt_root = math.sqrt(abs(delta))
    print("delta is=", sqrt_root)
    rootX1 = ((-b + sqrt_root) / (2 * a))
    print("Root1 of X=", rootX1)
    rootX2 = ((-b - sqrt_root) / (2 * a))
    print("Root2 of X=", rootX2)
