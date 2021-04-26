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
#  @file gui_func.py
# 
#  @author Dominika Sedilekova
#
#  @brief Formatting input and output from gui
#

## @package Tkinter
#  Library with gui modules.
## @package tkinter
#  Library with gui modules.
try:
    from Tkinter import END, messagebox 
except ImportError:
    from tkinter import END, messagebox
  
from calculator import Calculator, is_int, int_or_float, absolute
## @package decimal
#  Support for fast correctly-rounded decimal floating point arithmetic..
from decimal import Decimal
## @package re
#  Support for regular expressions (RE).
import re
## @package os
#  OS routines for NT or Posix depending on what system we're on.
import os

##
#  @brief formates input and output from gui 
class Gui_Functions:
    
    ## 
    #  @brief the constructor
    #  
    #  @param self the object pointer
    #  @param inputField input and output field from passed gui
    #  @param expressionField field, where expression is outputted from passed gui
    #  @param inputScrollBar scrollbar of input field
    # 
    #  Initiates member variables.
    def __init__(self, inputField, expressionField, inputScrollBar):
        self.inputField = inputField
        self.expression = ""
        self.result = 0
        self.ansResult = 0
        self.ansAddPar = False
        self.toDelete = False
        self.addPar = False
        self.doublePar = False
        self.inPar = False
        self.calculator = ""
        self.expressionField = expressionField
        self.doubleClear = False
        self.addAbs = False
        self.deleteAbs = False
        self.lastExpressionLength = len(self.expression)
        self.inputScrollBar = inputScrollBar

    ## 
    #  @brief calculates expession
    #  
    #  @param self the object pointer
    #  @param expr expression as string
    #
    def calculate(self, expr):
        ## initiates calculator from Calculator module
        try:
            self.calculator = Calculator(expr)
        except (ValueError, ZeroDivisionError) as e:
            messagebox.showerror("Error", str(e))
            return "ERROR!"
        except:
            return "ERROR!"

        ## iterator for loop
        i = 0
        ## loops to solve sections of expression one by one, until only one value is left or error has occurred
        while i < self.calculator.exprArrayLen:
            try:
                self.calculator.solve_square_root()
                self.calculator.solve_exp()
                self.calculator.solve_mult()
                self.calculator.solve_div()
                self.calculator.solve_sub()
                self.calculator.solve_sum()
            except (ValueError, ZeroDivisionError) as e:
                messagebox.showerror("Error", str(e))
                return "ERROR!"
            except:
                return "ERROR!"
            ## iterator of loop is increased
            i += 1

        ## if there are more than one value as result of calculation error is returned
        if self.calculator.exprArrayLen > 1:
            return "ERROR!"

        ## result is saved from first index of final expression array as string
        resultStr = str(self.calculator.exprArray[0])

        # return str(self.calculator.exprArray)


        ## if value is decimal number with more than 5 decimal places
        if absolute(Decimal(resultStr).as_tuple().exponent) > 5:
            ## value is returned as rounded decimal number with five decimal places 
            return str(round(int_or_float(resultStr), 5))
        ## else value is returned
        else: 
            return resultStr

    ## 
    #  @brief open help pdf with 
    #  
    #  @param self the object pointer
    #
    def open_help(self):
        try:
            os.startfile("dokumentace.pdf")
        except:
            os.chdir("../")
            os.startfile("dokumentace.pdf")


    ## 
    #  @brief add absolute value pipes (|) around number
    #  
    #  @param self the object pointer
    # 
    def add_abs(self):
        ## finds if number was entered last
        findNum = re.search(r'[-]?\d+[.]?\d*$', self.expression)
        foundNum = int_or_float(findNum.group()) if findNum else None
        ## if number was found
        if foundNum:
            ## saves length of number as string
            numLen = len(str(foundNum))
            ## if expression contains 0 before given number 
            ## (expression automatically adds 0, if only operand is given at the beginning of the expression)
            if self.expression == ("0" + str(foundNum)):
                ## expression ans input field are cleared
                self.expression = ""
                self.inputField.delete(0, END)
            ## if number is not at the beginning
            else:
                i = 0
                ## removes number from expression by it's length
                while i < numLen:
                    self.remove()
                    i += 1
            ## add pipes to number
            foundNum = "|" + str(foundNum) + "|"
            ## concactinates the number
            self.conc_string(foundNum)

    ## 
    #  @brief deletes absolute value
    #  
    #  @param self the object pointer
    #
    def delete_abs(self):
        ## checks if number with absolute value pipes is at the end of expression
        findNum = re.search(r'[|][-]?\d+[.]?\d*[|]$', self.expression)
        foundNum = str(findNum.group()) if findNum else None
        ## if the number was found
        if foundNum:
            numLen = len(foundNum)
            ## the whole number along with pipes is removed from expression
            self.expression = self.expression[:(-numLen + 1)]

    ## 
    #  @brief adds root symbol to expression
    #  
    #  @param self the object pointer
    #
    def check_root(self):
        ## checks if number is at the end of expression
        findNum = re.search(r'[-]?\d+[.]?\d*$', self.expression)
        foundNum = int_or_float(findNum.group()) if findNum else None
        ## if number is found, only root symbol is added
        if foundNum:
            self.conc_string("√")
        ## if number isn't at the end 2 and root symbol is added to expression (automatically counts square root)
        else:
            self.conc_string("2√")

    ## 
    #  @brief adds paranthesis symbol to expression
    #  
    #  @param self the object pointer
    #  @param input values added
    #
    def add_paranth(self, input):
        ## checks if number with + or - sign is at the end of expression
        findNum = re.search(r'[+]\d+[.]?\d*$|[-]?\d+[.]?\d*^|[-]?\d+[.]?\d*$', self.expression)
        foundNum = str(findNum.group()) if findNum else None
        ## sets is in paratheses to false
        self.inPar = False
        ## sets add paratheses to false
        self.addPar = False
        ## if number is found
        if foundNum:
            numLen = len(str(foundNum))
            ## removes the number by it's length
            i = 0
            while i < numLen:
                self.remove()
                i += 1
            ## if ending paratheses was deleted
            if self.doublePar:
                ## save number with ending paranthesis
                foundNum = str(foundNum) + ")"
                ## sets doublePar back to false
                self.doublePar = False
            else:
                ## save number with paranthesis
                foundNum = "(" + str(foundNum) + ")"
            ## concactenate the number
            self.conc_string(foundNum + input)

    ## 
    #  @brief adds decimal point
    #  
    #  @param self the object pointer
    #
    def add_decimal(self):
        ## checks if number is at the end of expression
        findNum = re.search(r'[-]?\d+[.]\d*$', self.expression)
        foundNum = str(findNum.group()) if findNum else None
        ## if number is found
        if not foundNum:
            ## if expression is empty or if last in expression is not number
            if self.expression == "" or not is_int(self.expression[len(self.expression) - 1]):
                ## adds zero before dot
                self.conc_string("0.")
            else:
                ## adds only dot
                self.conc_string(".")

    ## 
    #  @brief turns the scrollbar widget on/off depending on input size
    #  
    #  @param self the object pointer
    #
    def input_scrollbar_on_off(self):
        if len(str(self.expression)) > 24:
            self.inputScrollBar.place(width = 335, relheight = 1, x = -12)
        else: 
            self.inputScrollBar.place_forget()

    ## 
    #  @brief concactinates expression and clears input field
    #  
    #  @param self the object pointer
    #  @input string
    #
    def conc_string(self, input):
        ## concactinates string to expression
        self.expression += str(input)
        ## currently added input to input field
        current = self.inputField.get()
        ## clears input field
        self.inputField.delete(0, END)
        ## inserts current with input to snput field 
        self.inputField.insert(0, str(current) + str(input))

    ## 
    #  @brief checks if paranthesis are needed to be added
    #  
    #  @param self the object pointer
    #  @input current input
    #
    def checkIfAddparanthesis(self, input):
        ## if number in paranthesis
        if self.inPar:
            ## if input is some operand
            if input == "-" or input == "+" or input == "/" or input == "*" or input == "^" or input == "√":
                ## sets value addPar to True so closing paranthesis would be added
                self.addPar = True
        ## if number is not in paranthesis
        if not self.inPar:
            ## if expression ends with some operand
            if self.expression.endswith("-") or self.expression.endswith("+") or self.expression.endswith("/") or self.expression.endswith("*") or self.expression.endswith("^") or self.expression.endswith("√"):
                ## if input is -
                if input == "-" or input == "+":
                    ## sets inPar boolean to true
                    self.inPar = True
                ## if input is n and ans in negative number
                elif input == "n" and int_or_float(self.ansResult) < 0:
                    ## sets add paratheses around ans value to true
                    self.ansAddPar = True        

    ## 
    #  @brief divides input values
    #  
    #  @param self the object pointer
    #  @input current input
    #
    def div_input(self, input):   
        ## sets input field focus on the end of line
        self.inputField.after(0, self.inputField.xview_moveto, 1) 

        self.input_scrollbar_on_off()    

        ## if toDelete boolean is set
        if self.toDelete:
            ## clears input field and expression
            self.inputField.delete(0, END)
            self.expression = "" 
            ## inserts blank expression into input field
            self.inputField.insert(0, self.expression)  
            ## clears expression field
            self.expressionField.delete(0, END)
            ## inputs result onto expression field
            self.expressionField.insert(0, self.result)  
            ## resets toDelete boolean to false
            self.toDelete = False

        ## if doubleClear boolean is set
        if self.doubleClear:
            ## clears expression field
            self.expressionField.delete(0, END)
            ## resets doubleClear boolean to false 
            self.doubleClear = False
        
        ## checks occurrences of operands to add paranthesis if needed
        self.checkIfAddparanthesis(input)
        
        if input == "c":
            self.clear_input_field()
            ## sets doubleClear to true
            self.doubleClear = True
        elif input == ".":
            self.add_decimal()
        elif input == "s":
            self.check_root()
        elif input == "a":
            self.add_abs() 
        ## if key n is pressed
        elif input == "n":
            ## if ans value is negative last in expression is some operand paranthesis are added
            if self.ansAddPar:
                self.conc_string("(" + self.ansResult + ")")
                self.ansAddPar = False
            ## ans value is concactinated to expression string
            else:
                self.conc_string(self.ansResult)
        ## if addPar is set to true
        elif self.addPar:
            self.add_paranth(input)
        ## if expression is blank and input is not a number
        elif self.expression == "" and not is_int(input): 
            ## expression is set to 0
            self.expression = "0" + self.expression
            self.conc_string(input)
        ## if expression is not blank and first item is -
        elif self.expression != "" and self.expression[0] == "-":
            ## expression is set to 0
            self.expression = "0" + self.expression
            self.conc_string(input)

        else: 
            self.conc_string(input)
            
    ##
    #  @brief clears input field
    #  
    #  @param self the object pointer
    #
    def clear_input_field(self):
        self.inputField.delete(0, END)
        ## if calculator is set, expression array is cleared
        if self.calculator:
            self.calculator.clear_array()
        self.expression = ""
        self.input_scrollbar_on_off()

    ##
    #  @brief evaluates expression
    #  
    #  @param self the object pointer
    #
    def equal(self):
        ## if inPar is set to true, sets addPar to true
        if self.inPar:
            self.addPar = True
        ## if addPar is set to true adds ending paranthesis 
        if self.addPar:
            self.add_paranth("")
        
        ## clears input field
        self.inputField.delete(0, END) 
        
        ## if expression is blank
        if self.expression == "":
            ## calculates only 0 and inputs result onto screen
            self.result = self.calculate("0")
            self.inputField.insert(0, self.result)
        ## if expression contains only number
        elif is_int(self.expression):
            ## converts string to number and stores it
            num = int_or_float(self.expression)
            ## if number is negative
            if num < 0:
                ## store result of: 0 - entered number
                self.result = self.calculate("0" + self.expression)
            else:
                ## store result of: 0 - entered number
                self.result = self.calculate(self.expression)
            ## print result onto input field
            self.inputField.insert(0, self.result)
            ## clear expression field
            self.expressionField.delete(0, END)
            ## print result onto expression(result) field
            self.expressionField.insert(0, self.result)
        ## if first value is minus sign
        elif self.expression[0] == "-":
            ## calls div_input function with blank input
            self.div_input("")
            ## clears input field
            self.clear_input_field()
        else:
            ## stores calculated result
            self.result = self.calculate(self.expression)
            ## prints result onto screen
            self.inputField.insert(0, self.result)

        ## if error occurred 
        if self.result == "ERROR!":
            ## clears expression field and adds expression that caused error
            self.expressionField.delete(0, END)
            self.expressionField.insert(0, self.expression)
            ## sets result to 0
            self.result = 0
        else:
            ## expression field is cleared and expression is printed there
            self.expressionField.delete(0, END)
            self.expressionField.insert(0, self.expression)
            ## stores result as ans value
            self.ansResult = self.result
            ## clears expression array 
            self.calculator.clear_array()
            self.expression = self.result
        ## toDelete is set to true
        self.toDelete = True

        self.input_scrollbar_on_off()

    ##
    #  @brief removes characters from expression one by one form end
    #  
    #  @param self the object pointer
    #
    def remove(self):
        ## moves entry focus to the end of line, when line is too long
        self.inputField.after(0, self.inputField.xview_moveto, 1)

        self.input_scrollbar_on_off()
        
        ## if expression is not empty
        if self.expression != "":
            ## if expression ends with ending parenthesis
            if self.expression.endswith(")"): 
                ## inPar and doublePar is set to true
                self.inPar = True 
                self.doublePar = True
            ## expression ends with pipe, removes whole absolute value
            if self.expression.endswith("|"): 
                self.delete_abs()
            ## removes last character from expression
            self.expression = self.expression[:-1]
            ## clears input field
            self.inputField.delete(0, END)
            ## prints expression onto input field
            self.inputField.insert(0, self.expression)

    ##
    #  @brief checks which key was pressed
    #  
    #  @param self the object pointer
    #  @event what type of event has occurred
    #
    def key_press(self, event):
        ## key variable is set to event which means: pressed character
        key = event.char

        ## allowed key presses are passed to div_input function
        if key == "1" or key == "2" or key == "3" or key == "4" or key == "5" or key == "6" or key == "7" or key == "8" or key == "9" or key == "0" or key == "+" or key == "-" or key == "*" or key == "/" or key == "^" or key == "a" or key == "c" or key == "s" or key == "." or key == "!" or key == "n":
            self.div_input(key)
        ## if = is pressed equal function is called
        elif key == "=":
            self.equal()
