# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     array = [[0] * 10 for _ in range(10)]
#     for _ in range(N):
#         r1, c1, r2, c2, color = list(map(int, input().split()))
#
#         for i in range(r1,r2+1):
#             for j in range(c1,c2+1):
#                 array[i][j] += color
#     purple = 0
#     for idx in range(10):
#         purple += array[idx].count(3)
#     print(f'#{tc} {purple}')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))

        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                array[i][j] += color
    purple = 0
    for idx in range(10):
        purple += array[idx].count(3)
    print(f'#{tc} {purple}')





















# arr2 = [[0] * 3 for _ in range(2)]
# print(arr2)
# print(arr1)
# print(*arr1)
#
# for i in range(2):
#     print(*arr2[i])
# print()
# for i in range(2):
#     for j in range(3):
#         print(arr2[i][j], end=' ')
#     print()

