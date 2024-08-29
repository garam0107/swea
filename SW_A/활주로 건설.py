def build(N,arr,l):
    result = 0
    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1] + 1:
                counts = 1
                visit[i][j+1] = arr[i][j+1]
                for idx in range(1,l):
                    if (j+1+idx) < N and arr[i][j+1+idx] == arr[i][j+1]:
                        visit[i][j+1+idx] = arr[i][j+1]
                        counts += 1
                    if counts == l:
                        break
    for i in range(N):
        for j in range(N-1,0,-1):
            if arr[i][j] == arr[i][j-1] + 1 and visit[i][j-1] != 0:
                continue
            else:
                counts = 1
                visit[i][j-1] = arr[i][j-1]
                for idx in range(1,l):
                    if (j + 1 - idx) > -1 and arr[i][j + 1 - idx] == arr[i][j - 1]:
                        visit[i][j + 1 - idx] = arr[i][j - 1]
                        counts += 1
                    if counts == l:
                        result += 1
                        break

    return result



T = int(input())
for tc in range(1,T+1):
    N,length = map(int,input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    print(build(N,array,length))
    print(visit)

