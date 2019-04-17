import sys

from Week1.Algorithms.utility import day_of_week


def main():

    m = int(input("enter the month\n"))
    d = int(input("enter the day\n"))
    y = int(input("enter the year\n"))
    day_of_week(m, d, y)



if __name__ == "__main__":
    main()
