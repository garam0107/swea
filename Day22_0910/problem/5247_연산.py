def bfs(level,N):
    if N == num_2:
        print(N)
        return N

    for i in range(4):
        if visit[i]: continue

        if i == 0:
            visit[i] = 1
            N += 1
            bfs(level+1,N)
            visit[i] = 0
        elif i == 1:
            visit[i] = 1
            N -= 1
            bfs(level+1,N)
            visit[i] = 0
        elif i == 2:
            visit[i] = 1
            N *= 2
            bfs(level+1,N)
            visit[i] = 0
        else:
            visit[i] = 1
            N -= 10
            bfs(level + 1, N)
            visit[i] = 0





T = int(input())
for tc in range(1,T+1):
    num_1,num_2 = map(int, input().split())
    visit = [0] * 4
    answer = bfs(0,num_1)
    print(answer)

