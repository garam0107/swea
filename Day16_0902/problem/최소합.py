def min_sum(arr,N):
    dr = [0,1]
    dc = [1,0]
    queue = []
    r,c = 0,0
    queue.append((r,c))
    sum = arr[r][c]
    while queue:
        for add in range(2):
            nr = r + dr[add]
            nc = c + dc[add]





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
