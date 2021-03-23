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

def sum(num1, num2):
    ##
    #  @brief sum
    #  adds two numbers
    #
    #  @param num1 first number for addition
    #  @param num2 second number for addition
    #
    #  @return value of addition of two numbers

    return num1 + num2

def sub(num1, num2):
    ##
    #  @brief sub
    #  subtracts two numbers
    #
    #  @param num1 first number for subtraction
    #  @param num2 second number for subtraction
    #
    #  @return value of subtraction of two numbers

    return num1 - num2

def mult(num1, num2):
    ##
    #  @brief mult
    #  multiples two numbers
    #
    #  @param num1 first number for multiplication
    #  @param num2 second number for multiplication
    #
    #  @return value of multiplication of two numbers

    return num1 * num2

def div(num1, num2):
    ##
    #  @brief div
    #  divides two numbers
    #
    #  @param num1 first number for division
    #  @param num2 second number for division
    #
    #  @return value of division of two numbers

    if (num2 == 0):
        raise ZeroDivisionError

    return num1 / num2

def fact(num):
    ##
    #  @brief fact
    #  calculates factorial of a number
    #
    #  @param num number to factore
    #
    #  @return value of factorial of a number

    if (num < 0) or isinstance(num, float):
        raise ValueError

    return 1 if (num==1 or num==0) else num * fact(num - 1)

def exp(num, exp):
    ##
    #  @brief exp
    #  calculates exponent of a number
    #
    #  @param num base of power
    #  @param exp exponent of power
    #
    #  @return value of exponentiation
    if exp == 0:
        return 1
    if (exp < 0) or isinstance(exp, float):
        raise ValueError

    return num ** exp

def absolute(num):
    ##
    #  @brief absolute
    #  calculates absolute value of a number
    #
    #  @param num number
    #
    #  @return absolute value of the number

    return -num if(num < 0) else num

def root(num, deg):
    ##
    #  @brief div
    #  calculates square root of a number
    #
    #  @param num radicand of root
    #  @param deg degree of root
    #
    #  @return value of n-th root

    if deg % 2 == 0:
        if num < 0:
            raise ValueError
    
    if (deg < 0) or isinstance(deg, float):
        raise ValueError
    if num == 0:
        return 0
    if num < 0:
        result = abs(num)**(1/deg)
        return -result

    return num**(1/deg)
