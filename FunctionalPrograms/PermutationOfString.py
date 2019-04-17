from Week1.FunctionalPrograms.Utilities.Utility import permutation


def main():
    string = input("enter the string")  # getting the string from the user
    n = len(string)  # getting the length of the user-input string
    s = list(string)  # converting the string to list to get the indexes
    # of the string to swap the letters of it
    permutation(s, 0, n - 1)


if __name__ == '__main__':
    main()