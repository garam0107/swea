N = int(input())
list = [[0]*7 for _ in range(2)]
for i in range(4):
    list[0][i] = N + i
    list[1][-(i+1)] = N - i
print(list)
