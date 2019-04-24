
# program to print the two dimensional array or list

rows = int(input("Enter row size \n"))
col = int(input("Enter column size \n"))
two_d_array = [[0 for i in range(col)] for j in range(rows)]
print("Enter the Elements of the list")
for i in range(rows):
    for j in range(col):  # loop for creating the list elements during run time
        tow_d_array[i][j] = int(input())
print(two_d_array)
