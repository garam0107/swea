'''
0x4A3
25
'''

# print(bin(0x4A3 | 25))
# print(hex(0x4A3 | 25))
#
# print(0b1011 ^ 0b1101)
#
# a = 7070 ^ 1004
# print(a ^ 1004)
#
# print()


# print(1)
# print(1 << 1)
# print(1 << 4)
# print(bin(1 << 2))
#
# print(1 >> 2)
# print(7 >> 2 )

# i & (1 << N) - > N번째 비트가 0인지 아닌지 알 수 있다.
arr = [1,2,3,4]
# i의 의미는 i번째 부분집합
for i in range(1 << len(arr)): #2 ** len(arr)
    for idx in range(len(arr)):
        if i & (1 << idx):
        # - i번째 부분집합에 idx요소가 포함되어 있는지 아닌지지        if i & (1 << idx):
            print(arr[idx], end = ' ')


