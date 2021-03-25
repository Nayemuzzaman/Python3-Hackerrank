#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    lst = list(student_marks[query_name])
    lngth = len(lst)
    total_score = sum(lst)
    avarage = total_score /lngth
    print("%.2f"%avarage)
