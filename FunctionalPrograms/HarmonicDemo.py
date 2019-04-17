#  Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N

number = int(input("Enter the Input"))
res = 0.0
i = 1
while i <= number:
    print("1/", i, "=")
    res = res+1/i
    i += 1
    print("The sum is", res)
