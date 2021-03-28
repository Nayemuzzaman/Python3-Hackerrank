#https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())

    arr = []
    for i in range(0,N):
       command_input = input().split();
       if command_input[0] == "insert":
           arr.insert(int(command_input[1]), int(command_input[2]))
       elif command_input[0] == "append":
           arr.append(int(command_input[1]))
       elif command_input[0] == "remove":
           arr.remove(int(command_input[1]))
       elif command_input[0] == "sort":
           arr.sort()
       elif command_input[0] == "pop":
           arr.pop()
       elif command_input[0] == "reverse":
           arr.reverse()
       elif command_input[0] == "print":
           print(arr)
