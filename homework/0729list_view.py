N = int(input())
arr = list(map(int, input().split()))


# mid = arr[2]
# A = []
# for i in range(3,N-1):
#     if arr[i] < mid and arr[i+1] < mid:
#         mid = arr[2]
#     if arr[i] < arr[i+1]:
#         A.append(int(mid - arr[i+1]))
#     else:
#         A.append(int(mid - arr[i]))
# print(A)
#
#     if arr[n-2] < arr[n] and arr[n-1] < arr[n]:
#         mid = arr[n]
#     arr[]

x = arr[2]
A = []

for i in range(3, N-1):
    if x > arr[i] and x > arr[i+1]:
        x = arr[2]
    if arr[i] > arr[i+1]:
        A.append(x - arr[i])
    else:
        A.append(x -arr[i+1])


A = []
for i in range(N):
    if arr[i] > arr[i+1]:


