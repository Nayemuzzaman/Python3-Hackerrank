#https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
   value = "-".join(line.split())
   return value

if __name__ == '__main__':
   line = input()
   result = split_and_join(line)
   print(result)