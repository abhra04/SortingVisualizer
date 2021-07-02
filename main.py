from tkinter import *
from tkinter import ttk
import random
from bubbleSort import *

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 800)
root.config(bg='black')

arr  = []


def drawData(data,colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill= colorArray[i] )
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()


def Generate():
    global arr
    minval = int(minEntry.get())
    maxval = int(maxEntry.get())
    size = int(sizeEntry.get())
    if minval > maxval:
        minval,maxval = maxval,minval 

    arr = []
    for _ in range(size):
        arr.append( random.randrange(minval , maxval + 1 )  )

    drawData(arr,['red' for x in range(len(arr))])


def startAlgorithm():
    global arr
    bubble_sort(arr, drawData, speed.get())


selected_alg = StringVar()

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

UI_frame = Frame(root, width= 600, height=300, bg='grey')
UI_frame.grid(row=2, column=0, padx=10, pady=5)


Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=2, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort'])
algMenu.grid(row=2, column=1, padx=5, pady=5)
algMenu.current(0)
Button(UI_frame, text="Start Sorting", command= startAlgorithm , bg='red').grid(row=2, column=2, padx=5, pady=5)

speed = Scale(UI_frame, from_ = 1, to =20  , length = 200 , digits = 1 , resolution=1, orient =HORIZONTAL , label = "Select Speed" )
speed.grid(row = 3 , column = 1 , pady = 3 )



#Label(UI_frame, text="Size of the array", bg='grey').grid(row=4, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Scale(UI_frame, from_ = 1, to =200  , length = 200, resolution=1, orient =HORIZONTAL , label = "Array Size" )
sizeEntry.grid(row=4, column=1, padx=5, pady=5, sticky=W)



#Label(UI_frame, text="Minimum Value", bg='grey').grid(row=5, column=0, padx=5, pady=5, sticky=W)
minEntry = Scale(UI_frame, from_ = 1, to =200  , length = 200, resolution=1, orient =HORIZONTAL , label = "Minimum Value" )
minEntry.grid(row=5, column=1, padx=5, pady=5, sticky=W)



#Label(UI_frame, text="Maximum Value", bg='grey').grid(row=6, column=0, padx=5, pady=5, sticky=W)
maxEntry = Scale(UI_frame, from_ = 1, to =200  , length = 200, resolution=1, orient =HORIZONTAL , label = "Maximum Value" )
maxEntry.grid(row=6, column=1, padx=5, pady=5, sticky=W)




Button(UI_frame, text="Generate Array", command=Generate, bg='green').grid(row=7, column=1, padx=5, pady=5)



root.mainloop()