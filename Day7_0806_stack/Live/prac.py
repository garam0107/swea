# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-2)+fibo(n-1)
#
#
#
# print(fibo(10))
#
#
# def f(n):
#     global cnt
#     cnt += 1
#     if n == 0:
#         return 1
#     else:
#         f(n-1)
#
# cnt = 0
# f(1250)
# print(cnt)

arr = [1,2,3]
text = []

for i in range(len(arr)-1, -1, -1):
    text.append(arr[i])

print(text)

def f(i,N): # i: 현재 인덱스 ,N: 크기
    if i==N:
        return
    else:
        print(arr[i])
        f(i+1, N)
        return


arr = [1,2,3]
N = 3
f(1,3)




