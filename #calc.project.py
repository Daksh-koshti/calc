#calc project
#lets make a calculator in python 
import tkinter

#calc setup
button_values = [
    ["C", "+/-", "%", "÷"], 
    ["7", "8", "9", "X"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "X", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row = len(button_values) #5
col = len(button_values[0]) #4

colour_green = "green"
colour_cyan = "cyan"
colour_black = "black"
colour_blue = "blue"
colour_purple = "purple"

#UI setup
UI = tkinter.Tk() #UI is the main window
UI.title("Calculator") #title of the window
UI.resizable(False, False) #disable resizing of the window
frame = tkinter.Frame(UI)
label = tkinter.Label(frame, text="Calculator", font=("Arial", 46), background = colour_black,    
                     foreground = colour_cyan)  #frame is the main window for the calculator

label.grid(row=0, column=0, columnspan=4, pady=10)
for column in range(col):
  value = button_values[row][column]
  button = tkinter.Button(frame, text=value, font=("Arial", 31), width=5, height=2, background = colour_blue, foreground = colour_black)
frame.pack()
UI.mainloop()


