"""
Algorihtm:
Split the array into halves till all the numbers are in their own arrays -> compare the adjacent ones and keep sorting
Complexity -> O(nlogn) (avg and worst case)
"""


import time
 
count =  0 
def mergeSort(arr, left, right, drawData, play):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid, drawData, play)
        mergeSort(arr, mid+1, right, drawData, play)
        merge(arr, left, mid, right, drawData, play)
    else:
        return 

def merge(arr, left, mid, right, drawData, play):
    global count
    drawData(arr, getColorArray(len(arr), left, mid, right))
    time.sleep(1/play)

    leftPart = arr[left:mid+1]
    rightPart = arr[mid+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                count += 1 
                arr[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                arr[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        
        elif leftIdx < len(leftPart):
            arr[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            arr[dataIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    color = [0]*(len(arr))
    for i in range(len(arr)):
        if i>=left and i<=right:
            color[i] = 'green'
        else:
            color[i] = 'white'


    drawData(arr, color)
    time.sleep(1/play)
    count = 0 

def getColorArray(leght, left, mid, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= mid:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")

    return colorArray


'''
Testing:
    arr = [7,5,7,9,4,2]
    print(arr)

    quickSort(arr,0,len(arr) -1 , 0,0)

    print(arr)
'''