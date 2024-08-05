def kmp(t,p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)

    j = 0 # 일치한 개수 == 비교할 패턴 위치
    lps[0] = -1

    for i in range(1,M):
        lps[i] = j
        if p[i] == p[j]:
            j+= 1
        else:
            j = 0
    lps[M] = j
    print(lps)
    i = 0
    j = 0
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == M:
            print(i-M, end=' ')
            j = lps[j]
    print()
    return

t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t,p)
