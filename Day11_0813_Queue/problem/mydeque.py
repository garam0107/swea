from collections import deque

q = deque()
q.append(1)

t = q.popleft()

print(q)