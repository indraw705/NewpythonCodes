#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER_ARRAY apples
#  4. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    modarr1 = list(map(lambda x: x + a, apples))
    modarr2 = list(map(lambda x: x + b, oranges))
    finalCount1 = list(filter(lambda x: (x >= s and x <= t), modarr1))
    finalCount2 = list(filter(lambda x: (x >= s and x <= t), modarr2))

    print("Apples : "+str(len(finalCount1)))
    print("oranges : "+str(len(finalCount2)))


if __name__ == '__main__':
    countApplesAndOranges(7, 11, 5, 15, [1,4,2,6], [8, 0 , -2,-8])
