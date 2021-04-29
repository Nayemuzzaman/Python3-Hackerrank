#https://www.hackerrank.com/challenges/exceptions/problem

a = int(input())

for i in range(a):
    try:
        num1, num2 = map(int, input().split())
        result = num1 // num2
        print(result)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as v:
        print(f"Error Code: {v}")

