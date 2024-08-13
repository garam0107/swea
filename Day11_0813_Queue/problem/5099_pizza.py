def pizza(array, N):
    Q = [0] * N
    for i in range(N):
        Q[i] = array.pop(i)
    while True:
        Q = [c // 2 for c in Q]
        for i in range(N):
            if Q[i] == 0:
                Q.pop(i)
                if array:
                    Q.append(array[0])
            if len(Q) == 1:
                break
        return Q[0]



T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    C = list(map(int, input().split()))
    print(pizza(C,N))

