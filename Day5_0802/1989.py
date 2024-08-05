def myLen(lst):
    lstLen = 0
    for _ in range(lst):
        lstLen += 1
    return lstLen

T = int(input())
for tc in range(1, T+1):
    words = input()
    reverse = [0] * myLen(words)
    for i in range(myLen(words)):
        for idx in range(myLen(words), -1, -1):
            reverse[i] = words[idx]
    print(reverse)








