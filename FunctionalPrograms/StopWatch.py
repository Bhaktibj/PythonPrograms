# program for using stopwatch , and to check the elapsed time..

import time

try:
    start_time = 0
    stop_time = 0
    start_time = int(input("Enter 0 to start"))
    if start_time == 0:
        start_time = time.time()
        stop_time = int(input("Enter 1 to stop"))
        if stop_time == 1:
            stop_time = time.time()
            elapsed_time = stop_time - start_time
            print("Elapsed time is=", elapsed_time)
except Exception as e:
    print("Enter The valid Values")
