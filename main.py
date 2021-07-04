from tkinter import *
from tkinter import ttk
import random
from bubbleSort import *
from quickSort import *
from mergeSort import *
from insertionSort import *
from selectionSort import *
from heapSort import *

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(1500, 1500)
root.config(bg='black')

arr  = []


def drawData(data,colorArray):
    canvas.delete("all")
    if len(data)<=100:
        c_height = 500
        c_width = 1300
        x_width = c_width / (len(data) + 1)
        offset = 5
        spacing = 5
        normalizedData = [ i / max(data) for i in data]
        for i, height in enumerate(normalizedData):
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 480
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            canvas.create_rectangle(x0, y0, x1, y1, fill= colorArray[i] )
            canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
            #canvas.create_text(10, 20, anchor=SW, text='Operations :' + str(count) )  

        root.update_idletasks()
    else:
        c_height = 500
        c_width = 1300
        x_width = c_width / (len(data) + 1)
        offset = 5
        spacing = 2
        normalizedData = [ i / max(data) for i in data]
        for i, height in enumerate(normalizedData):
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 480
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            canvas.create_rectangle(x0, y0, x1, y1, fill= colorArray[i] )
            #canvas.create_text(10, 20, anchor=SW, text='Operations :' + str(count) ) 
        root.update_idletasks()


def startAlgorithm():
    global arr
    if not arr:
        return 
    if menu.get() == 'Quick Sort':
        quickSort(arr, 0, len(arr)-1, drawData, speed.get())
        drawData(arr, ['green' for x in range(len(arr))])

    elif menu.get() == 'Bubble Sort':
        bubbleSort(arr, drawData, speed.get())
        #drawData(arr, ['green' for x in range(len(arr))])

    elif menu.get() == 'Merge Sort':
        mergeSort(arr,0,len(arr) - 1 ,drawData, speed.get())
        #drawData(arr, ['green' for x in range(len(arr))])
    elif menu.get() == 'Insertion Sort':
        insertionSort(arr,drawData, speed.get())

    elif menu.get() == 'Selection Sort':
        selectionSort(arr,drawData, speed.get())

    elif menu.get() == 'Heap Sort':
        heapSort(arr,drawData, speed.get())




def gen():
    global arr
    minval = int(minVal.get())
    maxval = int(maxVal.get())
    size = int(inputSize.get())
    if minval > maxval:
        minval,maxval = maxval,minval 

    arr = []
    for _ in range(size):
        arr.append( random.randrange(minval , maxval + 1 )  )

    print(arr)
    drawData(arr,['red' for x in range(len(arr))] )





selected_alg = ''

canvas = Canvas(root, width=1310, height=500, bg='light blue')
canvas.grid(row=1, column=0, padx=2, pady=2)

UI_frame = Frame(root, width= 1300, height=300, bg='pink')
UI_frame.grid(row=2, column=0, padx=2, pady=2)


Label(UI_frame, text="Select Algorithm: ", bg='OliveDrab1',width=35,height=2).grid(row=2, column=1, padx=5, pady=5)
menu = ttk.Combobox(UI_frame, textvariable=selected_alg, width=65 , values=['Bubble Sort', 'Merge Sort','Quick Sort','Insertion Sort','Selection Sort','Heap Sort'])
menu.grid(row=2, column=2, padx=5, pady=5)
menu.current(0)
Button(UI_frame, text="Start Sorting", command= startAlgorithm ,width=35,height=2 ,  bg='orchid2').grid(row=2, column=3, padx=5, pady=5)

speed = Scale(UI_frame, from_ = 1, to =40  , length = 420 , digits = 1 , resolution=1, orient =HORIZONTAL , label = "Select Speed" )
speed.grid(row = 3 , column = 2 , pady = 3 )



inputSize = Scale(UI_frame, from_ = 1, to =300 , length = 420, resolution=1, orient =HORIZONTAL , label = "Array Size" )
inputSize.grid(row=4, column=1, padx=5, pady=5, sticky=W)


maxVal = Scale(UI_frame, from_ = 1, to =400  , length = 420, resolution=1, orient =HORIZONTAL , label = "Maximum Value" )
maxVal.grid(row=4, column=2, padx=5, pady=5, sticky=W)

minVal = Scale(UI_frame, from_ = 1, to =400  , length = 420, resolution=1, orient =HORIZONTAL , label = "Minimum Value" )
minVal.grid(row=4, column=3, padx=5, pady=5, sticky=W)


Button(UI_frame, text="Generate Array",width=35,height=2, command=gen, bg='SeaGreen1').grid(row=5, column=2, padx=5, pady=5)



root.mainloop()