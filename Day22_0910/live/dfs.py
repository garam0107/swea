# dfs 재귀 호출

'''
시작점 1번 - 끝점 (1번에서 갈 수 있는 모든 정점) 방문시 종료
visited 처리 덕분에 기저조건이 없어도 종료
'''
def dfs(node):
    print(node, end=' ')  # 현재 노드 출력

    # 갈 수 있는 노드들을 탐색
    #  for next_node in graph[node][::-1]: 숫자가 큰 노드부터 탐색
    for next_node in graph[node]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
# graph = [[0] * (N+1) for _ in range(N+1)] # 인접행렬 예시
visited = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
# 작은 수 우선 탐색
visited[1] = 1
dfs(1)



# 7 8
# 1 2
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7