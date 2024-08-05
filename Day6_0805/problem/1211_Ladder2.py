def Ladder(array):
    N = 100
    row = 0
    col = 0
    dr = [0,0,1]
    dc = [-1,1,0]
    counts = 0
    min_value = 100
    while row < 100:
        for idx in range(N):
            if array[0][idx] == 0: continue
            if array[0][idx] == 1:
                col = idx
                array[row][col] += 1
                row += 1
                counts += 1
            for k in range(3):
                nr = row + dr[k]
                nc = col + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if array[nr][nc] == 1:
                        counts += 1
                        row = nr
                        col = nc

        if min_value > counts:
            min_value = counts
    return counts

array = [list(map(int, input().split()))]

answer = Ladder(array)

print(answer)