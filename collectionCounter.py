#https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

def totalMoney(x):
    earning = 0
    shoe_size = Counter(map(int, input().split()))
    n = int(input())
    for i in range(n):
        size, x_i = map(int, input().split())
        if size in shoe_size and shoe_size[size] > 0:
            shoe_size[size]-=1
            earning+=x_i
    print(earning)
if __name__ == '__main__':
    x = int(input())
    totalMoney(x)


