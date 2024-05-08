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

# write a unit test to check if the padding and unpadding works
def recursiveIntegerMultiplication(number1, number2,n1,n2):
    '''Assumption: number1 and number2 are of the same size and their sizes is a power of 2'''
    '''input: number1, number2, number of digits in number1, number of digits in number2'''
    '''output: multiplication of number1 and number2'''
    '''This function implements the pseudocode for recursive integer multiplication @page 9 of the book Algorithm Illuminated Part 1: The Basics'''
    # Base case
    if n1 == 1 and n2 == 1:
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

def main():
    assert ( 5678*1234) == recursiveIntegerMultiplication(5678,1234,4,4)
    
if __name__ =="__main__":
    main()