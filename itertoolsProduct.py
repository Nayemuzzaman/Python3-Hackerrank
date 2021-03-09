# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

def cartesian_product(num, num2):
    val = (product(num, num2))
    print(*product(num, num2))
if __name__ == '__main__':
    num = map(int, input().split())
    num2 = map(int, input().split())
    cartesian_product(num, num2)