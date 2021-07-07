import time 
import heapq 

def heapify(arr,n,i,drawData,play,x):
    largest = i 
    left = 2*i + 1 
    right = 2*i + 2 
    color = ['yellow']*n + ['green']*x
    color[i] = 'gray'
    if left<n:
    	color[left]='black'
    if right<n:
    	color[right] = 'white'
    drawData(arr, color)
    time.sleep(1/play)
    if left<n and arr[left]>arr[i]:
        largest = left
    if right<n and arr[right]>arr[largest]:
        largest = right
        
    if i!=largest:
        arr[i],arr[largest] = arr[largest],arr[i]
        color[i] = 'pink'
        color[largest] = 'pink'
        heapify(arr,n,largest,drawData,play,x)




def heapSort( arr , drawData , play ):
	n = len(arr)
	for i in range(n-1, -1, -1):
		heapify(arr, n, i,drawData ,play,0)

	x = 0 
	for i in range(n-1, -1, -1):
		color = ['red' for x in range(i)] + ['green' for x in range(i,n)]
		color[i] = 'blue'
		drawData(arr, color)
		time.sleep(1/play)
		arr[i], arr[0] = arr[0], arr[i] 
		color[i],color[0] = 'orange','orange'
		x = x + 1 
		heapify(arr, i, 0,drawData,play,x)
	drawData(arr, ['green' for x in range(n)] )


	 