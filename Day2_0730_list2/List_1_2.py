T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr1,arr2 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    P = int(input())

bus1 = []
bus2 = []

for x in range(arr1[0], arr1[-1]+1):
    bus1.append(x)
for y in range(arr2[0], arr2[-1]+1):
    bus2.append(y)
count = []
for _ in range(P):
    num = int(input())
    if num in bus1 and num in bus2:
        count.append(2)
    elif num in bus1 or bus2:
        count.append(1)
    else:
        count.append(0)
print(f'#{tc} {" ".join(list(map(str,count)))}')

