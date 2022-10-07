import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is the function called when the button is clicked
def btnClickFunctionq():
	# This is the section of code which creates the a label
	Label(root, text='ETS wird gestartet!', bg='#3D3D3D', font=('arial', 12, 'normal')).place(x=8, y=61)


# this is the function called when the button is clicked
def btnClickFunctionw():
	# This is the section of code which creates the a label
	Label(root, text='Creating better GUI and polishing it, ETS AddOn, ETS Telemetry', bg='#3D3D3D', font=('arial', 12, 'normal')).place(x=8, y=61)


# this is the function called when the button is clicked
def btnClickFunctione():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunctionr():
	print('clicked')


# this is the function called when the button is clicked
def btnClickFunctiont():
	print('clicked')


# this is the function called when the button is clicked
def eksit():
	exit(0)


# this is the function called when the button is clicked
def osterei():
	print('Attacked by the dead men!')



root = Tk()

# This is the section of code which creates the main window
root.geometry('890x570')
root.configure(background='#4A4A4A')
root.title('Speck🥓-Frau👩🏻')


# This is the section of code which creates a button
Button(root, text='ETS', bg='#008B00', font=('arial', 12, 'normal'), command=btnClickFunctionq).place(x=8, y=11)


# This is the section of code which creates a button
Button(root, text='Aufträge', bg='#008B00', font=('arial', 12, 'normal'), command=btnClickFunctionw).place(x=78, y=11)


# This is the section of code which creates a button
Button(root, text='Gehlt', bg='#008B00', font=('arial', 12, 'normal'), command=btnClickFunctione).place(x=178, y=11)


# This is the section of code which creates a button
Button(root, text='Kontor', bg='#008B00', font=('arial', 12, 'normal'), command=btnClickFunctionr).place(x=258, y=11)


# This is the section of code which creates a button
Button(root, text='Spedi', bg='#008B00', font=('arial', 12, 'normal'), command=btnClickFunctiont).place(x=348, y=11)


# This is the section of code which creates a button
Button(root, text='.', bg='#3D3D3D', font=('arial', 1, 'normal'), command=osterei).place(x=878, y=1)

# This is the section of code which creates a button
Button(root, text='Exit', bg='#8B1A1A', font=('arial', 12, 'normal'), command=eksit).place(x=838, y=11)


root.mainloop()
