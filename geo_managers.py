import tkinter as tk

window = tk.Tk()

# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) #fill=tk.X FILLS window from left to right; width is unneeded

# frame2 = tk.Frame(master=window, width=50, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) #side=tk.LEFT stacks from the left to right; fill=tk.Y FILLS window from top to bottom; height is unneeded

# frame3 = tk.Frame(master=window, width=25, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) #expand=True makes them the same size; fill=tk.BOTH applies to all frames


#
# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()

# label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
# label1.place(x=0,y=0) #place() specifies where (x,y); label's TOP LEFT CORNER is placed at (x,y)

# label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="red")
# label2.place(x=75,y=75)


#making a grid
for i in range(3): #outerloop is rows
    window.columnconfigure(i, weight=1, minsize=75) #parameters are index, weight, minimum size
    window.rowconfigure(i, weight=1, minsize=50) #the grid expands
    

    for j in range(3): #innerloop is columns
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
        )
        frame.grid(row=i, column=j, padx=5, pady=5) #pad is pixels around frame
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5) #pixels around label



#
window.columnconfigure(0, minsize=250)
window.rowconfigure([0,1], minsize=100) #give a list of indexes for more than one row

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="n") #sticky= determines what direction object sticks to; uses cardinal directions: n, s, ne, sw, etc...


label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="n")


#
window.rowconfigure(0,weight=1,minsize=50)
window.columnconfigure([0,1,2,3],weight=1,minsize=50) #minimum size is default, first size before expanding window

label1=tk.Label(text="1", bg="black", fg="white")
label2=tk.Label(text="2", bg="black", fg="white")
label3=tk.Label(text="3", bg="black", fg="white")
label4=tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew") #all four directions


#
window.mainloop()