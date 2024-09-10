def bfs(num,cnt):
    if num == M:
        return cnt
    cnt += 1
    for i in range(4):
        if visit[i]: continue
        visit[i] = 1
        if i == 0:
            if 0 < num+1 <= 10 ** 6:
                num += 1
                bfs(num,cnt)
                visit[i] = 0

        if i == 1:
            if 0 < num - 1 <= 10 ** 6:
                num -= 1
                bfs(num,cnt)
                visit[i] = 0

        if i == 2:
            if 0 < num * 2 <= 10 ** 6:
                num *= 2
                bfs(num,cnt)
                visit[i] = 0

        if i == 3:
            if 0 < num - 10 <= 10 ** 6:
                num -= 1
                bfs(num,cnt)
                visit[i] = 0


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    answer = bfs(N,0)
    print(answer)