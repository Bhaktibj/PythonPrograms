import numpy as np
import random

# init to play tic-tac-toe game

def tic_tac_toe():
    arr = np.zeros((3, 3))
    player = int(input("If you want to play first then enter 1 else 2. "))
    cnt = 0
    while cnt < 9:
        if player == 1:
            show_game(arr)
            player_call(arr)
            cnt += 1
            player = 2
            if win_check(arr, 'X') == -1:
                player = -1
            elif player == 2:
                computer(arr)
                cnt += 1
                player = 1
                if win_check(arr, 'O') == -1:
                    player = -1
                else:
                    show_game(arr)
                    break

# Show the tic-tac-toe game

def show_game(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if int(arr[i][j]) != 0:
                print(chr(int(arr[i][j])), end=" ")
            else:
                print("-", end=" ")
print()

# This method for user player to play tic-tac-toe
# First will get position from player to marked X

def player_call(arr):
    print("Enter position with x and y co-ordinate")
    posX, posY = int(input()), int(input())
    # while True:
    if arr[posX][posY] == 0:
        arr[posX][posY] = ord('X')
    else:
        print("This position already marked.")
        show_game(arr)
        player_call(arr)

# This method for computer player
# Generate position and then marked O

def computer(arr):
    while True:
        posX = random.randrange(0, 3, 1)
        posY = random.randrange(0, 3, 1)
        if arr[posX][posY] == 0:
            arr[posX][posY] = ord('O')
            break

# Check to who won the tic-tac-toe game

def win_check(arr, ch):
    c = ord(ch)
    if (arr[0][0] == c and arr[0][1] == c and arr[0][2] == c) \
            or (arr[1][0] == c and arr[1][1] == c and arr[1][2] == c) \
            or (arr[2][0] == c and arr[2][1] == c and arr[2][2] == c) \
            or (arr[0][0] == c and arr[1][0] == c and arr[2][0] == c) \
            or (arr[0][1] == c and arr[1][1] == c and arr[2][1] == c) \
            or (arr[0][2] == c and arr[1][2] == c and arr[2][2] == c) \
            or (arr[0][0] == c and arr[1][1] == c and arr[2][2] == c) \
            or (arr[0][2] == c and arr[1][1] == c and arr[2][0] == c):
        if ch == 'X':
            print("Player won")
            return -1
        else:
            print("Computer won")
            return -1


if __name__ == '__main__':
    tic_tac_toe()
