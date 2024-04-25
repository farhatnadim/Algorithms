''''''

import numpy as np
import unittest


# get number of digits in a number using log10
def getNumDigits(number):
    if number == 0:
        return 1
    if np.floor(np.log10(number)) == 0:
        return 1 
    if number < 0:
        number = -number
    return np.floor(np.log10(number)) + 1
# get number of 2 multiples in a number using log2
def getNum2Multiples(number):

    return np.floor(np.log2(number)) + 1

def getPaddingsize(number):
    '''Pad a number with zeros to make it a power of 2'''
    num_digits = getNumDigits(number)
    if num_digits == 1:
        return 0
    num_zeros = 2**getNum2Multiples(num_digits) - num_digits
    print("num_zeros",num_zeros)
    return num_zeros

def padNumber(number,pading_size):
    '''Pad a number with zeros to make it a power of 2'''
    padding = number * 10**int( pading_size)
    return padding
def unpadNumber(number,pading_size):
    '''removed padded zeros from a number'''
    return number // 10**int( pading_size)

# write a unit test to check if the padding and unpadding works

class TestPadUnpad(unittest.TestCase):

    def test_pad_unpad(self):

    # generate 10000 random numbers using numpy
        number_of_tests = 10000
        print(f"Generating {number_of_tests} tests \n")
        for i in range(number_of_tests):
            # Generate a random number betwee 1 and 10**9
            number = np.random.randint(1, 10**9)
            pading_size = getPaddingsize(number)
            padded_number = padNumber(number,pading_size)
            unpadded_number = unpadNumber(padded_number,pading_size)
            print(f"number = {number}, padded_number = {padded_number}, unpadded_number = {unpadded_number}")
            assert number == unpadded_number

# run the unit test
if __name__ == '__main__':
    unittest.main()

