#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    i = 0
    n = int(input())
    arr = map(int, input().split())
    value=sorted(list(set(arr)), reverse=True)
    print(value[1])
