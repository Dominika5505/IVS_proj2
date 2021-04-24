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
#  @file calculator.py
# 
#  @author Dominika Sedilekova
#
#  @brief Implementation of the calculator functions
#

## @package math_lib
#  Library with basic math functions.
from math_lib import *
## @package re
#  Support for regular expressions (RE).
import re


##
#  @brief checks if given string is integer
#
#  @param str string
#
#  @return boolean value determining if string is int or not
def is_int(str):
    isInt = True

    try:
        int(str)
    except ValueError:
        isInt = False
    
    return isInt

##
#  @brief converts the number to int or float value
#
#  @param num number
#
#  @return integer or float number
def int_or_float(num):
    return int(num) if float(num).is_integer() else float(num)

##
#  @brief calculates compound expressions using math library 
class Calculator:
    
    ## 
    #  @brief the constructor
    #  
    #  @param self the object pointer
    #  @param exprString expression string passed from gui input
    # 
    #  Initiates member variables.
    #  Divides passed expression string into array.
    #  Solves factorial, absolute values, removes parantheses, and converts string to number
    def __init__(self, exprString):
        ## divides expression string into array of operands and numbers as strings
        self.exprArray = re.findall(r'[+-\/\*\^√]+|[|]?[(]?[-]?\d+[.]?\d*[)]?[!]?[|]?', exprString)  
        ## solves factorial, absolute values, occurrence of parantheses in loop
        for num in range(len(self.exprArray)):
            try:
                self.solve_fact(num)
                self.solve_abs(num)
                self.solve_par(num)
                ## each element that is number is converted to number 
                self.convert_to_num(num)
            ## if error occurred stops solving and breaks out of loop (error is already stored in result)
            except ValueError as e:
                raise ValueError(str(e))
                # break
        ## saves length of array with expression
        self.exprArrayLen = len(self.exprArray)

    ## 
    #  @brief deletes array of expression numbers and mathematic signs
    #  
    #  @param self the object pointer
    #
    def clear_array(self):
        self.exprArray.clear()
        self.exprArrayLen = 0
    
    ## 
    #  @brief solves expressions containing root of a number
    #  
    #  @param self the object pointer
    #
    def solve_square_root(self):
        ## index of expression array
        index = 0
        ## loops through expression array
        while index < self.exprArrayLen:
            ## finds index that contains only root symbol
            if self.exprArray[index] == "√":

                ## number to get root of (found on index after root symbol)
                num = int_or_float(self.exprArray[index + 1])
                ## degree of root function (found on index before root symbol)
                deg = int_or_float(self.exprArray[index - 1])

                ## result of root function
                result = root(num, deg)
                
                ## removes num, root symbol and deg one by one from array
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                ## inserts result into array in place of deleted num, root symbol and deg
                self.exprArray.insert(index - 1, int_or_float(result))
                ## modifies array length, decreasing it by 2 (3 items deleted, 1 inserted)
                self.exprArrayLen -= 2
                index = 0
            ## iterator of loop increased
            index += 1

    ##
    #  @brief solves expressions containing exponent
    #  
    #  @param self the object pointer
    #
    def solve_exp(self):
        ## index of expression array
        index = 0
        ## loops through expression array
        while index < self.exprArrayLen:
            ## finds index that contains only exponential symbol
            if self.exprArray[index] == "^":

                ## the base of exponent (found on index before root symbol)
                num = int_or_float(self.exprArray[index - 1])
                ## exponent of exponential function (found on index before root symbol)
                exponent = int_or_float(self.exprArray[index + 1])

                ## result of exponential function
                result = exp(num, exponent)

                ## removes num, exponent symbol and exponent one by one from array
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                ## inserts result into array in place of deleted num, exponent symbol and exponent
                self.exprArray.insert(index - 1, int_or_float(result))
                ## modifies array length, decreasing it by 2 (3 items deleted, 1 inserted)
                self.exprArrayLen -= 2
                index = 0
            ## iterator of loop increased
            index+=1

    ##
    #  @brief solves expressions containing multiplication
    #  
    #  @param self the object pointer
    #
    def solve_mult(self):
        ## index of expression array
        index = 0
        ## loops through expression array
        while index < self.exprArrayLen:

            ## finds index that contains only multiplication symbol
            if self.exprArray[index] == "*":
                ## first number for multiplication (found on index before root symbol)
                num1 = int_or_float(self.exprArray[index - 1])
                ## second number for multiplication (found on index before root symbol)
                num2 = int_or_float(self.exprArray[index + 1])

                ## result of multiply function
                result = mult(num1, num2)

                ## removes num1, multiplication symbol and num2 one by one from array
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                ## inserts result into array in place of deleted num1, multiplication symbol and num2
                self.exprArray.insert(index - 1, int_or_float(result))
                ## modifies array length, decreasing it by 2 (3 items deleted, 1 inserted)
                self.exprArrayLen -= 2
                index = 0
            ## iterator of loop increased
            index+=1

    ##
    #  @brief solves expressions containing division
    #  
    #  @param self the object pointer
    #
    def solve_div(self):
        ## index of expression array
        index = 0
        ## loops through expression array
        while index < self.exprArrayLen:

            ## finds index that contains only division symbol
            if self.exprArray[index] == "/":
                ## first number for division (found on index before root symbol)
                num1 = int_or_float(self.exprArray[index - 1])
                ## second number for division (found on index before root symbol)
                num2 = int_or_float(self.exprArray[index + 1])
                
                ## result of divide function
                result = div(num1, num2)

                ## removes num1, division symbol and num2 one by one from array
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                ## inserts result into array in place of deleted num1, division symbol and num2
                self.exprArray.insert(index - 1, int_or_float(result))
                ## modifies array length, decreasing it by 2 (3 items deleted, 1 inserted)
                self.exprArrayLen -= 2
                index = 0
            ## iterator of loop increased
            index+=1

    ##
    #  @brief solves expressions containing sum
    #  
    #  @param self the object pointer
    #
    def solve_sum(self):
        # ## index of expression array
        index = 0
        ## loops through expression array
        while index < self.exprArrayLen:

            ## finds index that contains only sum symbol
            if self.exprArray[index] == "+":

                ## first number for sum (found on index before root symbol)
                num1 = int_or_float(self.exprArray[index - 1])
                ## second number for sum (found on index before root symbol)
                num2 = int_or_float(self.exprArray[index + 1])

                ## result of sum function
                result = sum(num1, num2)

                ## removes num1, sum symbol and num2 one by one from array
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                ## inserts result into array in place of deleted num1, sum symbol and num2
                self.exprArray.insert(index - 1, int_or_float(result))
                ## modifies array length, decreasing it by 2 (3 items deleted, 1 inserted)
                self.exprArrayLen -= 2
                index = 0
            
            ## iterator of loop increased
            index+=1
            

    ##
    #  @brief solves expressions containing subtraction
    #  
    #  @param self the object pointer
    #
    def solve_sub(self):
        ## index of expression array
        index = 0
        ## loops through expression array
        while index < self.exprArrayLen:

            ## finds index that contains only subtraction symbol
            if self.exprArray[index] == "-":

                ## first number for subtraction (found on index before root symbol)
                num1 = int_or_float(self.exprArray[index - 1])
                ## second number for subtraction (found on index before root symbol)
                num2 = int_or_float(self.exprArray[index + 1])

                ## result of sub function
                result = sub(num1, num2)

                ## removes num1, subtraction symbol and num2 one by one from array
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                self.exprArray.pop(index - 1)
                ## inserts result into array in place of deleted num1, subtraction symbol and num2
                self.exprArray.insert(index - 1, int_or_float(result))
                ## modifies array length, decreasing it by 2 (3 items deleted, 1 inserted)
                self.exprArrayLen -= 2
                index = 0
            
            ## iterator of loop increased
            index+=1

    ##
    #  @brief solves expressions containing absolute value
    #  
    #  @param self the object pointer
    #  @param numIndex index of number in array
    #
    def solve_abs(self, numIndex):
        ## element in index of array
        num = self.exprArray[numIndex]
        ## finds pipe symbol in element
        absSymbol = num.find("|")

        ## if symbol is in element
        if absSymbol != -1:
            ## removes pipes from element and convert to number
            numFound = int_or_float(self.exprArray[numIndex][absSymbol + 1:-1])
            ## replaces element with absolute value of converted number
            self.exprArray[numIndex] = str(absolute(numFound))

    ##
    #  @brief solves expressions with negative numbers
    #  
    #  @param self the object pointer
    #  @param numIndex index of number in array
    #
    def solve_par(self, numIndex):
        ## element in index of array
        num = self.exprArray[numIndex]
        ## if parantheses symbol is in element
        if num.find("(") != -1:
            ## searches for decimal or integer number in element
            numExt = re.search(r'[-]?\d+[.]?\d*', num)
            ## returns number as string or None if number wasn't found
            newNum = str(numExt.group()) if numExt else None

            ## if number was found
            if newNum:
                ## if the element before is minus sign
                if self.exprArray[numIndex - 1] == "-":
                    ## replaces number with its absolute value
                    newNum = absolute(int_or_float(newNum))
                    ## minus sign replaces by plus sign
                    self.exprArray[numIndex - 1] = "+"
                ## replaces element by new number as string
                self.exprArray[numIndex] = str(newNum)

    ##
    #  @brief converts string to number
    #  
    #  @param self the object pointer
    #  @param numIndex index of number in array
    #
    def convert_to_num(self, numIndex):
        ## element in index of array
        num = self.exprArray[numIndex]
        ## checks if num is int
        if is_int(num):
            ## replaces element as int or float
            self.exprArray[numIndex] = int_or_float(self.exprArray[numIndex])

    ##
    #  @brief converts string to number
    #  
    #  @param self the object pointer
    #  @param numIndex index of number in array
    #
    def solve_fact(self, numIndex):
        ## element in index of array
        num = self.exprArray[numIndex]

        ## if exclamation mark is in element
        if num.find("!") != -1:
            ## searches for decimal or integer number in element
            numExt = re.search(r'[-]?\d+[.]?\d*', num)
            ## returns number as int or float value or None if number wasn't found
            newNum = int_or_float(numExt.group()) if numExt else None

            ## if number was found
            if newNum:
                ## replaces element with result of factorial
                try:
                    self.exprArray[numIndex] = str(fact(int_or_float(newNum)))
                except ValueError as e:
                    # print(f"Argument Error: {e}")
                    errMsg = f"Argument Error: {e}"
                    print(errMsg)
                    raise ValueError(str(e))
