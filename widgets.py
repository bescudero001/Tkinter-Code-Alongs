import tkinter as tk # .py is python file

window = tk.Tk() # Tk is the Class from tkinter module
window.title("Prof. Kuznicki's App")

label1 = tk.Label(
    master=window, 
    text="Hallo? Is anybody out there?",
    foreground="white", # can use hex codes
    background="#34A2FE",
    width=20, #0 is not as wide as it is tall
    height=10,
    ) # window is master object
label1.pack() # pack is geometry manager

button1=tk.Button(
    master=window,
    text="Do not press this button.",
    fg = "blue", #shortened version of foreground
    bg = "red",
)
button1.pack()

entry1 = tk.Entry(master=window,)
entry1.pack()

entry1.insert(0, "This is a random entry.") #index begins at 0
entry1.insert(0, "Hi! ") #before line 27

some_text = entry1.get() 
print(some_text) #appears in terminal

entry1.delete(0)
entry1.delete(0,2) #deletes only in window, but not terminal
entry1.delete(0, tk.END) #deletes all
#use hashtags with ctrl, slash
#
text_box = tk.Text()
text_box.pack()

text_box.insert("1.0", "Wassup") #1 = line, 0 = first character
text_box.insert("2.0", "\nNothin much") #if line 2 doesn't exist, will add things to last line that has text, hence line 1; \n adds new line
text_box.insert(tk.END, "Toodles!") #added at last line that has text
text_box.insert(tk.END, "\nOkay, actually toodles this time!")

text = text_box.get("1.0")
print(text) # gets first char in line 1 to terminal
text = text_box.get("2.0","2.5")
print(text)
text = text_box.get("1.0",tk.END)
print(text)

text_box.delete("1.0") #deletes only character
text_box.delete("1.0","1.5")
text = text_box.get("1.0")
print(text) #terminal empty b/c of deleting
text_box.delete("1.0") #actually deletes line
text_box.delete("1.0", tk.END)
#
frame1 = tk.Frame()
frame2 = tk.Frame()

label1 = tk.Label(master=frame1, text="Dis is frame 1!",bg="red")
label1.pack()

label2 = tk.Label(master=frame2, text="And dis is frame 2!",bg="blue")
label2.pack()


frame1.pack()
frame2.pack() # empty b/c nothings contained in them
#
bordereffects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for relief_name, relief1 in bordereffects.items(): #.items gives key-value pair
    frame = tk.Frame(master=window, relief=relief1, borderwidth=5) #relief is a keyword #framesize doesn't affect height
    frame.pack(side=tk.LEFT) #side by side instead of upside down
    label = tk.Label(master=frame, text=relief_name) #calling dictionary keys
    label.pack()



#
window.mainloop() # loop that keeps running until window 