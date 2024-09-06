def ten():
    ten = []
    for i in range(len(num_list)):
        ten.append(int((num_list[i]),16))
    return ten

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    array = list(map(str, input()))
    x = N // 4
    a = []
    password = set()

    for i in range(0,N,x):
        a.append(tuple(array[i:i+x]))
    for idx in range(len(a)):
        password.add(a[idx])

    for _ in range(x):
        y = array.pop(-1)
        array.insert(0,y)
        b = []
        for i in range(0, N, x):
            b.append(tuple(array[i:i + x]))
        for idx in range(len(b)):
            password.add(b[idx])
    final = []
    for i in password:
        final.append(i)

    num_list = []
    for i in range(len(final)):
        txt = ''
        for j in range(x):
            txt += final[i][j]
        num_list.append(txt)
    answer = ten()
    answer.sort(reverse=True)
    print(f'#{tc} {answer[K-1]}')


