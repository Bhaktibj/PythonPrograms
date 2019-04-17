# User Input and Replace String Template “Hello <<UserName>>, How are you?”

username = str(input("Enter The UserName"))
length = len(username)  # length orf the string
if length < 3:  # Check if length of is minimum 3 or not.
    print("username length should be minimum three")
else:
    print("Before Replacement UserName")
    print("Hello " + username + " How Are You!!")
    print("After Replacement UserName")
username = username.replace(username, "Bhakti")  # Use the replace method and
# replace the string
print("Hello " + username + " How Are You!!\n")

username = str(input("Enter The Replace String"))  # Use the same variable name and replace that
print("Replace the String")
print("Hello" + username + " How Are You!!")
