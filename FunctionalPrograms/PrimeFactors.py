#  Number to find the prime factors

number = int(input("Enter the Number"))
for i in range(2, number, 1):
    while number % i == 0:
        print(i, end=" ")
        number = number / i
print()
