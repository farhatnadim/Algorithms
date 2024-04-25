''' this program implements the pseudocode for recursive integer multiplication @page 9 of the book Algorithm Illuminated Part 1: The Basics'''
''' Check Karatsuba.pdf for the discussion of the Algorithm''' 
''' it works for numbers of the same size and the size can be arbitrary'''
''' itoverflows for numbers of size 10**9 and above'''
''' but if you a number of size 10**9 and it is power of 2 you can skip the padding and it will work'''
from numpy import random
import numpy as np
import unittest
import time 
import sys



# get number of digits in a number using log10
def getNumDigits(number):
    '''get number of digits in a number using log10'''
    '''Helper function for generalizing Karatsuba algorithm to numbers of arbitrary size'''
    ''''returns the number of digits in a number'''
    number = np.double(number)
    if number == 0:
        return 1
    if np.floor(np.log10(number)) == 0:
        return 1 
    if number < 0:
        number = -number
    return  int(np.floor(np.log10(abs(number)))) + 1
# get number of 2 multiples in a number using log2
def getNum2Multiples(number):

    return int(np.floor(np.log2(abs(number)))) + 1

def getPaddingsize(number):
    '''Pad a number with zeros to make it a power of 2'''
    '''Helper function for generalizing Karatsuba algorithm to numbers of arbitrary size'''
    ''' Takes a number and returns the number of zeros needed to add to the left to make the number of digits a power of 2'''

    num_digits = getNumDigits(number)
    if num_digits == 1:
        return 0
    num_zeros = 2**getNum2Multiples(num_digits) - num_digits
    return num_zeros

def padNumber(number,pading_size):
    '''Left Pad a number with zeros its number of digits power of 2'''
    '''Helper function for generalizing Karatsuba algorithm to numbers of arbitrary size'''
    '''Input number to be padded, number of zeros to be padded'''
    '''Output padded number'''
    padding = number * 10**int( pading_size)
    return padding

def unpadNumber(number,pading_size):
    '''removed padded zeros from a number'''
    '''Helper function for generalizing Karatsuba algorithm to numbers of arbitrary size'''
    '''After the multiplication we need to remove the padded zeros'''
    '''Input number to be unpadded, number of zeros to be unpadded'''
    '''Output unpadded number'''

    return number // 10**int( pading_size)

# write a unit test to check if the padding and unpadding works
def recursiveIntegerMultiplication(number1, number2,n1,n2):
    '''Assumption: number1 and number2 are of the same size and their sizes is a power of 2'''
    '''input: number1, number2, number of digits in number1, number of digits in number2'''
    '''output: multiplication of number1 and number2'''
    '''This function implements the pseudocode for recursive integer multiplication @page 9 of the book Algorithm Illuminated Part 1: The Basics'''
    # Base case
    if n1== 1:
        return number1 * number2
    # Recursive case
    else:
        a = number1 // 10**(n1//2)
        b = number1 % 10**(n1//2)
        c = number2 // 10**(n2//2) 
        d = number2 % 10**(n2//2) 
        n3 = n1//2
        n4 = n2//2  
        ac = recursiveIntegerMultiplication(a,c,n3,n4)
        bd = recursiveIntegerMultiplication(b,d,n3,n4)
        ad = recursiveIntegerMultiplication(a,d,n3,n4)
        bc = recursiveIntegerMultiplication(b,c,n3,n4)
        return 10**(n1)*ac + 10**(n3)*(ad+bc) + bd

def karatsubaMultiplication(number1, number2,n1,n2):
    
    '''Assumption: number1 and number2 are of the same size and there size is a power of 2'''
    '''input: number1, number2, number of digits in number1, number of digits in number2'''
    '''output: multiplication of number1 and number2'''
    '''This function implements the pseudocode for recursive integer multiplication @page 9 of the book Algorithm Illuminated Part 1: The Basics'''
    # Base case
    if n1== 1:
        return number1 * number2
    # Recursive case
    else:
        a = number1 // 10**(n1//2)
        b = number1 % 10**(n1//2) 
        c = number2 // 10**(n2//2) 
        d = number2 % 10**(n2//2) 
        p = a+b
        q = c+d
        n3 = n1//2
        n4 = n2//2  
        ac = karatsubaMultiplication(a,c,n3,n4)
        bd = karatsubaMultiplication(b,d,n3,n4)
        pq = karatsubaMultiplication(p,q,n3,n4)

        adbc = pq - ac - bd
        return 10**(n1)*ac + 10**(n3)*(adbc) + bd

