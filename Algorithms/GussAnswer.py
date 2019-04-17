from Week1.Algorithms.utility import to_number

def main():

     n = int(input("how many questions you want to be asked?\n"))
     first = 0
     last = int(2**n)
     print("think of any number between", first, "and", last)
     print(to_number(first, last))


if __name__ == '__main__':
    main()