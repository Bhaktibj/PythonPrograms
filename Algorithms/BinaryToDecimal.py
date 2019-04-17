import sys
from Week1.Algorithms.utility import to_decimal


def main():
    print("Enter the Binary Number")
    d = str(input(sys.argv[0]))
    print("Decimal Number is=", d)
    to_decimal(d)


if __name__ == "__main__":
    main()