from Week1.FunctionalPrograms.Utilities.Utility import coupons


def main():
    try:
        inputNumber = int(input("Enter a distinct coupon number:"))
        list1 = [int(i) for i in str(inputNumber)]
        coupons(list1)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()