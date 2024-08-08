def start(N):
    for i in range(N):
        for j in range(N):
            if array[i][j] == 2:
                return i,j




def maze(array,N):
    sr,sc =start(N)
    stack = []
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    visited[sr][sc] = 1
    stack.append([sr,sc])
    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if array[nr][nc] != 1 and visited[nr][nc] == 0:
                stack.append([nr,nc])
                sr,sc = nr,nc
        else:
            sr,sc = stack.pop()

    return stack



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    print(maze(array,N))