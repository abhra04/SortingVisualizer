"""
Algorithm:
Go to the current element -> all the elements to right already sorted -> compare the correct element with all the elemenst to right untill you reach the end or find a greater element -> Insert the curent element in that position and move all the elements by 1
Complexity : O(n2)

"""




import time 

def insertionSort(arr,drawData,play):
	n = len(arr)
	for i in range(1,n):
		curr = arr[i]
		j =  i - 1 
		color = ['green' for x in range(i)] + ['red' for x in range(i,n)]
		color[i] = 'blue'
		drawData(arr, color)
		time.sleep(1/play)

		while j>=0 and arr[j] > curr:
			arr[j+1] = arr[j]
			color[j+1] = 'white'
			color[j] = 'white'
			j = j - 1 
			drawData(arr, color)
			time.sleep(1/play)


		arr[j + 1] = curr 
		color[j+1] = 'gray'
		color[i] = 'gray'
		drawData(arr, color  )
		time.sleep(1/play)

	drawData(arr, ['green' for x in range(n)] )



"""

arr = [7,5,7,9,4,2]
print(arr)

insertionSort(arr,0 , 0)

print(arr)

"""
