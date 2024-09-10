def bfs(level,N):
    if level == 4:
        return
    if N == num_2:
        print(N)
        return N

    for i in range(4):
        if visit[i]: continue
        visit[i] = 1
        if i == 0:
            N += 1
        elif i == 1:
            N -= 1
        elif i == 2:
            N *= 2
        else:
            N -= 10
        visit[i] = 0
        bfs(level + 1, N)





T = int(input())
for tc in range(1,T+1):
    num_1,num_2 = map(int, input().split())
    visit = [0] * 4
    answer = bfs(0,num_1)
    print(answer)

