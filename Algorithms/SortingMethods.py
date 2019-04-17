from Week1.Algorithms.utility import binay_search_integer, binay_search_string ,insertion_sort_integer,\
    insertion_sort_string, bubble_sort_integer, bubble_sort_string


def main():

    n = int(input("Enter the size of list\n"))
    ch = int(input("Enter the Choice"))
    if ch == 1:
        binay_search_integer(n)
    elif ch == 2:
        binay_search_string(n)
    elif ch == 3:
        insertion_sort_integer(n)
    elif ch == 4:
        insertion_sort_string(n)
    elif ch == 5:
        bubble_sort_integer(n)
    elif ch == 6:
        bubble_sort_string(n)
    else:
        print("Enter the Valid Choice")

if __name__ == '__main__':
    main()