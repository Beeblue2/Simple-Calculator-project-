import tkinter

field_text = ""


def add_to_field(sth):
    global field_text
    # Allows numbers to change from 0 to an entered number if there's only one 0 on the screen
    if len(field_text) == 1 and field_text[0] == "0":
        field_text = ""
    field_text = field_text + str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)


def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)


def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")


def delete():
    global field_text
    field_text = field_text[0:-1]
    # If there is nothing else to delete, insert a 0 on further attempts to delete
    if field_text == "":
        field_text = "0"
    field.delete("1.0", "end")
    field.insert("end", field_text)


root = tkinter.Tk()
root.title("Cal app")

root.geometry("300x300")
field = tkinter.Text(root, height=2, width=21, font=("This New Roman", 20), bg="grey")
field.grid(row=1, column=1, columnspan=4)

b1 = tkinter.Button(root, text="1", command=lambda: add_to_field(1), width=5, font=("Times New Roman", 14))
b1.grid(row=5, column=1)

b2 = tkinter.Button(root, text="2", command=lambda: add_to_field(2), width=5, font=("Time New Roman", 14))
b2.grid(row=5, column=2)

b3 = tkinter.Button(root, text="3", command=lambda: add_to_field(3), width=5, font=("Time New Roman", 14))
b3.grid(row=5, column=3)

b4 = tkinter.Button(root, text="4", command=lambda: add_to_field(4), width=5, font=("Time New Roman", 14))
b4.grid(row=4, column=1)

b5 = tkinter.Button(root, text="5", command=lambda: add_to_field(5), width=5, font=("Time New Roman", 14))
b5.grid(row=4, column=2)

b6 = tkinter.Button(root, text="6", command=lambda: add_to_field(6), width=5, font=("Time New Roman", 14))
b6.grid(row=4, column=3)

b7 = tkinter.Button(root, text="7", command=lambda: add_to_field(7), width=5, font=("Time New Roman", 14))
b7.grid(row=3, column=1)

b8 = tkinter.Button(root, text="8", command=lambda: add_to_field(8), width=5, font=("Time New Roman", 14))
b8.grid(row=3, column=2)

b9 = tkinter.Button(root, text="9", command=lambda: add_to_field(9), width=5, font=("Time New Roman", 14))
b9.grid(row=3, column=3)

b0 = tkinter.Button(root, text="0", command=lambda: add_to_field(0), width=5, font=("Time New Roman", 14))
b0.grid(row=6, column=1)

but_plus = tkinter.Button(root, text="+", command=lambda: add_to_field("+"), width=5, font=("Time New Roman", 14))
but_plus.grid(row=3, column=4)

but_minus = tkinter.Button(root, text="-", command=lambda: add_to_field("-"), width=5, font=("Time New Roman", 14))
but_minus.grid(row=4, column=4)

but_multiply = tkinter.Button(root, text="*", command=lambda: add_to_field("*"), width=5, font=("Time New Roman", 14))
but_multiply.grid(row=2, column=3)

but_del = tkinter.Button(root, text="<x>", command=lambda: delete(), width=5, font=("Time New Roman", 14))
but_del.grid(row=2, column=4)

but_clear = tkinter.Button(root, text="C", command=lambda: clear(), width=5, font=("Time New Roman", 14))
but_clear.grid(row=2, column=1)

but_dec = tkinter.Button(root, text=".", command=lambda: add_to_field("."), width=5, font=("Time New Roman", 14))
but_dec.grid(row=6, column=3)

# open_bracket = tkinter.Button(root, text="(", command=lambda: add_to_field("("), width=5, font=("Time New Roman", 14))
# open_bracket.grid(row=6, column=1)

# close_bracket = tkinter.Button(root, text=")", command=lambda: add_to_field(")"),
# width=5, font=("Time New Roman", 14))
# close_bracket.grid(row=6, column=2)

but_divide = tkinter.Button(root, text="/", command=lambda: add_to_field("/"), width=5, font=("Time New Roman", 14))
but_divide.grid(row=2, column=2)

but_equal = tkinter.Button(root, text="=", command=lambda: calculate(), width=5,
                           font=("Time New Roman", 14), bg="green")
but_equal.grid(row=6, column=4)

root.mainloop()
