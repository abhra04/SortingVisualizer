import time 
import heapq 

def heapSort( arr , drawData , play ):
	n = len(arr)
	maxHeap  = []
	for item in arr:
		heapq.heappush(maxHeap , -item)
	temp = []
	color = ['red' for x in range(n)]
	drawData(arr, color)
	time.sleep(1/play)
	while maxHeap:
		t = -heapq.heappop(maxHeap)
		pos =[-x for x in maxHeap]
		arr = pos + [t] + temp
		color = ['gray'] + ['red' for x in range(1,len(pos))] +['blue'] +  ['green' for x in range( len(pos) + 1 , len(arr) )]
		#print(len(color))
		drawData(arr, color)
		time.sleep(1/play)
		temp = [t] + temp 
	color = ['green']*n
	drawData(arr, color)


	 