#Compares two elements and after each iteration places the largest value to it's correct postion
#1st iteration : Largest --- > last position
#2nd iteration : Second Largest ---> Second Last Position

import time

def bubble_sort(data, drawData, play):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(1/play)
    drawData(data, ['green' for x in range(len(data))])