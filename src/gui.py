# ======== Copyright (c) 2021, Vepro-knedlo-zelo s bryndzou, All rights reserved. ============ #
#
#  $Purpose:         Calculator - math library
#  
#  $University:      Brno University of Technology
#  $Faculty:         Faculty of Information Technology
#  $Programme:       Information Technology (Bachelor)
#  $Course:          Practical Aspects of Software Design (IVS)
#  $Academic year:   2020/2021 
#
#  $Authors:         Dominika Sedilekova    <xsedil00@stud.fit.vutbr.cz>  
#
# ======== Copyright (c) 2021, Vepro-knedlo-zelo s bryndzou, All rights reserved. ============ #

## 
#  @file gui.py
# 
#  @author Dominika Sedilekova
#
#  @brief Creating and placing gui 
#


## @package Gui_Functions
#  Gui input and output formatting.
from gui_func import Gui_Functions
try:
    ## @package Tkinter
    #  Library with gui modules.
    import Tkinter as tk
    ## @package Tkinter.font
    #  Font settings for gui.
    import Tkinter.font as tkFont
except ImportError:
    ## @package tkinter
    #  Library with gui modules.
    import tkinter as tk
    ## @package tkinter.font
    #  Font settings for gui.
    import tkinter.font as tkFont

##
#  @brief formates creates gui 
class GUI:
    ## 
    #  @brief the constructor
    #  
    #  @param self the object pointer
    # 
    #  Initiates member variables.
    def __init__(self):
        ## initiates variables for icons
        self.sunIcon = ""
        self.moonIcon = ""
        self.helpDarkIcon = ""
        self.helpLightIcon = ""
        ## variable for switching between light and dark mode, 1 == light, 0 == dark
        self.switchVar = 1
 
        self.create_root()
        self.create_frames()
        self.create_input_field()
        self.create_expression_field()
        ## calling gui formatting functions
        self.guiFuncs = Gui_Functions(self.inputField, self.expressionField)

        self.create_buttons()
        self.position_buttons()
        self.create_light_mode_buttons()
        self.create_help_button()
        self.change_light_mode(self.switchVar)
        self.define_keybinds()

    ## 
    #  @brief creates root of gui
    #  
    #  @param self the object pointer
    #
    def create_root(self):
        ## initiates root
        self.root = tk.Tk()
        ## sets app not to be resized
        self.root.resizable(0, 0)
        ## sets apps icon
        self.root.iconbitmap('imgs/icon.ico')
        ## sets default font of app
        self.defaultFont = tkFont.Font(root = self.root, family = "Lato", size = 24, weight = "bold")
        ## sets dimensions of an app
        self.root.geometry("312x400")
        ## sets title of an app
        self.root.title("Kalkulačka 1.0")

    ## 
    #  @brief creates main frames
    #  
    #  @param self the object pointer
    #
    def create_frames(self):
        ## frame for light mode and help buttons
        self.settingsFrame = tk.Frame(self.root, width = 312, height = 30, bd = 0)
        self.settingsFrame.pack()
        ## frame for expression field
        self.textFrame = tk.Frame(self.root, width = 312, height = 20)
        self.textFrame.pack()
        ## frame for input field
        self.inputFrame = tk.Frame(self.root, width = 312, height = 50, bd = 0)
        self.inputFrame.pack(side = tk.TOP)
        ## empty frame, that creates space between input and button frame
        self.emptyFrame = tk.Frame(self.root, width = 312, height = 5)
        self.emptyFrame.pack()
        ## frame for buttons
        self.btnsFrame = tk.Frame(self.root, width = 312, height = 300)
        self.btnsFrame.pack()

    ## 
    #  @brief creates input field
    #  
    #  @param self the object pointer
    #
    def create_input_field(self):
        self.inputField = tk.Entry(self.inputFrame, font = ("Lato", 14), width = 50, bd = 0, justify = tk.RIGHT, cursor = "arrow")
        self.inputField.place(bordermode = tk.OUTSIDE, relwidth = 0.95, relheight = 1)

    ## 
    #  @brief creates expression field
    #  
    #  @param self the object pointer
    #
    def create_expression_field(self):
        self.expressionField = tk.Entry(self.textFrame, font = ('Lato', 11), width = 50, bd = 0, justify = tk.RIGHT, cursor = "arrow")

        self.expressionField.pack()
        self.expressionField.place(relwidth = 0.95, relheight = 1)

    ## 
    #  @brief creates help button
    #  
    #  @param self the object pointer
    #
    def create_help_button(self):
        ## saves path to dark help icon
        self.helpDarkIcon = tk.PhotoImage(file = "./imgs/help_dark_icon.png")
        ## saves path to light help icon
        self.helpLightIcon = tk.PhotoImage(file = "./imgs/help_light_icon.png")
        ## creates and places help button, which calls function, that opens help pdf
        self.helpButton = tk.Button(self.settingsFrame, bd = 0, borderwidth = 0, command = lambda:self.guiFuncs.open_help())
        self.helpButton.pack()
        self.helpButton.place(x = 5, y = 6)

    ## 
    #  @brief creates light mode button
    #  
    #  @param self the object pointer
    #
    def create_light_mode_buttons(self):
        ## saves path to sun icon for light mode
        self.sunIcon = tk.PhotoImage(file = "./imgs/sun_bw.png")
        ## saves path to moon icon for dark mode
        self.moonIcon = tk.PhotoImage(file = "./imgs/moon.png")
        
        ## creates button to switch light mode which calls change_light_mode function on click
        self.lightModeButton = tk.Radiobutton(self.settingsFrame, variable = self.switchVar,
                            indicatoron = False, value = 1, bd = 0, command = lambda: self.change_light_mode(self.switchVar))
        ## place switch button
        self.lightModeButton.pack(side="left")
        self.lightModeButton.place(x = 32, y = 5)

    ## 
    #  @brief changes light mode
    #  
    #  @param self the object pointer
    #
    def change_light_mode(self, buttonLightChecked):
        
        ## if light mode is currently set
        if buttonLightChecked == 1:
            ## sets colors of frames
            self.settingsFrame.config(bg = "#f8f8f8")
            ## sets image and colors of button
            self.lightModeButton.config(bg = "#f8f8f8", fg = "#555", highlightcolor = "#f8f8f8", highlightbackground = "#f8f8f8", selectcolor = "#f8f8f8", image = self.sunIcon, activebackground = "#f8f8f8")

            ## sets image and colors of button
            self.helpButton.config(bg = "#f8f8f8", fg = "#555", highlightcolor = "#f8f8f8", highlightbackground = "#f8f8f8", activebackground = "#f8f8f8", image = self.helpDarkIcon)

            ## sets colors of frames
            self.textFrame.config(bg = "#f8f8f8")
            self.inputFrame.config(bg = "#f8f8f8")
            self.emptyFrame.config(bg = "#f8f8f8")
            self.btnsFrame.config(bg = "#fff")
            self.inputField.config(bg = "#f8f8f8", fg = "#555")
            self.expressionField.config(bg = "#f8f8f8", fg = "#999")

            ## sets colors of buttons
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

            ## sets light mode variable to 0 (dark mode)
            self.switchVar = 0
        ## if dark mode is currently set
        else:
            ## sets colors of frames
            self.settingsFrame.config(bg = "#4f4f4f")
            ## sets image and colors of button
            self.lightModeButton.config(bg = "#4f4f4f", fg = "#bbb", selectcolor = "#4f4f4f", highlightcolor = "#4f4f4f", highlightbackground = "#4f4f4f", image = self.moonIcon, activebackground = "#4f4f4f")

            ## sets image and colors of button
            self.helpButton.config(bg = "#4f4f4f", fg = "#bbb", highlightcolor = "#4f4f4f", highlightbackground = "#4f4f4f", activebackground = "#4f4f4f", image = self.helpLightIcon)

            ## sets colors of frames
            self.textFrame.config(bg = "#4f4f4f")
            self.inputFrame.config(bg = "#4f4f4f")
            self.emptyFrame.config(bg = "#4f4f4f")
            self.btnsFrame.config(bg = "#4f4f4f")
            self.inputField.config(bg = "#4f4f4f", fg = "#aaa")
            self.expressionField.config(bg = "#4f4f4f", fg = "#888")

            ## sets colors of buttons
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

            self.buttonAns.config(bg = "#494949", fg = "#bbb")
            self.button0.config(bg = "#494949", fg = "#bbb")
            self.buttonDot.config(bg = "#494949", fg = "#bbb")
            self.buttonEqual.config(bg = "#444", fg = "#bbb")

            ## sets light mode variable to 1 (light mode)
            self.switchVar = 1

    ## 
    #  @brief creates calculator buttons with function callings to gui functions (input/output formatting)
    #  
    #  @param self the object pointer
    #
    def create_buttons(self):

        self.buttonClear = tk.Button(self.btnsFrame, text="Clear", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("c"))
        self.buttonAns = tk.Button(self.btnsFrame, text="Ans", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("n"))
        self.buttonDelete = tk.Button(self.btnsFrame, text="<", bd=0, borderwidth=0, command=self.guiFuncs.remove)

        self.buttonExp = tk.Button(self.btnsFrame, text="^", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("^"))
        self.buttonSquare = tk.Button(self.btnsFrame, text="√", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("s"))
        self.buttonFact = tk.Button(self.btnsFrame, text="x!", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("!"))
        self.buttonDiv = tk.Button(self.btnsFrame, text="÷", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("/"))

        self.button7 = tk.Button(self.btnsFrame, text="7", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(7))
        self.button8 = tk.Button(self.btnsFrame, text="8", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(8))
        self.button9 = tk.Button(self.btnsFrame, text="9", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(9))
        self.buttonMul = tk.Button(self.btnsFrame, text="×", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("*"))

        self.button4 = tk.Button(self.btnsFrame, text="4", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(4))
        self.button5 = tk.Button(self.btnsFrame, text="5", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(5))
        self.button6 = tk.Button(self.btnsFrame, text="6", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(6))
        self.buttonSub = tk.Button(self.btnsFrame, text="-", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("-"))

        self.button1 = tk.Button(self.btnsFrame, text="1", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(1))
        self.button2 = tk.Button(self.btnsFrame, text="2", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(2))
        self.button3 = tk.Button(self.btnsFrame, text="3", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(3))
        self.buttonAdd = tk.Button(self.btnsFrame, text="+", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("+"))

        self.buttonAbs = tk.Button(self.btnsFrame, text="|x|", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("a"))
        self.button0 = tk.Button(self.btnsFrame, text="0", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input(0))
        self.buttonDot = tk.Button(self.btnsFrame, text=".", bd=0, borderwidth=0, command=lambda: self.guiFuncs.div_input("."))
        self.buttonEqual = tk.Button(self.btnsFrame, text="=", bd=0, borderwidth=0, command=self.guiFuncs.equal)

    ## 
    #  @brief positions calculator buttons
    #  
    #  @param self the object pointer
    #
    def position_buttons(self):
        self.buttonClear.place(relwidth = 0.75, height = 50)
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
        self.button0.place(relwidth = 0.25, height = 50, relx = 0.25, y = 250)
        self.buttonDot.place(relwidth = 0.25, height = 50, relx = 0.5, y = 250)
        self.buttonEqual.place(relwidth = 0.25, height = 50, relx = 0.75, y = 250)

    ## 
    #  @brief defines all allowed keybinds
    #  
    #  @param self the object pointer
    #
    def define_keybinds(self):
        ## pressed key "Return" or "Enter" calls gui funcion equal
        self.root.bind(("<Return>") ,lambda event:self.guiFuncs.equal())
        ## pressed key "Backspace" calls gui funcion remove, which removes one by one form input field
        self.root.bind(("<BackSpace>") ,lambda event:self.guiFuncs.remove())
        ## pressed key "m" calls self function, which changes light mode
        self.root.bind("<m>" ,lambda event:self.change_light_mode(self.switchVar))
        ## pressed "h" calls function, that opens help pdf
        self.root.bind("<h>" ,lambda event:self.guiFuncs.open_help())
        ## any other pressed key is sent to gui_func function, which sorts them out
        self.root.bind("<Key>" ,self.guiFuncs.key_press)
        ## secures, that input field cannot be clicked on
        self.inputField.bind("<Button-1>", lambda event: "break")
        ## secures, that expression field cannot be clicked on
        self.expressionField.bind("<Button-1>", lambda event: "break")
        