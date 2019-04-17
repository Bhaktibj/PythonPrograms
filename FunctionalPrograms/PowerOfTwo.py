# Find the Power of Two
import sys

number = int(input(sys.argv[0]))
powerOf = 1
i = 0
if number >= 0 and number <= 31:
    while i <= number:
        print("2^", i, "=", powerOf)
        powerOf = 2 * powerOf
        i = i + 1
else:
    print("Please Enter The value Between 0 to 31")
