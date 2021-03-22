from tkinter import *
from gui_func import Gui_Functions
    
class GUI:
    def __init__(self):
        self.create_root()
        self.create_frames()
        self.create_input_field()
        
        self.guiFuncs = Gui_Functions(self.inputField)

        self.create_buttons()
        self.position_buttons()
        self.define_keybinds()

    def create_root(self):
        self.root = Tk()
        self.root.iconbitmap("../imgs/icon3.ico")
        self.root.geometry("312x377")
        # self.root.resizable(0, 0)
        self.root.title("Calculator")

    def create_frames(self):
        self.inputFrame = Frame(self.root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
        self.inputFrame.pack(side = TOP)
        self.btnsFrame = Frame(self.root, width = 312, height = 272, bg = "#fff")
        self.btnsFrame.pack()
        # self.btnsFrame = Frame(self.root, width = 312, height = 272.5, bg = "#fafafa")
        # self.btnsFrame.pack()

    def create_input_field(self):
        self.inputField = Entry(self.inputFrame, font = ('lato', 14), width = 50, bg = "#fafafa", bd = 0, borderwidth=0, justify = RIGHT)
        self.inputField.grid(row = 0, column = 0)
        self.inputField.pack(ipady = 15)

    def create_buttons(self):

        self.buttonClear = Button(self.btnsFrame, text="Clear", fg="#555555", width = 32, height = 3, bd=0, bg="#fafafa", command=self.guiFuncs.clear_input_field)
        self.buttonDelete = Button(self.btnsFrame, text="<", fg="#555555", width = 10, height = 3, bd=0, bg="#fafafa", command=self.guiFuncs.remove)

        self.buttonExp = Button(self.btnsFrame, text="^", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fafafa", command=lambda: self.guiFuncs.div_string("^"))
        self.buttonSquare = Button(self.btnsFrame, text="√", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fafafa", command=lambda: self.guiFuncs.div_string("s"))
        self.buttonFact = Button(self.btnsFrame, text="x!", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fafafa", command=lambda: self.guiFuncs.div_string("!"))
        self.buttonDiv = Button(self.btnsFrame, text="÷", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fafafa", command=lambda: self.guiFuncs.div_string("/"))

        self.button7 = Button(self.btnsFrame, text="7", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(7))
        self.button8 = Button(self.btnsFrame, text="8", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(8))
        self.button9 = Button(self.btnsFrame, text="9", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(9))
        self.buttonMul = Button(self.btnsFrame, text="×", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fafafa", command=lambda: self.guiFuncs.div_string("*"))

        self.button4 = Button(self.btnsFrame, text="4", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(4))
        self.button5 = Button(self.btnsFrame, text="5", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(5))
        self.button6 = Button(self.btnsFrame, text="6", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(6))
        self.buttonSub = Button(self.btnsFrame, text="-", borderwidth=0, fg="#555",  width = 10, height = 3, bg="#fafafa", command=lambda: self.guiFuncs.div_string("-"))

        self.button1 = Button(self.btnsFrame, text="1", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(1))
        self.button2 = Button(self.btnsFrame, text="2", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(2))
        self.button3 = Button(self.btnsFrame, text="3", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(3))
        self.buttonAdd = Button(self.btnsFrame, text="+", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fafafa", command=lambda: self.guiFuncs.div_string("+"))

        self.buttonAbs = Button(self.btnsFrame, text="|x|", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string("a"))
        self.button0 = Button(self.btnsFrame, text="0", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string(0))
        self.buttonDot = Button(self.btnsFrame, text=".", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fff", command=lambda: self.guiFuncs.div_string("."))
        self.buttonEqual = Button(self.btnsFrame, text="=", borderwidth=0, fg="#555", width = 10, height = 3, bg="#fafafa", command=self.guiFuncs.equal)


    def position_buttons(self):

        self.buttonClear.grid(row=0, column=0, columnspan=3, pady=1)
        self.buttonDelete.grid(row=0, column=3, pady=1)

        self.buttonExp.grid(row=1, column=0)
        self.buttonSquare.grid(row=1, column=1)
        self.buttonFact.grid(row=1, column=2)
        self.buttonDiv.grid(row=1, column=3)

        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
        self.buttonMul.grid(row=2, column=3)

        self.button4.grid(row=3, column=0)
        self.button5.grid(row=3, column=1)
        self.button6.grid(row=3, column=2)
        self.buttonSub.grid(row=3, column=3)

        self.button1.grid(row=4, column=0)
        self.button2.grid(row=4, column=1)
        self.button3.grid(row=4, column=2)
        self.buttonAdd.grid(row=4, column=3)

        self.buttonAbs.grid(row=5, column=0)
        self.button0.grid(row=5, column=1)
        self.buttonDot.grid(row=5, column=2)
        self.buttonEqual.grid(row=5, column=3)

    def define_keybinds(self):
        self.root.bind(("<Return>") ,lambda event:self.guiFuncs.equal())
        self.root.bind(("<BackSpace>") ,lambda event:self.guiFuncs.remove())
        self.root.bind("<Key>" ,self.guiFuncs.key_press)