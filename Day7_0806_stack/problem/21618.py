def same(array):
    counts = 0
    for i in range(len(array) - counts):
        counts += 1
        if array[i] == array[i + 1]:
            array.pop(i)
            array.pop(i)
            same(array)
            break
    return array

#
# T = int(input())
# for tc in range(1,T+1):
#     array = list(input())
#     stack = []
#     for idx in range(len(array)):



# array = list(input())
# counts = 0
# for i in range(len(array)-counts):
#     counts += 1
#     if array[i] == array[i+1]:
#         array.pop(i)
#         array.pop(i)
#         break
#
# print(array)
array = list(input())

print(same(array))