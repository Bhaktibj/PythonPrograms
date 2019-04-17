#  Check year is Leap Year or Not

print("Year, ensure it is a 4 digit number\n")
year = int(input("Enter the Year"))
year_str = str(year)     # Convert the Integer into String
length = len(year_str)     # Length of the String
if length == 4:       # check if the length of year_str is 4 or not
    if year % 4 == 0:
     print("Leap Year")
    else:
     print("Not Leap Year")
else:
 print("Please Enter The 4 Digit Year")

