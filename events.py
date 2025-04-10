import tkinter as tk

window = tk.Tk()

# def handle_keypress(event):
#     print(event.char) #can do .char for just characters

# window.bind("<Key>", handle_keypress)  #listens for every time a key is pressed (loop)

# def handle_click(event):
#     print("The button was clicked!")
#     print(event)

# button = tk.Button(text="Click me!",)
# button.pack()

# button.bind("<Button-1>", handle_click) #button-1 is a left click #what you binded to determines how it responds (not window)
#commenting out is ctrl + forward slash
def increase():
    value = int(lbl_value["text"]) #the label currently
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"]) #the label currently
    lbl_value["text"] = f"{value - 1}"

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0,1,2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew") #nsew expand to fill in all four directions

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1,)

btn_increase = tk.Button(master=window, text="+", command=increase) #command gives function we want it to run; only applicable to buttons
btn_increase.grid(row=0, column=2, sticky="nsew")



window.mainloop()