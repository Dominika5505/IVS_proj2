from tkinter import Button, Entry, Tk, END
import calc

root = Tk()
root.title("Calculator")

display = Entry(root, width=42, borderwidth=0, fg="#ffffff", bg="#313131")
display.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

equation = ""
result = ""
toDelete = False


def conc_string(input):
    global toDelete
    global equation
    if(toDelete):
        display.delete(0, END)
    toDelete = False
    equation += str(input)
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(input))

def clear():
    display.delete(0, END)
    global equation
    equation = ""

def equal():
    global toDelete
    global equation
    global result
    display.delete(0, END)
    if equation == "":
        display.insert(0, "0")
    else:
        result = eval(equation)
        display.insert(0, result)
    toDelete = True
    equation = ""

def remove():
    global equation
    if equation != "":
        equation = equation[:-1]
        display.delete(0, END)
        display.insert(0, equation)

def key_press(event):
    key = event.char
    if key == "c":
        clear()
    elif key == "1" or key == "2" or key == "3" or key == "4" or key == "5" or key == "6" or key == "7" or key == "8" or key == "9" or key == "0" or key == "+" or key == "-" or key == "*" or key == "/":
        conc_string(key)
    elif key == "=":
        equal()



def create_buttons():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, button0
    global buttonAdd, buttonSub, buttonMul, buttonDiv, buttonEqual, buttonClear, buttonDelete

    button1 = Button(root, text="1", padx=25, pady=20, borderwidth=0, fg="#ffffff", bg="#202020", command=lambda: conc_string(1))
    button2 = Button(root, text="2", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string(2))
    button3 = Button(root, text="3", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string(3))
    button4 = Button(root, text="4", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string(4))
    button5 = Button(root, text="5", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string(5))
    button6 = Button(root, text="6", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string(6))
    button7 = Button(root, text="7", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string(7))
    button8 = Button(root, text="8", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string(8))
    button9 = Button(root, text="9", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string(9))
    button0 = Button(root, text="0", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string(0))

    buttonAdd = Button(root, text="+", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string("+"))
    buttonSub = Button(root, text="-", padx=27, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string("-"))
    buttonMul = Button(root, text="×", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string("*"))
    buttonDiv = Button(root, text="÷", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: conc_string("/"))
    buttonEqual = Button(root, text="=", padx=56, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=equal)
    buttonClear = Button(root, text="C", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=clear)
    buttonDelete = Button(root, text="<", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=remove)


def position_buttons():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, button0
    global buttonAdd, buttonSub, buttonMul, buttonDiv, buttonEqual, buttonClear, buttonDelete

    button1.grid(row=4, column=0, padx=1, pady=1)
    button2.grid(row=4, column=1, padx=1, pady=1)
    button3.grid(row=4, column=2, padx=1, pady=1)
    button4.grid(row=3, column=0, padx=1, pady=1)
    button5.grid(row=3, column=1, padx=1, pady=1)
    button6.grid(row=3, column=2, padx=1, pady=1)
    button7.grid(row=2, column=0, padx=1, pady=1)
    button8.grid(row=2, column=1, padx=1, pady=1)
    button9.grid(row=2, column=2, padx=1, pady=1)
    button0.grid(row=5, column=0, padx=1, pady=1)

    buttonAdd.grid(row=2, column=3, padx=1, pady=1)
    buttonSub.grid(row=3, column=3, padx=1, pady=1)
    buttonMul.grid(row=4, column=3, padx=1, pady=1)
    buttonDiv.grid(row=5, column=3, padx=1, pady=1)
    buttonEqual.grid(row=5, column=1, columnspan=2, padx=1, pady=1)
    buttonClear.grid(row=1, column=3, padx=1, pady=1)
    buttonDelete.grid(row=1, column=2, padx=1, pady=1)

def define_keybinds():
    root.bind(("<Return>") ,lambda event:equal())
    root.bind(("<BackSpace>") ,lambda event:remove())
    root.bind("<Key>" ,key_press)

create_buttons()
position_buttons()
define_keybinds()
    
root.mainloop()