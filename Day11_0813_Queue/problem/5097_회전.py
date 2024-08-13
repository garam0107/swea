def rotation(array,M):
    for _ in range(M):
        array.append(array.pop(0))
    return array[0]


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    array = list(input().split())
    answer = rotation(array,M)
    print(f'#{tc} {answer}')


def rotation(array,N,M):
    Q = [0] * N
    front = -1
    rear = -1


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    array = list(input().split())
    answer = rotation(array,N,M)
    print(f'#{tc} {answer}')
