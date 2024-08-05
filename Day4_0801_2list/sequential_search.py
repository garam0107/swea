# 정렬되어 있지 않은 경우
def sequential_search(lst, n, key):
    i = 0
    while i < n and lst[i] != key:
        i += 1
        if i < n:
            return i
        else:
            return -1

# for i in range(n):
#     if lst[i] == key:
#         print(i)
#
# print(-1)