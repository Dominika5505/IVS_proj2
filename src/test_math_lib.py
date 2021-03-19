# ======== Copyright (c) 2021, Vepro-knedlo-zelo s bryndzou, All rights reserved. ============ #
#
#  $Purpose:         Calculator - tests for TDD
#  
#  $University:      Brno University of Technology
#  $Faculty:         Faculty of Information Technology
#  $Programme:       Information Technology (Bachelor)
#  $Course:          Practical Aspects of Software Design (IVS)
#  $Academic year:   2020/2021 
#
#  $Author:          Petr Pucek <xpucek03@stud.fit.vutbr.cz>
#
# ======== Copyright (c) 2021, Vepro-knedlo-zelo s bryndzou, All rights reserved. ============ #

import unittest
import math_lib # upcoming library of implemented functions

## 
#  @file test_math_lib.py
# 
#  @author Petr Pucek
#
#  @brief Implementation of the tests for Test-driven development
#

class TestMathOperations(unittest.TestCase):
     
    def test_sum(self):
        ##
        #  @brief test_sum
        #  checks accuracy of math function for addition
        # 

        # test for proving commutative property
        self.assertEqual(math_lib.sum(10, 5), 15)
        self.assertEqual(math_lib.sum(5, 10), 15)

        # test for addition with negative nums
        self.assertEqual(math_lib.sum(-10, 5), -5)
        self.assertEqual(math_lib.sum(10, -5), 5)
        self.assertEqual(math_lib.sum(-10, -5), -15)

        # test for addition with zero (neutral element)
        self.assertEqual(math_lib.sum(0, 5), 5)
        self.assertEqual(math_lib.sum(10, 0), 10)

        # test for addition with large nums
        self.assertEqual(math_lib.sum(573453876, 34346546), 607800422)

        # test for addition with decimal nums
        self.assertEqual(math_lib.sum(10.3554, 5.2057), 15.5611)


    def test_sub(self):
        ##
        #  @brief test_sub
        #  checks accuracy of math function for subtraction
        # 

        # test for disclaiming commutative property
        self.assertEqual(math_lib.sub(10, 5), 5)
        self.assertEqual(math_lib.sub(5, 10), -5)    
    
        # test for subtraction with negative nums
        self.assertEqual(math_lib.sub(-10, 5), -15)
        self.assertEqual(math_lib.sub(10, -5), 15)
        self.assertEqual(math_lib.sub(-10, -5), -5)

        # test for subtraction with zero 
        self.assertEqual(math_lib.sub(0, 5), -5)
        self.assertEqual(math_lib.sub(10, 0), 10) # zero as neutral element

        # test for subtraction with large nums
        self.assertEqual(math_lib.sub(573453876, 34346546), 539107330)
        self.assertEqual(math_lib.sub(453876, 34346546), -33892670)

        # test for subtraction with decimal nums
        self.assertEqual(math_lib.sub(10.3554, 5.2057), 5.1497)
        self.assertEqual(math_lib.sub(1.2945, 5.45765), -4.16315)

    def test_mult(self):
        ##
        #  @brief test_mult
        #  checks accuracy of math function for multiplication
        # 

        # test for proving commutative property
        self.assertEqual(math_lib.mult(10, 5), 50)
        self.assertEqual(math_lib.mult(5, 10), 50)    
    
        # test for multiplication with negative nums
        self.assertEqual(math_lib.mult(-10, 5), -50)
        self.assertEqual(math_lib.mult(10, -5), -50)
        self.assertEqual(math_lib.mult(-10, -5), 50)

        # test for multiplication with zero
        self.assertEqual(math_lib.mult(0, 5), 0)
        self.assertEqual(math_lib.mult(10, 0), 0)

        # test for multiplication with 1 (neutral element)
        self.assertEqual(math_lib.mult(10, 1), 10)

        # test for multiplication with large nums
        self.assertEqual(math_lib.mult(573453, 34346), 19695816738)

        # test for multiplication with decimal nums
        self.assertEqual(math_lib.mult(10.3554, 5.2057), 53.90710578)
        self.assertEqual(math_lib.mult(20, 0.05), 1)

    def test_div(self):
        ##
        #  @brief test_div
        #  checks accuracy of math function for division
        # 

        # test for disclaiming commutative property
        self.assertEqual(math_lib.div(10, 5), 2)
        self.assertEqual(math_lib.div(5, 10), 0.5)

        # test for division with negative nums
        self.assertEqual(math_lib.div(-10, 5), -2)
        self.assertEqual(math_lib.div(10, -5), -2)
        self.assertEqual(math_lib.div(-10, -5), 2)

        # test for division with zero
        self.assertEqual(math_lib.div(0, 5), 0)
        self.assertRaises(ZeroDivisionError, math_lib.div, 10, 0) # expecting exception for dividing by zero

        # test for division with 1 (neutral element)
        self.assertEqual(math_lib.div(10, 1), 10)

        # test for division with large nums
        self.assertEqual(math_lib.div(3297216, 34346), 96)

        # test for division with decimal nums
        self.assertEqual(math_lib.div(10.354, 5), 2.0708)

    def test_fact(self):
        ##
        #  @brief test_fact
        #  checks accuracy of math function for factorial
        #

        # test for special value of 0!
        self.assertEqual(math_lib.fact(0), 1)

        # test for basic values
        self.assertEqual(math_lib.fact(1), 1)
        self.assertEqual(math_lib.fact(2), 2)
        self.assertEqual(math_lib.fact(3), 6)
        self.assertEqual(math_lib.fact(4), 24)
        self.assertEqual(math_lib.fact(5), 120)

        # test for large values
        self.assertEqual(math_lib.fact(12), 479001600)
        self.assertEqual(math_lib.fact(20), 2432902008176640000)

        # test for unwanted params
        self.assertRaises(ValueError, math_lib.fact, -5) # expecting exception for factorial of negative number
        self.assertRaises(ValueError, math_lib.fact, 5.23) # expecting exception for factorial of decimal number

    def test_exp(self):
        ##
        #  @brief test_exp
        #  checks accuracy of math function for exponentiation with natural nums (x^n)
        #

        # test for special value for n=0
        self.assertEqual(math_lib.exp(1, 0), 1)
        self.assertEqual(math_lib.exp(5, 0), 1)

        # test for n=1
        self.assertEqual(math_lib.exp(1, 1), 1)
        self.assertEqual(math_lib.exp(2, 1), 2)
        self.assertEqual(math_lib.exp(5, 1), 5)

        # test for x=1
        self.assertEqual(math_lib.exp(1, 2), 1)
        self.assertEqual(math_lib.exp(1, 5), 1)

        # test for wide range of n
        self.assertEqual(math_lib.exp(5, 2), 25)
        self.assertEqual(math_lib.exp(5, 3), 125)
        self.assertEqual(math_lib.exp(4, 5), 1024)
        self.assertEqual(math_lib.exp(2, 6), 64)
        self.assertEqual(math_lib.exp(13, 2), 169)

        # test for negative x 
        self.assertEqual(math_lib.exp(-5, 2), 25)
        self.assertEqual(math_lib.exp(-5, 3), -125)

        # test for decimal x
        self.assertEqual(math_lib.exp(5.65, 2), 31.9225)

        # test for large values
        self.assertEqual(math_lib.exp(56, 6), 30840979456)

        # test for unwanted n param (not a natural number)
        self.assertRaises(ValueError, math_lib.exp, 5, 2.5)
        self.assertRaises(ValueError, math_lib.exp, 5, -2)
    
    def test_root(self):
        ##
        #  @brief test_root
        #  checks accuracy of math function for nth root (n-th root of x)
        #

        # test for x=1 || x=0
        self.assertEqual(math_lib.root(0, 2), 0)
        self.assertEqual(math_lib.root(0, 3), 0)
        self.assertEqual(math_lib.root(1, 2), 1)
        self.assertEqual(math_lib.root(1, 3), 1)

        # test for n=1
        self.assertEqual(math_lib.root(5, 1), 5)
        self.assertEqual(math_lib.root(125, 1), 125)

        # test for wide range of n
        self.assertEqual(math_lib.root(36, 2), 6)
        self.assertEqual(math_lib.root(125, 3), 5)
        self.assertEqual(math_lib.root(256, 4), 4)

        # test for negative x (when n is odd)
        self.assertEqual(math_lib.root(-125, 3), -5)
        self.assertEqual(math_lib.root(-3125, 5), -5)

        # test for decimal result
        self.assertAlmostEqual(math_lib.root(27, 2), 5.1961, places=4) # checks equality for first 4 decimal places
        self.assertAlmostEqual(math_lib.root(-69, 3), -4.1016, places=4) # checks equality for first 4 decimal places

        # test for decimal x
        self.assertAlmostEqual(math_lib.root(25.5, 2), 5.0498, places=4) # checks equality for first 4 decimal places
        self.assertAlmostEqual(math_lib.root(-66.6, 3), -4.0534, places=4) # checks equality for first 4 decimal places

        # test for large values
        self.assertEqual(math_lib.root(1048576, 2), 1024)
        self.assertEqual(math_lib.root(-19683, 3), -27)

        # test for unwanted n param (not a natural number)
        self.assertRaises(ValueError, math_lib.root, 25, 2.5)
        self.assertRaises(ValueError, math_lib.root, 27, -3)

        # test for negative x param when n is even
        self.assertRaises(ValueError, math_lib.root, -25, 2)

    def test_abs(self):
        ##
        #  @brief test_abs
        #  checks accuracy of math function for absolute value of a number
        #

        return

# starts unittest module right away
if __name__ == '__main__':
    unittest.main()