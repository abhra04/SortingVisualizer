"""
Algorithm:
Compares two elements and after each iteration places the largest value to it's correct postion
1st iteration : Largest --- > last position
2nd iteration : Second Largest ---> Second Last Position
"""
import time

def bubbleSort(arr, drawData, play):
    n = len(arr)
    count = 0 
    for _ in range(n-1):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                count = count + 1 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                drawData(arr, ['green' if x == j or x == j+1 else 'red' for x in range(n)]  )
                time.sleep(1/play)
    drawData(arr, ['green' for x in range(n)] )


'''
Testing:
    arr = [7,5,7,9,4,2]
    print(arr)

    bubbleSort(arr,0, 0)

    print(arr)
'''