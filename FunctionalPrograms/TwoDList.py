# 13th program
# program to print the two dimensional list

rows = int(input("Enter the rows\n"))
col = int(input("Enter the columns\n"))
a = [[0 for i in range(col)] for j in range(rows)]
print("Enter the Elements of the list")
for i in range(rows):
    for j in range(col):  # loop for creating the list elements during run time
        a[i][j] = int(input("Enter the Elements"))
for i in range(rows):
    for j in range(rows):  # loop for printing the  2d-list
        print(a[i][j], end=" ")
