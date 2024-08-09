N = int(input())
num_list = [i for i in range(N)]
visited = [0] * len(num_list)
perm = []
r = N
array = [list(map(int, input().split()))]
def permutaion(depth):
    min_v = 9*N
    if depth == r:
        for i in perm:
            array[][i]


    for i in range(len(num_list)):
        if visited[i] == 0:
            visited[i] = 1
            perm.append(num_list[i])
            permutaion(depth+1)
            perm.pop()
            visited[i] = 0

permutaion(0)

