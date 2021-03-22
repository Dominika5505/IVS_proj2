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
        self.root.geometry("312x402")
        self.root.title("Calculator")

    def create_frames(self):
        self.textFrame = Frame(self.root, width = 312, height = 50, bg = "#f5f5f5")
        self.textFrame.pack()
        self.inputFrame = Frame(self.root, width = 312, height = 50, bd = 0, bg = "#f5f5f5")
        self.inputFrame.pack(side = TOP)
        self.btnsFrame = Frame(self.root, width = 312, height = 300, bg = "#fff")
        self.btnsFrame.pack()

    def create_input_field(self):
        self.inputField = Entry(self.inputFrame, font = ('lato', 14), width = 50, bg = "#f5f5f5", bd = 0, justify = RIGHT)
        self.inputField.pack(ipady = 15)
        self.inputField.place(bordermode = OUTSIDE, relwidth = 0.95, relheight = 1)

    def create_buttons(self):

        self.buttonClear = Button(self.btnsFrame, text="Clear", bd=0, borderwidth=0, fg="#555555", bg="#fafafa", command=self.guiFuncs.clear_input_field)
        self.buttonDelete = Button(self.btnsFrame, text="<", bd=0, borderwidth=0, fg="#555555", bg="#fafafa", command=self.guiFuncs.remove)

        self.buttonExp = Button(self.btnsFrame, text="^", bd=0, borderwidth=0, fg="#555", bg="#fafafa", command=lambda: self.guiFuncs.div_string("^"))
        self.buttonSquare = Button(self.btnsFrame, text="√", bd=0, borderwidth=0, fg="#555", bg="#fafafa", command=lambda: self.guiFuncs.div_string("s"))
        self.buttonFact = Button(self.btnsFrame, text="x!", bd=0, borderwidth=0, fg="#555", bg="#fafafa", command=lambda: self.guiFuncs.div_string("!"))
        self.buttonDiv = Button(self.btnsFrame, text="÷", bd=0, borderwidth=0, fg="#555", bg="#fafafa", command=lambda: self.guiFuncs.div_string("/"))

        self.button7 = Button(self.btnsFrame, text="7", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(7))
        self.button8 = Button(self.btnsFrame, text="8", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(8))
        self.button9 = Button(self.btnsFrame, text="9", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(9))
        self.buttonMul = Button(self.btnsFrame, text="×", bd=0, borderwidth=0, fg="#555", bg="#fafafa", command=lambda: self.guiFuncs.div_string("*"))

        self.button4 = Button(self.btnsFrame, text="4", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(4))
        self.button5 = Button(self.btnsFrame, text="5", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(5))
        self.button6 = Button(self.btnsFrame, text="6", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(6))
        self.buttonSub = Button(self.btnsFrame, text="-", bd=0, borderwidth=0, fg="#555",  bg="#fafafa", command=lambda: self.guiFuncs.div_string("-"))

        self.button1 = Button(self.btnsFrame, text="1", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(1))
        self.button2 = Button(self.btnsFrame, text="2", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(2))
        self.button3 = Button(self.btnsFrame, text="3", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(3))
        self.buttonAdd = Button(self.btnsFrame, text="+", bd=0, borderwidth=0, fg="#555", bg="#fafafa", command=lambda: self.guiFuncs.div_string("+"))

        self.buttonAbs = Button(self.btnsFrame, text="|x|", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string("a"))
        self.button0 = Button(self.btnsFrame, text="0", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string(0))
        self.buttonDot = Button(self.btnsFrame, text=".", bd=0, borderwidth=0, fg="#555", bg="#fff", command=lambda: self.guiFuncs.div_string("."))
        self.buttonEqual = Button(self.btnsFrame, text="=", bd=0, borderwidth=0, fg="#555", bg="#fafafa", command=self.guiFuncs.equal)

    def position_buttons(self):
        self.buttonClear.place(relwidth = 0.8, height = 50)
        self.buttonDelete.place(relwidth = 0.2, height = 50, relx = 0.8)

        self.buttonExp.place(relwidth = 0.25, height = 50, y = 50)
        self.buttonSquare.place(relwidth = 0.25, height = 50, relx = 0.25, y = 50)
        self.buttonFact.place(relwidth = 0.25, height = 50, relx = 0.5, y = 50)
        self.buttonDiv.place(relwidth = 0.25, height = 50, relx = 0.75, y = 50)

        self.button7.place(relwidth = 0.25, height = 50, y = 100)
        self.button8.place(relwidth = 0.25, height = 50, relx = 0.25, y = 100)
        self.button9.place(relwidth = 0.25, height = 50, relx = 0.5, y = 100)
        self.buttonMul.place(relwidth = 0.25, height = 50, relx = 0.75, y = 100)

        self.button4.place(relwidth = 0.25, height = 50, y = 150)
        self.button5.place(relwidth = 0.25, height = 50, relx = 0.25, y = 150)
        self.button6.place(relwidth = 0.25, height = 50, relx = 0.5, y = 150)
        self.buttonSub.place(relwidth = 0.25, height = 50, relx = 0.75, y = 150)

        self.button1.place(relwidth = 0.25, height = 50, y = 200)
        self.button2.place(relwidth = 0.25, height = 50, relx = 0.25, y = 200)
        self.button3.place(relwidth = 0.25, height = 50, relx = 0.5, y = 200)
        self.buttonAdd.place(relwidth = 0.25, height = 50, relx = 0.75, y = 200)

        self.buttonAbs.place(relwidth = 0.25, height = 50, y = 250)
        self.button0.place(relwidth = 0.25, height = 50, relx = 0.25, y = 250)
        self.buttonDot.place(relwidth = 0.25, height = 50, relx = 0.5, y = 250)
        self.buttonEqual.place(relwidth = 0.25, height = 50, relx = 0.75, y = 250)

    def define_keybinds(self):
        self.root.bind(("<Return>") ,lambda event:self.guiFuncs.equal())
        self.root.bind(("<BackSpace>") ,lambda event:self.guiFuncs.remove())
        self.root.bind("<Key>" ,self.guiFuncs.key_press)
        self.inputField.bind("<Button-1>", lambda event: "break")