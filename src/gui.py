from tkinter import Button, Entry, Tk, END
from gui_func import Gui_Functions, root

gui_funcs = Gui_Functions()
    
class GUI:
    def __init__(self):

        self.button1 = Button(root, text="1", padx=25, pady=20, borderwidth=0, fg="#ffffff", bg="#202020", command=lambda: gui_funcs.div_string(1))
        self.button2 = Button(root, text="2", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string(2))
        self.button3 = Button(root, text="3", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string(3))
        self.button4 = Button(root, text="4", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string(4))
        self.button5 = Button(root, text="5", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string(5))
        self.button6 = Button(root, text="6", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string(6))
        self.button7 = Button(root, text="7", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string(7))
        self.button8 = Button(root, text="8", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string(8))
        self.button9 = Button(root, text="9", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string(9))
        self.button0 = Button(root, text="0", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string(0))

        self.buttonAdd = Button(root, text="+", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string("+"))
        self.buttonSub = Button(root, text="-", padx=27, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string("-"))
        self.buttonMul = Button(root, text="×", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string("*"))
        self.buttonDiv = Button(root, text="÷", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string("/"))
        self.buttonEqual = Button(root, text="=", padx=56, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=gui_funcs.equal)
        self.buttonClear = Button(root, text="C", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=gui_funcs.clear_display)
        self.buttonDelete = Button(root, text="<", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=gui_funcs.remove)
        self.buttonSquare = Button(root, text="√", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string("s"))
        self.buttonExp = Button(root, text="^", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string("^"))
        self.buttonAbs = Button(root, text="|x|", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string("a"))
        self.buttonDot = Button(root, text=".", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string("."))
        self.buttonFact = Button(root, text="x!", padx=25, pady=20, borderwidth=0, fg="#ffffff",  bg="#202020", command=lambda: gui_funcs.div_string("!"))


    def position_buttons(self):
        self.buttonAbs.grid(row=1, column=0, padx=1, pady=1)
        self.buttonDot.grid(row=1, column=1, padx=1, pady=1)
        self.buttonFact.grid(row=1, column=2, padx=1, pady=1)

        self.buttonExp.grid(row=2, column=0, padx=1, pady=1)
        self.buttonSquare.grid(row=2, column=1, padx=1, pady=1)
        self.buttonDelete.grid(row=2, column=2, padx=1, pady=1)
        self.buttonClear.grid(row=2, column=3, padx=1, pady=1)

        self.button7.grid(row=3, column=0, padx=1, pady=1)
        self.button8.grid(row=3, column=1, padx=1, pady=1)
        self.button9.grid(row=3, column=2, padx=1, pady=1)
        self.buttonAdd.grid(row=3, column=3, padx=1, pady=1)

        self.button5.grid(row=4, column=1, padx=1, pady=1)
        self.button4.grid(row=4, column=0, padx=1, pady=1)
        self.button6.grid(row=4, column=2, padx=1, pady=1)
        self.buttonSub.grid(row=4, column=3, padx=1, pady=1)

        self.button1.grid(row=5, column=0, padx=1, pady=1)
        self.button2.grid(row=5, column=1, padx=1, pady=1)
        self.button3.grid(row=5, column=2, padx=1, pady=1)
        self.buttonMul.grid(row=5, column=3, padx=1, pady=1)

        self.buttonDiv.grid(row=6, column=3, padx=1, pady=1)
        self.button0.grid(row=6, column=0, padx=1, pady=1)
        self.buttonEqual.grid(row=6, column=1, columnspan=2, padx=1, pady=1)

    def define_keybinds(self):
        root.bind(("<Return>") ,lambda event:gui_funcs.equal())
        root.bind(("<BackSpace>") ,lambda event:gui_funcs.remove())
        root.bind("<Key>" ,gui_funcs.key_press)