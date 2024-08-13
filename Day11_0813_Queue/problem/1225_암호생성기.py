def password(arr,N):
    while True:
        for num in range(1,6):
            result = arr[0] - num
            for i in range(N-1):
                arr[i] = arr[i+1]
            arr[N-1] = result
            if arr[N-1] <= 0:
                arr[N-1] = 0
                return arr





T = 10
for _ in range(1,T+1):
    N = 8
    tc = int(input())
    array = list(map(int, input().split()))
    answer = ' '.join(map(str, password(array,N)))
    print(f'#{tc} {answer}')