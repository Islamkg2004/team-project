
# Program description: A simple calculator using Tkinter.
# Updated on: November 17, 2026
# admin: Islam Syndanbekov,  Mekan Bayramov Diego baron, Ulises Valencia
# This program allows the user to perform basic math operations:
# addition, subtraction, multiplication, and division.

from tkinter import *

# Create the main application window.
root = Tk()

# Set the title of the calculator window.
root.title("Simple Calculator")

# Create an entry field where numbers and results are displayed.
# width sets the size, and borderwidth sets the border thickness.
e = Entry(root, width=35, borderwidth=5)

# Place the entry field in the first row and use three columns.
# padx and pady add space around the entry field.
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# This function displays the clicked number in the entry field.
def button_click(number):
    # Get the current text from the entry field.
    current = e.get()

    # Clear the entry field.
    e.delete(0, END)

    # Add the clicked number to the current text.
    e.insert(0, str(current) + str(number))

# This function clears everything from the entry field.
def button_clear():
    e.delete(0, END)

# This function saves the first number and selected operator.
def button_operator(operator):
    # Get the first number from the entry field.
    first_number = e.get()

    # Use global variables to save the number and operator.
    global f_num
    global num_operator

    # Convert the first number from a string to an integer.
    f_num = int(first_number)

    # Save the selected mathematical operator.
    num_operator = operator

    # Clear the entry field to enter the second number.
    e.delete(0, END)

# This function performs the calculation when the equal button is clicked.
def button_equal():
    # Get the second number from the entry field.
    second_number = e.get()

    # Clear the entry field before displaying the result.
    e.delete(0, END)

    # Check which operator was selected and perform the calculation.
    if num_operator == '+':
        # Add the first and second numbers.
        e.insert(0, f_num + int(second_number))

    elif num_operator == '*':
        # Multiply the first and second numbers.
        e.insert(0, f_num * int(second_number))

    elif num_operator == '/':
        # Divide the first number by the second number.
        e.insert(0, f_num / int(second_number))

    elif num_operator == '-':
        # Subtract the second number from the first number.
        e.insert(0, f_num - int(second_number))

    else:
        # Display an error message if the operator is invalid.
        e.insert(0, "Invalid!!!")

# Create buttons for numbers 0 through 9.
# Lambda functions call button_click() with the selected number.
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Create the addition button.
# When clicked, it calls button_operator() with "+".
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))

# Create the equal button to calculate the result.
button_equal = Button(root, text="   =   ", padx=79, pady=20, command=button_equal)

# Create the Clear button to clear the entry field.
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Create buttons for subtraction, multiplication, and division.
# Each button sends its operator to the button_operator() function.
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# Place all number and operation buttons in the calculator window.
# The grid() method determines the row and column of each button.

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Start the Tkinter event loop.
# This keeps the calculator window open and waits for user actions.
root.mainloop()
