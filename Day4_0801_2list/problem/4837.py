


T = int(input())
for tc in range(1,T+1):
    N,K = map(int, input().split())
    arr = list(range(1,N+1))
    subset_cnt = 2 ** N

    subsets = []
    for i in range(subset_cnt):
        subset = []
        for j in range(len(arr)):
            if i &(1<<j):
                subset.append(arr[j])
        subsets.append(subset)
    counts = 0
    for idx in range(subset_cnt):
        if sum(subsets[idx]) == K and len(subsets[idx]) == N:
            counts += 1
    print(f'#{tc} {counts}')


