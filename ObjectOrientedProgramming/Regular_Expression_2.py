""" Regular Expression Demonstration
I/P -> read in the Message
Logic -> Use Regex to do the following
Replace <<name>> by first name of the user ( assume you are the user)
replace <<full name>> by user full name.replace any occurance of mobile number
that should be in format 91-xxxxxxxxxx by your contact number.
replace any date in the format XX/XX/XXXX by current date.
O/P -> Print the Modified Message.
"""

import re     # re is  python module
import datetime

class RegularExpression:

    def regex_function(self):
       string = "  Hello <<user-name>>,we have your full name as <<full-name>> in our system."
       first_name = input("Enter your first name: ")
       string_one = re.sub("<<user-name>>", first_name,string) # sub method is used to replace the text.
       full_name = input("Enter your full name: ")
       string_two = re.sub("<<full-name>>", full_name,string_one)
       # print(string_two,"\n")
       try:
           contact_string = "Your contact number is 91-xxxxxxxxxx."
           mobil_number = int(input("Enter Your Mobile Number: "))
           new_mobile_num = str(mobil_number)
           new_string = re.sub("xxxxxxxxxx", new_mobile_num, contact_string)
           # print(new_string, "\n")
       except ValueError:
           print("Enter the data in number\n")
       date_string = "please, let us know in case of any clarification Thank you BridgeLabs,on <<Today>>-XX/XX/XXXX. "

       date = datetime.date.today() # date.today is display the today date
       replace_date = str(date)
       day = date.strftime("%A") # this method is used to display the day in full name .
       day1 = re.sub("<<Today>>", day, date_string)
       bridge_lab = re.sub("XX/XX/XXXX", replace_date, day1)
       # print(bridge_lab, "\n")
       print("Complete String")
       print(string_two , new_string)
       print(bridge_lab)
object1 = RegularExpression()
if __name__ == '__main__':
    try:
        object1.regex_function()
    except UnboundLocalError:
        print("try again by entering the valid data")
