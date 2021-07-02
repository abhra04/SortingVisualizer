"""
Algorithm:
Select a pivot - > start iteration from the begining -> compare the value with pivot -> if less than pivot swap with border ->  at the end replace border with pivot-> recurse of the subarray left and right of pivit
Compleity -> O(nlogn) (Average)
             O(n2)  (Worst Case)
"""



import time 

def getMid(arr,left,right,drawData,play):
	pivot = arr[right]
	border = left  
	drawData(arr, getColorArray(len(arr), left, right, border, border,False))
	time.sleep(1/play)

	for i in range(left,right):
		if arr[i] < pivot:
			drawData(arr, getColorArray(len(arr), left, right, border, border,True))
			time.sleep(1/play)
			arr[border],arr[i] = arr[i],arr[border]
			border = border + 1 

		drawData(arr, getColorArray(len(arr), left, right, border, border,False))
		time.sleep(1/play)

	drawData(arr, getColorArray(len(arr), left, right, border, border,True))
	time.sleep(1/play)
	arr[border],arr[right] = arr[right],arr[border]
	return border






def quickSort(arr,left,right,drawData,play):
	if left>=right:
		return 
	mid = getMid(arr,left,right,drawData,play)
	quickSort(arr,left,mid - 1 ,drawData , play)
	quickSort(arr,mid + 1,right,drawData,play)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('pink')
        else:
            colorArray.append('orange')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'
        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray



'''
Testing:
	arr = [7,5,7,9,4,2]
	print(arr)

	quickSort(arr,0,len(arr) -1 , 0,0)

	print(arr)
'''