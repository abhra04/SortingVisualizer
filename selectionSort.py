import time 

def selectionSort(arr,drawData,play):
	n = len(arr)
	for i in range(n):
		curr = i 
		color = ['green' for x in range(i)] + ['red' for x in range(i,n)]
		color[i] = 'blue'
		drawData(arr, color)
		time.sleep(1/play)
		for j in range(i+1,n):
			if arr[j] < arr[curr]:
				color[j] = 'white'
				drawData(arr, color)
				time.sleep(1/play)
				curr = j 

		color[curr] = 'gray'
		color[i] = 'gray'
		drawData(arr, color)
		time.sleep(1/play)
		arr[curr],arr[i] = arr[i],arr[curr]

	drawData(arr, ['green' for x in range(n)] )


"""
Testing:
	arr = [7,5,7,9,4,2]
	print(arr)

	selectionSort(arr,0, 0)

	print(arr)
"""