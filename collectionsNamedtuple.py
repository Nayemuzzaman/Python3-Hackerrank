#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

import collections

s_num = int(input("students number: "))


my_sub = ','.join(input().split())
student = collections.namedtuple('student', my_sub)

sum_marks = 0

for i in range(0, s_num):
    row = input().split()
    students = student(*row)
    sum_marks+=int(students.MARKS)


print("{:.2f}".format(sum_marks/s_num))