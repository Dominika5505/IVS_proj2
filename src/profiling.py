# ======== Copyright (c) 2021, Vepro-knedlo-zelo s bryndzou, All rights reserved. ============ #
#
#  $Purpose:         Profiling - python programme
#  
#  $University:      Brno University of Technology
#  $Faculty:         Faculty of Information Technology
#  $Programme:       Information Technology (Bachelor)
#  $Course:          Practical Aspects of Software Design (IVS)
#  $Academic year:   2020/2021 
#
#  $Authors:         Petr Pucek             <xpucek03@stud.fit.vutbr.cz>   
#
# ======== Copyright (c) 2021, Vepro-knedlo-zelo s bryndzou, All rights reserved. ============ #

import math_lib
import sys
import cProfile
import re

## 
#  @file math_lib.py
# 
#  @author Petr Pucek
#
#  @brief Implementation of the math function for standard deviation
#

##
#  @brief read_input
#  reads nums from stdin and adds them to a list 
#
#  @return list of nums
#
def read_input():
    

    nums = []
    line = sys.stdin.readline() ## reading of a first line from stdin

    for num in line.split():
        num = int(num)
        nums.append(num)

    return nums

##
#  @brief deviation_calc
#  calculates standard deviation
#
#  @param nums list with numbers
#
#  @return value of standard deviation
#
def deviation_calc(nums):

    n = len(nums)

    return math_lib.root((1/(n-1))*(sum_nums(squared_nums(nums))-n*math_lib.exp(mean_calc(nums), 2) ), 2)

##
#  @brief mean_calc
#  calculates arithmetic mean of list of nums
#
#  @param nums list of number
#
#  @return value of mean
#
def mean_calc(nums):
    
    return math_lib.div(sum_nums(nums), len(nums)) 

##
#  @brief sum_nums
#  calculates sum of a list of nums
#
#  @param nums list of numbers
#
#  @return value of sum of list
#
def sum_nums(nums):
    
    sum = 0
    for num in nums:
        sum = math_lib.sum(sum, num)

    return sum

##
#  @brief squared_nums
#  creates a list of squared nums from a different list 
#
#  @param nums list of numbers
#
#  @return list of squared nums
#
def squared_nums(nums):
    
    sqrdNums = []

    for num in nums:
        sqrdNums.append(math_lib.exp(num, 2))

    return sqrdNums   

##
#  @brief main
#  main function to startup the programme 
#
def main():
    nums = read_input()
    s = deviation_calc(nums)
    print("The value of the standard deviation is: " + str(s))
    print()
    return

## start of a programme
if __name__ == '__main__':
    cProfile.run('main()')
    
