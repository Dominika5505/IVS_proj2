from gui_func import Gui_Functions
import os
# try:
# from Tkinter import *
# import ttk
# import tkinter.font as tkFont
# from ttkwidgets.frames import Balloon
# except ImportError:
from tkinter import *
# from tkinter import tix
# from tkinter.tix import Balloon 
import tkinter.font as tkFont
import Pmw
    
class GUI:
    def __init__(self):
        self.sunIcon = ""
        self.moonIcon = ""
        self.switchVar = 1
 
        self.create_root()
        self.create_frames()
        self.create_input_field()
        self.create_equasion_field()
        
        self.guiFuncs = Gui_Functions(self.inputField, self.equaionField)

        self.create_buttons()
        self.position_buttons()
        self.create_light_mode_buttons()
        self.change_light_mode(self.switchVar)
        self.define_keybinds()

    def create_root(self):
        self.root = Tk()
        self.root.resizable(0, 0)
        self.defaultFont = tkFont.Font(root = self.root, family = "Lato", size = 24, weight = "bold")
        self.root.geometry("312x400")
        self.root.title("VKZsB Calculator")

    def create_frames(self):
        self.switchOuterFrame = Frame(self.root, width = 312, height = 30, bd = 0)
        self.switchOuterFrame.pack()

        self.switchFrame = Frame(self.switchOuterFrame, bd = 0)
        self.switchFrame.pack()

        self.switchFrame.place(relwidth = 0.3, relheight = 1)

        self.textFrame = Frame(self.root, width = 312, height = 20)
        self.textFrame.pack()
        
        self.inputFrame = Frame(self.root, width = 312, height = 50, bd = 0)
        self.inputFrame.pack(side = TOP)

        self.emptyFrame = Frame(self.root, width = 312, height = 5)
        self.emptyFrame.pack()
        
        self.btnsFrame = Frame(self.root, width = 312, height = 300)
        self.btnsFrame.pack()

    def create_input_field(self):
        self.inputField = Entry(self.inputFrame, font = ("Lato", 14), width = 50, bd = 0, justify = RIGHT, cursor = "arrow")
        self.inputField.place(bordermode = OUTSIDE, relwidth = 0.95, relheight = 1)

    def create_equasion_field(self):
        self.equaionField = Entry(self.textFrame, font = ('Lato', 11), width = 50, bd = 0, justify = RIGHT, cursor = "arrow")

        self.equaionField.pack()
        self.equaionField.place(relwidth = 0.95, relheight = 1)

    def create_light_mode_buttons(self):
        self.sunIcon = PhotoImage(file = "../imgs/sun_bw.png")
        self.moonIcon = PhotoImage(file = "../imgs/moon.png")
        

        self.lightModeButton = Radiobutton(self.switchFrame, variable = self.switchVar,
                            indicatoron = False, value = 1, bd = 0, command = lambda: self.change_light_mode(self.switchVar))

        self.lightModeButton.pack(side="left")
        self.lightModeButton.place(x = 5, y = 5)


    def change_light_mode(self, buttonLightChecked):
        
        if buttonLightChecked == 1:

            self.switchOuterFrame.config(bg = "#f8f8f8")
            self.switchFrame.config(bg = "#f8f8f8")
            self.lightModeButton.config(bg = "#f8f8f8", fg = "#555", highlightcolor = "#f8f8f8", highlightbackground = "#f8f8f8", selectcolor = "#f8f8f8", image = self.sunIcon, activebackground = "#f8f8f8")
            # self.darkModeButton.config(bg = "#f8f8f8", fg = "#555", highlightcolor = "#f8f8f8", highlightbackground = "#f8f8f8", selectcolor = "#f8f8f8")

            self.textFrame.config(bg = "#f8f8f8")
            self.inputFrame.config(bg = "#f8f8f8")
            self.emptyFrame.config(bg = "#f8f8f8")
            self.btnsFrame.config(bg = "#fff")
            self.inputField.config(bg = "#f8f8f8", fg = "#555")
            self.equaionField.config(bg = "#f8f8f8", fg = "#999")

            self.buttonClear.config(bg = "#f8f8f8", fg = "#555")
            self.buttonDelete.config(bg = "#f8f8f8", fg = "#555")
            self.buttonExp.config(bg = "#f8f8f8", fg = "#555")
            self.buttonSquare.config(bg = "#f8f8f8", fg = "#555")
            self.buttonFact.config(bg = "#f8f8f8", fg = "#555")
            self.buttonDiv.config(bg = "#f8f8f8", fg = "#555")

            self.button7.config(bg = "#fff", fg = "#555")
            self.button8.config(bg = "#fff", fg = "#555")
            self.button9.config(bg = "#fff", fg = "#555")
            self.buttonMul.config(bg = "#f8f8f8", fg = "#555")

            self.button4.config(bg = "#fff", fg = "#555")
            self.button5.config(bg = "#fff", fg = "#555")
            self.button6.config(bg = "#fff", fg = "#555")
            self.buttonSub.config(bg = "#f8f8f8", fg = "#555")

            self.button1.config(bg = "#fff", fg = "#555")
            self.button2.config(bg = "#fff", fg = "#555")
            self.button3.config(bg = "#fff", fg = "#555")
            self.buttonAdd.config(bg = "#f8f8f8", fg = "#555")

            self.buttonAbs.config(bg = "#fff", fg = "#555")
            self.button0.config(bg = "#fff", fg = "#555")
            self.buttonDot.config(bg = "#fff", fg = "#555")
            self.buttonEqual.config(bg = "#f8f8f8", fg = "#555")

            self.switchVar = 0
        else:
            self.switchOuterFrame.config(bg = "#4f4f4f")
            self.switchFrame.config(bg = "#4f4f4f")
            self.lightModeButton.config(bg = "#4f4f4f", fg = "#bbb", selectcolor = "#4f4f4f", highlightcolor = "#4f4f4f", highlightbackground = "#4f4f4f", image = self.moonIcon, activebackground = "#4f4f4f")

            self.textFrame.config(bg = "#4f4f4f")
            self.inputFrame.config(bg = "#4f4f4f")
            self.emptyFrame.config(bg = "#4f4f4f")
            self.btnsFrame.config(bg = "#4f4f4f")
            self.inputField.config(bg = "#4f4f4f", fg = "#aaa")
            self.equaionField.config(bg = "#4f4f4f", fg = "#888")

            self.buttonClear.config(bg = "#444", fg = "#bbb")
            self.buttonDelete.config(bg = "#444", fg = "#bbb")
            self.buttonExp.config(bg = "#444", fg = "#bbb")
            self.buttonSquare.config(bg = "#444", fg = "#bbb")
            self.buttonFact.config(bg = "#444", fg = "#bbb")
            self.buttonDiv.config(bg = "#444", fg = "#bbb")

            self.button7.config(bg = "#494949", fg = "#bbb")
            self.button8.config(bg = "#494949", fg = "#bbb")
            self.button9.config(bg = "#494949", fg = "#bbb")
            self.buttonMul.config(bg = "#444", fg = "#bbb")

            self.button4.config(bg = "#494949", fg = "#bbb")
            self.button5.config(bg = "#494949", fg = "#bbb")
            self.button6.config(bg = "#494949", fg = "#bbb")
            self.buttonSub.config(bg = "#444", fg = "#bbb")

            self.button1.config(bg = "#494949", fg = "#bbb")
            self.button2.config(bg = "#494949", fg = "#bbb")
            self.button3.config(bg = "#494949", fg = "#bbb")
            self.buttonAdd.config(bg = "#444", fg = "#bbb")

            self.buttonAbs.config(bg = "#494949", fg = "#bbb")
            self.button0.config(bg = "#494949", fg = "#bbb")
            self.buttonDot.config(bg = "#494949", fg = "#bbb")
            self.buttonEqual.config(bg = "#444", fg = "#bbb")

            self.switchVar = 1



    def create_buttons(self):

        self.buttonClear = Button(self.btnsFrame, text="Clear", bd=0, borderwidth=0, command=self.guiFuncs.clear_input_field)
        self.buttonDelete = Button(self.btnsFrame, text="<", bd=0, borderwidth=0, command=self.guiFuncs.remove)

        self.buttonExp = Button(self.btnsFrame, text="^", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("^"))
        self.buttonSquare = Button(self.btnsFrame, text="√", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("s"))
        self.buttonFact = Button(self.btnsFrame, text="x!", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("!"))
        self.buttonDiv = Button(self.btnsFrame, text="÷", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("/"))

        self.button7 = Button(self.btnsFrame, text="7", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(7))
        self.button8 = Button(self.btnsFrame, text="8", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(8))
        self.button9 = Button(self.btnsFrame, text="9", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(9))
        self.buttonMul = Button(self.btnsFrame, text="×", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("*"))

        self.button4 = Button(self.btnsFrame, text="4", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(4))
        self.button5 = Button(self.btnsFrame, text="5", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(5))
        self.button6 = Button(self.btnsFrame, text="6", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(6))
        self.buttonSub = Button(self.btnsFrame, text="-", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("-"))

        self.button1 = Button(self.btnsFrame, text="1", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(1))
        self.button2 = Button(self.btnsFrame, text="2", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(2))
        self.button3 = Button(self.btnsFrame, text="3", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(3))
        self.buttonAdd = Button(self.btnsFrame, text="+", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("+"))

        self.buttonAbs = Button(self.btnsFrame, text="|x|", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("a"))
        self.button0 = Button(self.btnsFrame, text="0", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(0))
        self.buttonDot = Button(self.btnsFrame, text=".", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("."))
        self.buttonEqual = Button(self.btnsFrame, text="=", bd=0, borderwidth=0, command=self.guiFuncs.equal)

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
        self.root.bind("<m>" ,lambda event:self.change_light_mode(self.switchVar))
        self.inputField.bind("<Button-1>", lambda event: "break")
        self.equaionField.bind("<Button-1>", lambda event: "break")
        