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
        self.exprArray = re.findall(r'[+-\/\*\^√]+|[|]?[(]?[-]?\d+[.]?\d*[)]?[!]?[|]?', exprString)  

        for num in range(len(self.exprArray)):
            try:
                self.solve_fact(num)
                self.solve_abs(num)
                self.solve_par(num)
                self.convert_to_num(num)
            except:
                break

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
            ## iterator of loop increased
            index+=1

    ##
    #  @brief solves expressions containing sum
    #  
    #  @param self the object pointer
    #
    def solve_sum(self):
        ## index of expression array
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
            ## iterator of loop increased
            index += 1

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
            ## ABS NOT WORKING (after |num|num doesnt throw error or always throws error with this condition) !!!!!!!!!!!!!!!
            if self.exprArray[numIndex + 1]: 
                if is_int(self.exprArray[numIndex + 20]):
                    raise Exception("Bad numbers") 
            numFound = int_or_float(self.exprArray[numIndex][absSymbol + 1:-1])
            self.exprArray[numIndex] = str(absolute(numFound))

    def solve_par(self, numIndex):
        num = self.exprArray[numIndex]
        x = num.find("(")

        if x != -1:
            numExt = re.search(r'[-]?\d+[.]?\d*', num)
            newNum = str(numExt.group()) if numExt else None

            if newNum:
                if self.exprArray[numIndex - 1] == "-":
                    newNum = absolute(int_or_float(newNum))
                    self.exprArray[numIndex - 1] = "+"
                self.exprArray[numIndex] = str(newNum)

    def convert_to_num(self, numIndex):
        num = self.exprArray[numIndex]
        if is_int(num):
            self.exprArray[numIndex] = int_or_float(self.exprArray[numIndex])

    def solve_fact(self, numIndex):
        num = self.exprArray[numIndex]
        x = num.find("!")

        if x != -1:
            numExt = re.search(r'[-]?\d+[.]?\d*', num)
            newNum = int_or_float(numExt.group()) if numExt else None

            if newNum:
                self.exprArray[numIndex] = str(fact(newNum))