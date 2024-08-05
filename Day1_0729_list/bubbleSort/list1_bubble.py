N = 5
arr = [55, 7, 78, 12, 42]

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(*arr)

# import sys
# sys.strdin = open('txt명') # 같은 폴더에 있으면 txt명 아니면 경로를 다 적어줘야함