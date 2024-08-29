T = int(input())
for tc in range(1,T+1):
    N = int(input())
    three = int(N ** (1/3))
    result = -1
    if three ** 3 == N:
        result = three
    elif (three+1) ** 3 == N:
        result = three + 1
    print(f'#{tc} {result}')
# 시간 복잡도 O(1)



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = -1
    for i in range(1,1000001):
        if N == i**3:
            result = i
            break
    print(f'#{tc} {result}')
# 시간 복잡도 몇?


