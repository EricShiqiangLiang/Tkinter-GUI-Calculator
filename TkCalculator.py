# Calculator with GUI
# Tcl/Tk version 8.6.4
# python 3.5
# version 1.0 

from tkinter import *

# All the following functions updates display. display is a global variable.

# Updates display. Trigerd by button event. It adds the content of the button to the screen.
def updateDisplay(buttonString):
    content = display.get()
    if content == "0":
        content = ""
    display.set(content + buttonString)

# Calculates the result of expression and display the result
def calculate():
	try:
		result = eval(display.get())
		display.set(display.get() + '=\n' + str(result))
	except Exception:
		display.set("Error!")


# Clear screen, trigered by Clear button
def clear():
    display.set('0')
    cache.set('')

# Delete one character, trigerd by Delete button
def backspace():
    display.set(str(display.get()[:-1]))

# Defining main window，size:400×420，screen coordinates:(300,300)
mainUI = Tk()
mainUI.title('Simple Calculator')
mainUI.geometry('400x420+600+600')

# Setting display content. Defalut display is "0"
# Object StringVar belongs to Tkinter libray. It tracks the changes of a value
# to ensure any change in value can be displayed simultaneously
# Python cannot do this directly, so Tkinter definded many objects such as StringVar、BooleanVar、DoubleVar、IntVar。
display = StringVar()
display.set('0')


# Add display area, use label, set background color and size
textLabel = Label(mainUI)
textLabel.config(bg='grey', width=28, height=3, font = ("Calibri bold", 18), anchor = E)
textLabel['textvariable'] = display

# Set the position of display area in grid
textLabel.grid(row=0, column=0, columnspan=4)

# Add buttons
# Clear button，text is the text on the button，fg is the color of text（bg is the background color）
# width is the width of button
# command binds clearButton to clear function so it chan be trigered by pushing the button
clearButton = Button(mainUI, text = 'C', fg = '#EF7321', width = 10, height = 3, font = ("Calibri bold", 12), command = clear)
# Set position
clearButton.grid(row = 1, column = 0)

# Other buttons 
# Lambda is used because the passed arguments need to be proccessed
Button(mainUI, text = '<-', width = 10, height = 3, font = ("Calibri", 12), command = backspace).grid(row = 2, column = 2)
Button(mainUI, text = '÷', width = 10, height = 3, font = ("Calibri", 12), command = lambda:updateDisplay('/')).grid(row = 1, column = 3)
Button(mainUI, text = '*', width = 10, height = 3, font = ("Calibri", 12), command = lambda:updateDisplay('*')).grid(row = 2, column = 3)
Button(mainUI, text = '7', width = 10, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('7')).grid(row = 3, column = 0)
Button(mainUI, text = '8', width = 10, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('8')).grid(row = 3, column = 1)
Button(mainUI, text = '9', width = 10, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('9')).grid(row = 3, column = 2)
Button(mainUI, text = '-', width = 10, height = 3, font = ("Calibri", 12), command = lambda:updateDisplay('-')).grid(row = 3, column = 3)
Button(mainUI, text = '4', width = 10, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('4')).grid(row = 4, column = 0)
Button(mainUI, text = '5', width = 10, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('5')).grid(row = 4, column = 1)
Button(mainUI, text = '6', width = 10, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('6')).grid(row = 4, column = 2)
Button(mainUI, text = '+', width = 10, height = 3, font = ("Calibri", 12), command = lambda:updateDisplay('+')).grid(row = 4, column = 3)
Button(mainUI, text = '1', width = 10, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('1')).grid(row = 5, column = 0)
Button(mainUI, text = '2', width = 10, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('2')).grid(row = 5, column = 1)
Button(mainUI, text = '3', width = 10, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('3')).grid(row = 5, column = 2)
Button(mainUI, text = '=', width = 10, height = 7, bg = '#EF7321', font = ("Calibri bold", 12), command = lambda:calculate()).grid(row = 5, column = 3, rowspan = 2)
Button(mainUI, text = '0', width = 22, height = 3, font = ("Calibri bold", 12), command = lambda:updateDisplay('0')).grid(row = 6, column = 0, columnspan = 2)
Button(mainUI, text = '.', width = 10, height = 3, font = ("Calibri", 12), command = lambda:updateDisplay('.')).grid(row = 6, column = 2)
Button(mainUI, text = 'π', width = 10, height = 3, font = ("Calibri", 12), command = lambda:updateDisplay('3.141592654')).grid(row = 2, column = 1)
Button(mainUI, text = '^', width = 10, height = 3, font = ("Calibri", 12), command = lambda:updateDisplay('**')).grid(row = 2, column = 0)
Button(mainUI, text = '^2', width = 10, height = 3, font = ("Calibri", 12), command = lambda:updateDisplay('**2')).grid(row = 1, column = 1)
Button(mainUI, text = '√', width = 10, height = 3, font = ("Calibri", 12), command = lambda:updateDisplay('**0.5')).grid(row = 1, column = 2)
# main loop
mainUI.mainloop()