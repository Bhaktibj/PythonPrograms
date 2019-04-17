import math
import time

# **********************************************************************************************
# anagram detection program

def anagram_func():
    temp = 0
    str1 = str(input("Enter the 1st string\n"))
    str2 = str(input("Enter the 2nd string\n"))
    str3 = str1.upper()
    str4 = str2.upper()
    if len(str1) == len(str2): # check the length of string is equal or not0
        for i in range(0, len(str3)):
            for j in range(0, len(str4)):
                if str3[i] == str4[j]:
                    temp += 1
                    break
        if len(str1) == temp:
            print(str1, "Is anagram of", str2)
        else:
            print(str1, "is not a anagram of ", str2)
    else:
        print("string are not anagram")


# **********************************************************************************************************************
# Check the given input number is Prime or Not

def check_prime(n):
    count = 0
    for i in range(2, (n - 1)):  # 1 and number itself should not be included because
        # that applies for every number
        if n % i == 0:
            count += 1  # count increases  for every i dividing n

    if count == 0:
        print("number is a prime number")
    else:
        print("number is not a prime number")


# **********************************************************************************************************************
# Find the Prime numbers to given range

def prime_num():
    list1 = [ ]
    for i in range(1000):  # Traverse each number in the interval \
        # with the help of for loop
        if i == 0 or i == 1:
            continue
        flag = True  # flag variable to tell if i is prime or not
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            list1.append(i)
    return list1


# **********************************************************************************************************************
# Using above function and find the anagram prime numbers

def anagram_prime():
    x = prime_num()
    x = [ str(i) for i in x ]
    anagram = [ ]
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if sorted(x[ i ]) == sorted(x[ j ]):
                anagram.append((x[ i ]))
                anagram.append(x[ j ])
    return anagram


# **********************************************************************************************************************
# Function to convert fahrenheit to celsius and vice-versa

def temp_conversion(temp):
    print("Convert celsius to fahrenheit ")
    f = temp * 9 / 5 + 32
    print("Convert Fahrenheit  to Celsius")
    c = f - 32 * 5 / 9
    return f, c


# **********************************************************************************************************************
# Function to check the day of the week of given date

def day_of_week(m, d, y):
    list1 = [ "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday" ]
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2  # formulas given in the question
    d0 = (d + x + 31 * m0 // 12) % 7  # this formula will generate values b/w 0 to 6
    print(list1[ d0 ])  # printing the list


# **********************************************************************************************************************
# to calculate monthly payment for r interest and p principal for y years

def monthly_payment(p, y, r):
    n = 12 * y  # Convert into years in month
    rm = r / (12 * 100)
    payment = p * rm / 1 - (1 + rm) * math.pow((1 + rm), (-n))
    return payment


# **********************************************************************************************************************
# Function to find the square root of given number

def sqrt_root(c):
    if c < 0:
        print("Enter the Non-negative Number")
    else:
        t = c
        t = ((t / c) + t) / 2
        epsilon = 1e-15
        while abs(t - c / t) > epsilon:  # repeat until desired accuracy reached
            t = (c / t + t) / 2.0
        return t


# **********************************************************************************************************************
# Function to convert decimal to binary

def to_binary(number):
    result = ""
    while number != 0:
        remainder = number % 2  # gives the exact remainder
        number = number // 2  # quotient will be again used as a number
        result = str(remainder) + result
    print("The binary representation is", result)


# **********************************************************************************************************************

# nibble Function to convert binary to Decimal

def to_decimal(num):
    while len(str(num)) < 8:
        num = num + str(0)

    s3 = num[ 4:8 ]
    s4 = num[ 0:4 ]
    swap = s3 + s4
    b = str(swap)
    print(swap)


# **********************************************************************************************************************
# note vending machine

def note_machine(rupees):
    a = [1000, 500, 100, 50, 10, 5, 2, 1]  # create a list of notes in descending
    # orders
    note = 0
    for i in range(0, len(a)):
        if rupees / a[ i ] > 0:
            print("no. of notes of ", a[i], " is ", rupees / a[ i ])
            # remainder will give no. of notes
            note = note + (rupees / a[i])
            rupees = rupees % a[i]  # quotient will give next value of rupees
    print("no. of notes are " + str(note))


# **********************************************************************************************************************
# Bubble Sort Implementation

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Traverse through all array element
        # Last i elements are already in place
        for j in range(0, n - i - 1):  # traverse the array from 0 to n-i-1

            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Sorted array is:")
    for i in range(len(arr)):
        print(arr[ i ])


# **********************************************************************************************************************
# Insertion Sort Implementation

def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n):
        j = i
        temp = arr[ i ]
        while j > 0 and temp < arr[ j - 1 ]:
            arr[ j ] = arr[ j - 1 ]
            j = j - 1
        arr[ j ] = temp
    print("Sorted array is:")
    for i in range(len(arr)):
        print(arr[i])


# **********************************************************************************************************************
# Python program for implementation of MergeSort

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # creating two temp variables
        R = arr[mid:]  # for left half and the right half

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]  # here left array elements will be assigned to
                # original array
                i += 1
            else:
                arr[k] = R[j]  # here right array elements will be assigned
                # to original array
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):  # again checking if any element is left or not
            arr[k] = R[j]
            j += 1
            k += 1
    print("Sorted array is:")
    for i in range(len(arr)):
        print(arr[i])


