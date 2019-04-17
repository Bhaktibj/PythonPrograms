#  Number to find the prime factors
# Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
number = int(input("Enter the Number"))
for i in range(2, number, 1):
    while number % i == 0:
        print(i, end=" ")
        number = number / i
print()
