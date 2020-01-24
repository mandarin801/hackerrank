#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    result = 0
    left_diagonal = []
    right_diagonal = []

    for i in arr:
        for j in arr[i]:
            if i == j:
                left_diagonal.append(arr[i][j])
    
    return result

if __name__ == '__main__':

    a = [11, 2, 4]
    b = [4, 5, 6]
    c = [10, 8, -12]

    arr = []

    arr.append(a)
    arr.append(b)
    arr.append(c)

    result = diagonalDifference(arr)

    print(result)
