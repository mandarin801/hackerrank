#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def aVeryBigSum(ar):
    
    result = 0
    for i in range(len(ar)):
        result += ar[i]
        print(result)
    return result



if __name__ == '__main__':

    sss = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

    result = aVeryBigSum(sss)

    print(result)

