#https://www.hackerrank.com/challenges/python-time-delta/problem

#!/bin/python3

import math
from datetime import datetime
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    one=datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    two=datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return (int(abs((one-two).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
