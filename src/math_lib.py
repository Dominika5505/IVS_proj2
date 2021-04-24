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
#                    Petr Pucek             <xpucek03@stud.fit.vutbr.cz>   
#
# ======== Copyright (c) 2021, Vepro-knedlo-zelo s bryndzou, All rights reserved. ============ #

## 
#  @file math_lib.py
# 
#  @author Dominika Sedilekova
#  @author Petr Pucek
#
#  @brief Implementation of the mathematic functions library
#

##
#  @brief sum
#  adds two numbers
#
#  @param num1 first number for addition
#  @param num2 second number for addition
#
#  @return value of addition of two numbers
#
def sum(num1, num2):

    return num1 + num2

##
#  @brief sub
#  subtracts two numbers
#
#  @param num1 first number for subtraction
#  @param num2 second number for subtraction
#
#  @return value of subtraction of two numbers
#
def sub(num1, num2):
    
    return num1 - num2

##
#  @brief mult
#  multiples two numbers
#
#  @param num1 first number for multiplication
#  @param num2 second number for multiplication
#
#  @return value of multiplication of two numbers
#
def mult(num1, num2):
    
    return num1 * num2

##
#  @brief div
#  divides two numbers
#
#  @param num1 first number for division
#  @param num2 second number for division
#
#  @return value of division of two numbers
#
def div(num1, num2):
    
    if (num2 == 0):
        raise ValueError("Division by zero!")

    return num1 / num2

##
#  @brief fact
#  calculates factorial of a number
#
#  @param num number to factore
#
#  @return value of factorial of a number
#
def fact(num):

    if (num < 0) or isinstance(num, float):
        raise ValueError("Factorial of decimal number doesn't exist!")

    return 1 if (num==1 or num==0) else num * fact(num - 1)

##
#  @brief exp
#  calculates exponent of a number
#
#  @param num base of power
#  @param exp exponent of power
#
#  @return value of exponentiation
#
def exp(num, exp):
    
    if exp == 0:
        return 1

    return num ** exp

##
#  @brief absolute
#  calculates absolute value of a number
#
#  @param num number
#
#  @return absolute value of the number
#
def absolute(num):
    
    return -num if(num < 0) else num

##
#  @brief div
#  calculates square root of a number
#
#  @param num radicand of root
#  @param deg degree of root
#
#  @return value of n-th root
#
def root(num, deg):
    
    if deg % 2 == 0:
        if num < 0:
            raise ValueError("")
    
    if isinstance(deg, float):
        raise ValueError("Degree of root can't be decimal number!")
    if (deg < 0): 
        raise ValueError("Degree of root can't be negative number!")
    if num == 0:
        return 0
    if num < 0:
        result = abs(num)**(1/deg)
        return -result

    return num**(1/deg)
