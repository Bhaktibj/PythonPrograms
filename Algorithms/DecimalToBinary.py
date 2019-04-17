import sys
from Week1.Algorithms.utility import to_binary


def main():
    print("Enter the Decimal Number")
    d = int(input(sys.argv[0]))
    print("Decimal Number is=", d)
    to_binary(d)


if __name__ == "__main__":
    main()
