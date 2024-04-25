'''This utility class is used to generate random data for testing purposes.'''
import numpy as np


'''This function generats a random array of integers of random size between user specified min and max size.'''

def generateRandomArray(minSize, maxSize, minValue, maxValue):
    size = np.random.randint(minSize, maxSize)
    return np.random.randint(minValue, maxValue, size)