# def omok(array, N):
#     omok_list = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if array[i][j] == 'o':
#                 omok_list[i][j] = 1
#     return omok_list

def five(arr, N):
    # arr = omok(array,N)
    if N == 5:
        for i in range(N):
            counts = 0
            for j in range(N):
                if arr[i][j] == 'o': counts += 1
                if counts == 5: return 'YES'
        for i in range(N):
            counts = 0
            for j in range(N):
                if arr[j][i] == 'o' : counts += 1
                if counts == 5 : return 'YES'
        counts = 0
        for i in range(N):
            if arr[i][i] == 'o': counts += 1
            if counts == 5 : return 'YES'
        counts = 0
        for i in range(N):
                if arr[i][N-1-i] == 'o': counts += 1
                if counts == 5 : return 'YES'
        return 'NO'

    elif N > 5:
        for i in range(N):
            counts = 0
            for j in range(N):
                if arr[i][j] == 'o': counts += 1
                if counts == 5: return 'YES'
        for i in range(N):
            counts = 0
            for j in range(N):
                if arr[j][i] == 'o' : counts += 1
                if counts == 5 : return 'YES'
        counts = 0
        for i in range(N):
            if arr[i][i] == 'o': counts += 1
            if counts == 5 : return 'YES'
        for i in range(1,N-4):
            counts = 0
            for j in range(N):
                if arr[i][j] == 'o': counts += 1
                if counts == 5 : return 'YES'
        for i in range(1, N-4):
            counts = 0
            for j in range(1, N - 4):
                if arr[i][j + i] == 'o': counts += 1
                if counts == 5: return 'YES'
        counts = 0
        for i in range(N):
                if arr[i][N-1-i] == 'o': counts += 1
                if counts == 5 : return 'YES'
        for i in range(1, N-4):
            counts = 0
            for j in range(N-1,i-1,-1):
                if arr[i][j] == 'o' : counts += 1
                if counts == 5 : return 'YES'
        return 'NO'


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = [list(input()) for _ in range(N)]
    answer = five(array,N)
    print(f'#{tc} {answer}')