# **********************************************************************************************************************
# program to binary search a word from the word list

def file():
    print("input the string you want to search")
    name = input()  # enter the string you want to search from the text file
    f = open("test1.txt", "r").readline()  # this function will open the txt file and read it

    if name in f:  # if the required string is present inside loop satisfies
        print("string is present")  # or the string is not present
    else:
        print("string is not present")


# **********************************************************************************************************************

# program for different sorting methods for integers and strings

# *****************************************Binary Search Integer*************************************************

def binay_search_integer(n):
    start1 = time.time()  # start method to start the timer
    flag = 1
    print("Enter the array elements")
    arr = [int(input()) for i in range(n)]  # input the list elements during the run
    # time
    x = len(arr)
    key = int(input("Enter the Key to search"))
    start = 0
    end = x - 1
    arr.sort()  # sort function to sort the list
    print("Sorted Array", arr)
    while start <= end:
        mid = (start + end) // 2  # will give the middle value
        if key == arr[mid]:
            flag = 0
            print("Element is found at the location", mid)
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if flag == 1:
        print("Element Not Found")
    stop1 = time.time()  # stop method to stop the timer for checking method run time
    elapsed_time = stop1 - start1  # function to check the elapsed time of method
    print("Elapsed time is", elapsed_time)


# *************************************************Binary Search String*************************************************
def binay_search_string(n):

    start1 = time.time()  #  start the timer for checking method run time
    flag = 1
    print("Enter the String array elements")
    arr = [str(input()) for i in range(n)]
    x = len(arr)
    key = str(input("Enter the Key to search"))  # enter the element you want to search
    start = 0
    end = x - 1  # sort function to sort the list
    arr.sort()
    print("Sorted Array", arr)
    while start <= end:
        mid = (start + end) // 2
        if key == arr[mid]:
            flag = 0
        print("Element is found at the location", mid)
        if key < arr[ mid ]:
            end = mid - 1
        else:
            start = mid + 1
    if flag == 1:
        print("Element Not Found")
    stop1 = time.time()  # to stop the timer for checking method run time
    elapsed_time = stop1 - start1  # to check the elapsed time of method
    print("Elapsed time is", elapsed_time)


#  ***********************************Insertion Sort Integer*******************************************
def insertion_sort_integer(n):

    start1 = time.time()  # start the timer for checking method run time
    print("Enter the Elements in the array")
    arr = [int(input()) for i in range(n)]
    x = len(arr)
    for i in range(1, n):
        j = i
        temp = arr[ i ]
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp
    print("Sorting Elements are")
    for i in range(0, n):
        print(arr[ i ])
    stop1 = time.time()  # stop the timer for checking method run time
    elapsed_time = stop1 - start1  # to check the elapsed time of method
    print("Elapsed time is", elapsed_time)

# ************************************Insertion Sort String*************************************************
def insertion_sort_string(n):

    start1 = time.time()  # start function to start the timer
    print("Enter the Elements in the array")
    arr = [(input()) for i in range(n)]  # creating a string list by giving input
    x = len(arr)
    for i in range(1, n):
        j = i
        temp = arr[i]
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp
    print("Sorting Elements are")
    for i in range(0, n):
        print(arr[i])
    stop1 = time.time()  # to stop the timer for checking method run time
    elapsed_time = stop1 - start1  # function to check the elapsed time
    print("Elapsed time is", elapsed_time)


# *************************************************Bubble Sort Integer*************************************************
def bubble_sort_integer(n):
    start1 = time.time()  # start function to start the timer
    print("Enter the Elements in the array")  # creating the integer list
    arr = [int(input()) for i in range(n)]
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[ j ]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print("Sorted Array is")
    for i in range(0, n):
        print(arr[i])
    stop1 = time.time()  # to stop the timer for checking method run time
    elapsed_time = stop1 - start1  # to check the elapsed time of method
    print("Elapsed time is", elapsed_time)


# ************************************************Bubble Sort String****************************************************

def bubble_sort_string(n):
    start1 = time.time()  # start function to start the timer
    print("Enter the String Elements in the array")
    arr = [(input()) for i in range(n)]  # creating the string list for bubble sort
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[ j ]
                arr[ j ] = arr[j + 1]
                arr[j + 1] = temp
    print("Sorted Array is")
    for i in range(0, n):
        print(arr[i])
    stop1 = time.time()  # to stop the timer for checking method run time
    elapsed_time = stop1 - start1  # to check the elapsed time
    print("Elapsed time is", elapsed_time)


# **********************************************************************************************************************

# program to check a number is a palindrome or not

def check_palindrom(num):
    temp = num
    rev = 0

    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10

    if num == rev:
        print("number is palindrome")
    else:
        print("number is not palindrome")


# **********************************************************************************************************************

# Question to find your number

def to_number(first, last):
    res = last - first
    if res == 1:  # loop will return the first number if difference is 1
        return first
    mid = first + (last - first) / 2  # finding the mid value for further process
    print("is the number less than ", mid, "if yes press 1 else press 0")
    n = int(input())
    if n == 1:  # pressing 1 means yes and pressing 0 means switching to next condition
        return to_number(first, mid)
    elif n == 0:
        return to_number(mid, last)
    else:
        print("enter the valid value")

# **********************************************************************************************************************
