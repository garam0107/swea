def truck(arr):
    cnt = 1
    N = len(arr)
    end = arr[0][1]
    for i in range(N):
        if end <= arr[i][0]:
            end = arr[i][1]
            cnt += 1

    return cnt


T= int(input())
for tc in range(1,T+1):
    N = int(input())
    time = [list(map(int,input().split())) for _ in range(N)]
    time.sort(key=lambda x: (x[1],x[0]))
    answer = truck(time)
    print(f'#{tc} {answer}')

