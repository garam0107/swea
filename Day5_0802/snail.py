T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    count = 0
    row = 0
    col = 0
    for _ in range(N^2):
        count += 1
        for i in range(N):
            for j in range(N):
                arr[i][j] = count
                for _ in range(N-1):
                    for k in range(4):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 0:
                                arr





