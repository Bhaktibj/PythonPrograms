from Week1.Algorithms.utility import monthly_payment


def main():

    p = int(input("Enter the principle amount"))
    y = int(input("Enter the duration in year"))
    r = int(input("Enter the rate of interest"))
    print("Payment is=", monthly_payment(p, y, r))


if __name__ == "__main__":
    main()



