#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students = [name, score]
        lst.append(students)
value = sorted(set([score for name, score in lst]))[1]
print("\n".join(sorted(name for name,score in lst if score == value)))
