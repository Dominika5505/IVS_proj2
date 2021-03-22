from math_lib import *
import re

def is_int(str):
    isInt = True

    try:
        int(str)
    except ValueError:
        isInt = False
    
    return isInt

def int_or_float(num):
    return int(num) if float(num).is_integer() else float(num)
class Calculator:
    eqArray = []
    numberArray = []
    mathSymbols = []
    eqArrayLen = 0
    
    def __init__(self, eqString):
        self.eqArray = re.findall(r'[+-\/\*\^√]+|[|]?[(]?[-]?\d+[.]?\d*[)]?[!]?[|]?', eqString)  

        for num in range(len(self.eqArray)):
            self.solveFact(num)
            self.solveAbs(num)
            self.solvePar(num)
            self.convertToNum(num)

        self.eqArrayLen = len(self.eqArray)

    def clearArray(self):
        self.eqArray.clear()
        self.numberArray.clear()
        self.mathSymbols.clear()
        self.eqArrayLen = 0
    
    def solveSquareRoot(self):
        index = 0
        while index < self.eqArrayLen:

            if self.eqArray[index] == "√":

                num = int_or_float(self.eqArray[index + 1])
                deg = int_or_float(self.eqArray[index - 1])

                result = root(num, deg)
                
                # result = root(self.eqArray[index + 1], self.eqArray[index - 1])
                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.insert(index - 1, int_or_float(result))
                self.eqArrayLen -= 2

            index+=1

    def solveExp(self):
        index = 0
        while index < self.eqArrayLen:

            if self.eqArray[index] == "^":
                num = int_or_float(self.eqArray[index - 1])
                exponent = int_or_float(self.eqArray[index + 1])

                result = exp(num, exponent)

                # result = exp(self.eqArray[index - 1], self.eqArray[index + 1])
                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.insert(index - 1, int_or_float(result))
                self.eqArrayLen -= 2

            index+=1

    def solveMult(self):
        index = 0
        while index < self.eqArrayLen:

            if self.eqArray[index] == "*":
                num1 = int_or_float(self.eqArray[index - 1])
                num2 = int_or_float(self.eqArray[index + 1])

                result = mult(num1, num2)

                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.insert(index - 1, int_or_float(result))
                self.eqArrayLen -= 2

            index+=1

    def solveDiv(self):
        index = 0
        while index < self.eqArrayLen:

            if self.eqArray[index] == "/":

                num1 = int_or_float(self.eqArray[index - 1])
                num2 = int_or_float(self.eqArray[index + 1])

                result = div(num1, num2)

                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.insert(index - 1, int_or_float(result))
                self.eqArrayLen -= 2

            index+=1

    def solveSum(self):
        index = 0
        # while index < self.eqArrayLen || index != 1:
        while index < self.eqArrayLen:

            if self.eqArray[index] == "+":
                num1 = int_or_float(self.eqArray[index - 1])
                num2 = int_or_float(self.eqArray[index + 1])

                result = sum(num1, num2)

                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.insert(index - 1, int_or_float(result))
                self.eqArrayLen -= 2

            index += 1

    def solveSub(self):
        index = 0
        while index < self.eqArrayLen:

            if self.eqArray[index] == "-":

                num1 = int_or_float(self.eqArray[index - 1])
                num2 = int_or_float(self.eqArray[index + 1])

                result = sub(num1, num2)

                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.pop(index - 1)
                self.eqArray.insert(index - 1, int_or_float(result))
                self.eqArrayLen -= 2

            index+=1

    def solveAbs(self, numIndex):
        num = self.eqArray[numIndex]
        x = num.find("|")

        if x != -1:
            numFound = int_or_float(self.eqArray[numIndex][x + 1:-1])
            self.eqArray[numIndex] = str(abs(numFound))

    def solvePar(self, numIndex):
        num = self.eqArray[numIndex]
        x = num.find("(")

        if x != -1:
            numExt = re.search(r'[-]?\d+[.]?\d*', num)
            newNum = str(numExt.group()) if numExt else None

            if newNum:
                if self.eqArray[numIndex - 1] == "-":
                    newNum = abs(int_or_float(newNum))
                    self.eqArray[numIndex - 1] = "+"
                self.eqArray[numIndex] = str(newNum)

    def convertToNum(self, numIndex):
        num = self.eqArray[numIndex]
        if is_int(num):
            self.eqArray[numIndex] = int_or_float(self.eqArray[numIndex])

    def solveFact(self, numIndex):
        num = self.eqArray[numIndex]
        x = num.find("!")

        if x != -1:
            numExt = re.search(r'[-]?\d+[.]?\d*', num)
            newNum = int_or_float(numExt.group()) if numExt else None

            if newNum:
                self.eqArray[numIndex] = str(fact(newNum))