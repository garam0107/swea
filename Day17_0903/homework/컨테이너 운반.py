def container(arr1,arr2):
    sum = 0
    idx = 0
    for i in range(N):
        for j in range(M-idx):
            if arr1[i] <= arr2[j]:
                sum += arr1[i]
                arr2.pop(j)
                idx += 1
                break
    return sum






T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    weight = list(map(int,input().split()))
    truck_max = list(map(int,input().split()))
    weight.sort(reverse=True)
    truck_max.sort(reverse=True)
    answer = container(weight,truck_max)
    print(f'#{tc} {answer}')