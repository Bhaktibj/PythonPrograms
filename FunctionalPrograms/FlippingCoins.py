# Find Percentage of head and tail

import random
tail = 0
head = 0
tailPerc = 0.0
headPerc = 0.0
count = 0
# randomNum = random.randint(0, 1)
flip = int(input("Enter the Flipping Coins"))
if flip < 0:
    print("Please check is it positive number ")
else:
    while count <= flip:
        randomNum = random.randint(0, 1) # random number between 0 to 1
        if randomNum < 0.5: # Checks if random number is less than 0.5
            tail += 1
        else:
            head += 1
        count += 1
print("flipping Coins", flip)
print("total count is =", count)
print("total of head is=", head)
print("total of tail is=",  tail)
headPerc = (head*100/flip)
print("Total percentage of head is=", headPerc, "%")
tailPerc = (tail*100/flip)
print("Total percentage of tail is=", tailPerc, "%")






























