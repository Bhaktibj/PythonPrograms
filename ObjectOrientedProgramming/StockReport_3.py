""" Stock Report
Desc -> Write a program to read in Stock Names, Number of Share, Share Price.
Print a Stock Report with total value of each Stock and the total value of Stock.
"""

from colored import fg, attr
class StockData:               # Stock data class is using to create the stock reports
    def __init__(self):
        self.number_of_shares = 0
        self.share_price = 0
        self.stock_total_value = 0
    def stock_data(self):
        try:
            number_of_stocks = int(input("Enter Number of stock details: "))
            number = 1
            for stock_details in range(number_of_stocks):
                print("stock number =",number)
                stock_name = input("Enter the stock name: ")
                self.number_of_shares = int(input("Enter the number of shares: "))
                self.share_price = int(input("Enter the share price: "))
                print("_____________________________________________________________________________________")
                print("print the stock details are as follows\n")
                print("Stock Name:",stock_name,"\nNumber of Shares: ",self.number_of_shares,"\nShare Price: ",self.share_price)
                number += 1
                stock_value = self.number_of_shares * self.share_price # calculate the stock value.
                self.stock_total_value += stock_value  # calculate total stock value
                print("")
                print("stock value of",stock_name,"=",stock_value)
                print("")
        except ValueError:
            print('%sEnter the valid data%s' % (fg(1), attr(0))) # this is display the text in red color format
        print("The Total value of Stock = ",self.stock_total_value)

class StockValues(StockData):
    def __init__(self):
      self.stock_data_obj = StockData()
    def stock_values(self):
        self.stock_data_obj.stock_data()
stock_value_object = StockValues()
if __name__ == '__main__':
    try:
        stock_value_object.stock_values() # Call the method
    except UnboundLocalError:
        print("\033[1;32;40m Bright Green  \n")
        print("Enter the valid data")









