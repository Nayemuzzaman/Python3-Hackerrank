from collections import deque

print("-------Queue----------")
# FIFO principle

q = deque()

q.append('1st element')
q.append('2nd Element')
q.append('3rd Elements')

print(q, '\n')

a = q.popleft()
print("The first popped elements is: ", a)
b = q.popleft()
print('The second popped elements is:', b)
c = q.popleft()
print('The third popped element is: ', c)



