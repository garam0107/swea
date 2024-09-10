from collections import deque


def bfs(node):
    q = deque([node])
    while q:
        now = q.popleft()
        print(now, end=' ')




# deque의 popleft()와 리스트의 pop(0)의 시간 복잡도를 비교하면 O(1)과 O(N)