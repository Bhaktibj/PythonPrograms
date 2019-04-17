import  random
# program to generate a random coupon number
def coupons(list1):
    count = 0               # starting the count resulting from the loop
    while len(list1) > 0:
        x = random.randint(0, 9)  # generate number between 0-9 using random function
        count += 1                   # increment count
        if x in list1:                 # check x is present in list or not
            list1.remove(x)         # if matched then remove that
        print(x)
    print("Total random number needed to have all distinct numbers:", count)

#***************************************************************************************

# permutation of a string
def permutation(s, l, r):
    if l == r:                   # checking whether string is of single character or not
        print(''.join(s))        # then printing the given string as it is
    else:
        for i in range(l, r+1):
            s[l], s[i] = s[i], s[l]
            permutation(s, l+1, r)      # recursion of the function
            s[l], s[i] = s[i], s[l]  # swap back, for the next loop


