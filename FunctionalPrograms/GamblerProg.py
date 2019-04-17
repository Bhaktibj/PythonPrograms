
# Print Number of Wins and Percentage of Win and Loss o f a gambler

import random

stake = int(input("Enter the Stake\n"))
goal = int(input("Enter the goal\n"))
time = int(input("Enter the number times\n"))
bet = 0
loss = 0
win = 0
n = random.randint(0, 1)
for i in range(time):
    cash = stake
    while (cash != goal) and (cash != 0):
        bet += 1  # each time he wil place a bet until he reaches his goal
        if n < 0.5:
            cash += 1
        else:
            cash -= 1
        if cash == goal:  # gambler wins if he reaches its goal else loose
            win += 1
        else:
            loss += 1
print("total number of wins", win)
print("total number of loss", loss)
print("persantage of wins", (win / (win+loss)) * 100)
print("persantage of loss", (loss / (win+loss)) * 100)
