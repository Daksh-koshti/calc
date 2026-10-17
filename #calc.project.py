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

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

colour_green = "green"
colour_cyan = "cyan"
colour_black = "black"
colour_blue = "blue"
colour_purple = "purple"

#UI setup
UI = tkinter.Tk() #UI is the main window
UI.title("calculator") #title of the window
UI.resizable(False, False) #disable resizing of the window
frame = tkinter.Frame(UI)
label = tkinter.Label(frame, text="0", font=("Arial", 46), background = colour_black,    
                     foreground = colour_cyan, anchor="e")  #frame is the main window for the calculator

label.grid(row=0, column=0, columnspan=column_count, sticky="nsew") #label is the title of the calculator
for row in range(row_count):
  for column in range(column_count):
    value = button_values[row][column]
    button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count-1, height=1,
                                               
                            command=lambda value=value: button_click(value)) #button is the button for the calculator
    
    button.grid(row=row+1, column=column, sticky="nsew")
frame.pack()
def button_click(value):
  pass
UI.mainloop()


