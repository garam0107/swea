#prim
import heapq
def prim(start):
    q = []
    visit = [0] * (V+1)
    result = 0
    heapq.heappush(q, (0, start))
    while q:
        weight, now = heapq.heappop(q)
        if visit[now] == 0:
            visit[now] = 1
            result += weight
            for i in range(V+1):
                if graph[now][i] and visit[i] == 0:
                    heapq.heappush(q,(graph[now][i],i))
    return result
T = int(input())
for tc in range(1,T+1):
    V,E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        n1,n2,w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w

    answer = prim(0)
    print(f'#{tc} {answer}')

# kruskal



