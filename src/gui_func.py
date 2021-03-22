from tkinter import END
from calculator import Calculator, is_int, int_or_float
import re
import sys

class Gui_Functions:
    
    def __init__(self, inputField):
        self.inputField = inputField
        self.equation = ""
        self.result = ""
        self.toDelete = False
        self.addPar = False
        self.doublePar = False
        self.inPar = False
        self.calculator = ""
        self.addedDot = False

    def calculate(self, eq):
        self.calculator = Calculator(eq)
        i = 0
        while i < self.calculator.eqArrayLen:
            try:
                self.calculator.solveSquareRoot()
                self.calculator.solveExp()
                self.calculator.solveMult()
                self.calculator.solveDiv()
                self.calculator.solveSub()
                self.calculator.solveSum()
            except:
                return "ERROR!"

            i += 1
        return str(self.calculator.eqArray)
        # return str(eq)

    def abs_test(self):
        num = self.inputField.get()
        self.inputField.delete(0, END)
        
        if is_int(num):
            self.inputField.insert(0, str(num))


    def add_abs(self):
        findNum = re.search(r'[-]?\d+[.]?\d*$', self.equation)
        foundNum = int_or_float(findNum.group()) if findNum else None

        if foundNum:
            numLen = len(str(foundNum))

            i = 0
            while i < numLen:
                self.remove()
                i += 1

            foundNum = "|" + str(foundNum) + "|"
            self.conc_string(foundNum)


    def check_root(self):
        findNum = re.search(r'[-]?\d+[.]?\d*$', self.equation)
        foundNum = int_or_float(findNum.group()) if findNum else None

        if foundNum:
            self.conc_string("√")
        else:
            self.conc_string("2√")


            
    def add_paranth(self, input):
        findNum = re.search(r'[-]?\d+[.]?\d*$', self.equation)
        foundNum = int_or_float(findNum.group()) if findNum else None

        self.inPar = False
        self.addPar = False

        if foundNum:
            numLen = len(str(foundNum))

            i = 0
            while i < numLen:
                self.remove()
                i += 1

            if self.doublePar:
                foundNum = str(foundNum) + ")"
                self.doublePar = False
            else:
                foundNum = "(" + str(foundNum) + ")"
            self.conc_string(foundNum + input)

    def add_decimal(self):
        findNum = re.search(r'[-]?\d+[.]\d*$', self.equation)
        foundNum = str(findNum.group()) if findNum else None
        
        if not foundNum:
            if self.equation == "" or not is_int(self.equation[len(self.equation) - 1]):
                self.conc_string("0.")
            else:
                self.conc_string(".")

    def conc_string(self, input):
        self.equation += str(input)
        current = self.inputField.get()
        self.inputField.delete(0, END)
        self.inputField.insert(0, str(current) + str(input))

    def div_string(self, input):
        if(self.toDelete):
            self.inputField.delete(0, END)
            self.calculator.clearArray()
            self.toDelete = False
        

        if self.inPar:
            if input == "-" or input == "+" or input == "/" or input == "*" or input == "^" or input == "√":
                self.addPar = True

        if not self.inPar:
            if self.equation.endswith("-") or self.equation.endswith("+") or self.equation.endswith("/") or self.equation.endswith("*") or self.equation.endswith("^") or self.equation.endswith("√") or self.equation == "":
                if input == "-":
                    self.inPar = True
        
        if input == "c":
            self.clear_input_field()
        elif input == ".":
            self.add_decimal()
        elif input == "s":
            self.check_root()
        elif input == "a":
            self.add_abs()
        elif self.addPar:
            self.add_paranth(input)
        elif self.equation == "" and not is_int(input): 
            if input != "." or input != "√":
                self.conc_string("0" + input)
        else: 
            self.conc_string(input)
            

    def clear_input_field(self):
        self.inputField.delete(0, END)
        # global self.equation, calculator
        if self.calculator:
            self.calculator.clearArray()
        self.equation = ""

    def equal(self):
        if self.inPar:
            self.addPar = True
        
        if self.addPar:
            self.add_paranth('')
        
        self.inputField.delete(0, END)
        if self.equation == "":
            self.inputField.insert(0, "0")
        else:
            self.result = self.calculate(self.equation)
            self.inputField.insert(0, self.result)
        self.toDelete = True
        self.equation = ""

    def remove(self):
        if self.equation != "":
            if self.equation.endswith(")"): 
                self.inPar = True 
                self.doublePar = True
            self.equation = self.equation[:-1]
            self.inputField.delete(0, END)
            self.inputField.insert(0, self.equation)

    def key_press(self, event):
        key = event.char

        if key == "1" or key == "2" or key == "3" or key == "4" or key == "5" or key == "6" or key == "7" or key == "8" or key == "9" or key == "0" or key == "+" or key == "-" or key == "*" or key == "/" or key == "^" or key == "a" or key == "c" or key == "s" or key == "." or key == "!":
            self.div_string(key)
        elif key == "=":
            self.equal()
