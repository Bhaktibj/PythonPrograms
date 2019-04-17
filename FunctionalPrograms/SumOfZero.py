# Sum of three Integer adds to ZERO


arr = [-25, -10, -7, 3, 2, 4, 8, 10, 9, -3, -6]  # Array Elements
for i in range(0, len(arr) - 1):
    for j in range(i + 1, len(arr) - 1):
        for k in range(i + 2, len(arr) - 1):
            s = arr[i] + arr[j] + arr[k]
            if s == 0:
                print(arr[i], arr[j], arr[k])
