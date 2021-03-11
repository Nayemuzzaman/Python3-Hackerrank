#https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

s,num = input().split(" ")
permu = list(permutations(s, int(num)))
permu.sort()

for i in permu:
    print("".join(i))