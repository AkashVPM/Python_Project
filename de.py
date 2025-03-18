import tkinter as tk

# Function to update the expression in the entry field
def press(num):
    current = entry_var.get()
    entry_var.set(current + str(num))

# Function to evaluate the expression
def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry field
def clear():
    entry_var.set("")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=calculate, bg="lightgreen")
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=clear, bg="red")
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda t=text: press(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
