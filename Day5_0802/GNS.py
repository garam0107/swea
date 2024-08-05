import sys
sys.stdin = open('GNS_test_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    counts = [0] * 10
    num = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    for n in range(10):
        for i in arr:
            if num[n] == i:
                counts[n] += 1
    print(f'#{tc}')
    for idx in range(10):
        print(num[idx]*counts[idx])

