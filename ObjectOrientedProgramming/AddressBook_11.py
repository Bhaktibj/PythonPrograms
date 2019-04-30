""" Create Object Oriented Analysis and Design of a simple Address Book .
"""

import pickle

def save():
       family_file = open("family.pickle","wb") # file is writing  binary mode
       pickle.dump(family,family_file) # family is pickle object and it save into family_file
       family_file.close()
def check():
       global family
       try:
           family_file = open("family.pickle","rb")
           family = pickle.load(family_file) #load the object from the file into family
       except IOError or EOFError: # input output file exception
           family = {} # Empty Dictionary
check()
ch = True
while ch:
       print("""
       Menu for Address Book:
       1. Add a contact
       2. Search for a contact
       3. Delete a contact
       4. Display all contact
       """)

       ch = int(input("What task would you like to do?"))
       print()
       if ch==1:

           first_name = input("Enter Your FirstName: ")
           last_name = input("Enter your LastName")
           mobile = int(input("Enter Your Mobile No: "))
           address = input("Enter your Address: ")
           city = input("Enter your city")
           pin_code =int(input("Enter your Pin Code"))
           email = input("Enter Your Email: ")
           family[first_name + last_name]=[address + city , pin_code , mobile , email ]
           save()
       elif ch==2:
           search = input("Who are looking for ? ")
           print()
           if search in family:
               print(search,":",family[search][0],",",family[search][1])
           else:
               print("")
       elif ch==3:
           rm = input("Who would you like to remove from address book")
           if rm in family:
                del family[rm]
           print("This person has been removed from the directory")
           save()
       elif ch==4:
           print()
           for val in sorted(family.items()):
               print(val)
       elif ch=="":
           print("invalid choice")
save()

