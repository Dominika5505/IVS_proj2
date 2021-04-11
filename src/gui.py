from gui_func import Gui_Functions
import os
try:
    import Tkinter as tk
    import Tkinter.font as tkFont
except ImportError:
    import tkinter as tk
    import tkinter.font as tkFont
    
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
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.defaultFont = tkFont.Font(root = self.root, family = "Lato", size = 24, weight = "bold")
        self.root.geometry("312x400")
        self.root.title("VKZsB Calculator")

    def create_frames(self):
        self.switchOuterFrame = tk.Frame(self.root, width = 312, height = 30, bd = 0)
        self.switchOuterFrame.pack()

        self.switchFrame = tk.Frame(self.switchOuterFrame, bd = 0)
        self.switchFrame.pack()

        self.switchFrame.place(relwidth = 0.3, relheight = 1)

        self.textFrame = tk.Frame(self.root, width = 312, height = 20)
        self.textFrame.pack()
        
        self.inputFrame = tk.Frame(self.root, width = 312, height = 50, bd = 0)
        self.inputFrame.pack(side = tk.TOP)

        self.emptyFrame = tk.Frame(self.root, width = 312, height = 5)
        self.emptyFrame.pack()
        
        self.btnsFrame = tk.Frame(self.root, width = 312, height = 300)
        self.btnsFrame.pack()

    def create_input_field(self):
        self.inputField = tk.Entry(self.inputFrame, font = ("Lato", 14), width = 50, bd = 0, justify = tk.RIGHT, cursor = "arrow")
        self.inputField.place(bordermode = tk.OUTSIDE, relwidth = 0.95, relheight = 1)

    def create_equasion_field(self):
        self.equaionField = tk.Entry(self.textFrame, font = ('Lato', 11), width = 50, bd = 0, justify = tk.RIGHT, cursor = "arrow")

        self.equaionField.pack()
        self.equaionField.place(relwidth = 0.95, relheight = 1)

    def create_light_mode_buttons(self):
        self.sunIcon = tk.PhotoImage(file = "./imgs/sun_bw.png")
        self.moonIcon = tk.PhotoImage(file = "./imgs/moon.png")
        

        self.lightModeButton = tk.Radiobutton(self.switchFrame, variable = self.switchVar,
                            indicatoron = False, value = 1, bd = 0, command = lambda: self.change_light_mode(self.switchVar))

        self.lightModeButton.pack(side="left")
        self.lightModeButton.place(x = 5, y = 5)


    def change_light_mode(self, buttonLightChecked):
        
        if buttonLightChecked == 1:

            self.switchOuterFrame.config(bg = "#f8f8f8")
            self.switchFrame.config(bg = "#f8f8f8")
            self.lightModeButton.config(bg = "#f8f8f8", fg = "#555", highlightcolor = "#f8f8f8", highlightbackground = "#f8f8f8", selectcolor = "#f8f8f8", image = self.sunIcon, activebackground = "#f8f8f8")

            self.textFrame.config(bg = "#f8f8f8")
            self.inputFrame.config(bg = "#f8f8f8")
            self.emptyFrame.config(bg = "#f8f8f8")
            self.btnsFrame.config(bg = "#fff")
            self.inputField.config(bg = "#f8f8f8", fg = "#555")
            self.equaionField.config(bg = "#f8f8f8", fg = "#999")

            self.buttonClear.config(bg = "#f8f8f8", fg = "#555")
            self.buttonAbs.config(bg = "#f8f8f8", fg = "#555")
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

            self.buttonAns.config(bg = "#fff", fg = "#555")
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
            self.buttonAbs.config(bg = "#444", fg = "#bbb")
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

            # self.buttonAbs.config(bg = "#494949", fg = "#bbb")
            self.buttonAns.config(bg = "#494949", fg = "#bbb")
            self.button0.config(bg = "#494949", fg = "#bbb")
            self.buttonDot.config(bg = "#494949", fg = "#bbb")
            self.buttonEqual.config(bg = "#444", fg = "#bbb")

            self.switchVar = 1



    def create_buttons(self):

        self.buttonClear = tk.Button(self.btnsFrame, text="Clear", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("c"))
        self.buttonAns = tk.Button(self.btnsFrame, text="Ans", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("n"))
        self.buttonDelete = tk.Button(self.btnsFrame, text="<", bd=0, borderwidth=0, command=self.guiFuncs.remove)

        self.buttonExp = tk.Button(self.btnsFrame, text="^", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("^"))
        self.buttonSquare = tk.Button(self.btnsFrame, text="√", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("s"))
        self.buttonFact = tk.Button(self.btnsFrame, text="x!", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("!"))
        self.buttonDiv = tk.Button(self.btnsFrame, text="÷", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("/"))

        self.button7 = tk.Button(self.btnsFrame, text="7", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(7))
        self.button8 = tk.Button(self.btnsFrame, text="8", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(8))
        self.button9 = tk.Button(self.btnsFrame, text="9", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(9))
        self.buttonMul = tk.Button(self.btnsFrame, text="×", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("*"))

        self.button4 = tk.Button(self.btnsFrame, text="4", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(4))
        self.button5 = tk.Button(self.btnsFrame, text="5", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(5))
        self.button6 = tk.Button(self.btnsFrame, text="6", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(6))
        self.buttonSub = tk.Button(self.btnsFrame, text="-", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("-"))

        self.button1 = tk.Button(self.btnsFrame, text="1", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(1))
        self.button2 = tk.Button(self.btnsFrame, text="2", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(2))
        self.button3 = tk.Button(self.btnsFrame, text="3", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(3))
        self.buttonAdd = tk.Button(self.btnsFrame, text="+", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("+"))

        self.buttonAbs = tk.Button(self.btnsFrame, text="|x|", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("a"))
        self.button0 = tk.Button(self.btnsFrame, text="0", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string(0))
        self.buttonDot = tk.Button(self.btnsFrame, text=".", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_string("."))
        self.buttonEqual = tk.Button(self.btnsFrame, text="=", bd=0, borderwidth=0, command=self.guiFuncs.equal)

    def position_buttons(self):
        self.buttonClear.place(relwidth = 0.75, height = 50)
        # self.buttonAns.place(relwidth = 0.25, height = 50, relx = 0.50)
        self.buttonDelete.place(relwidth = 0.25, height = 50, relx = 0.75)


        self.buttonAbs.place(relwidth = 0.19, height = 50, y = 50)
        self.buttonExp.place(relwidth = 0.19, height = 50, y = 50, relx = 0.19)
        self.buttonSquare.place(relwidth = 0.19, height = 50, relx = 0.38, y = 50)
        self.buttonFact.place(relwidth = 0.19, height = 50, relx = 0.57, y = 50)
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

        self.buttonAns.place(relwidth = 0.25, height = 50, y = 250)
        # self.buttonAbs.place(relwidth = 0.25, height = 50, y = 250)
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
        