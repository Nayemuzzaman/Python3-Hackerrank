#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    capital_word = [w.capitalize() for w in words]
    return " ".join(capital_word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = sys.stdout
    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
