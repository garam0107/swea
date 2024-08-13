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
    # while array[sr][sc] != 3:
    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if array[nr][nc] != 1 and visited[nr][nc] == 0:  # 인덱스 안벗어나고 방문한 적이 없을 때
                stack.append([nr,nc])
                sr,sc = nr,nc
                visited[nr][nc] = 1
                if array[sr][sc] == 3:
                    return 1
        elif 0 <= nr < N and 0 <= nc < N:
            while visited[nr][nc] != 1:
                stack.pop()
                sr,sc = stack[0][0],stack[0][1]
                if array[nr][nc] != 1 and visited[nr][nc] == 0:
                    stack.append([nr,nc])
                    sr,sc =nr,nc
                    visited[nr][nc] = 1
                    if array[sr][sc] ==3:
                        return 1
                else:
                    stack.pop()
                    if not stack:
                        return 0







T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    print(maze(array,N))