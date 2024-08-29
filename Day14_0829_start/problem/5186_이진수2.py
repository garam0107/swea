T = int(input())
for tc in range(1,T+1):
    arr = float(input())
    i = 1
    total = ''
    result = 'overflow'
    num = arr
    while i < 13:
        x = 2 ** -i
        if num > x:
            i += 1
            total += '1'
            num -= x
        elif num < x:
            i += 1
            total += '0'
        elif num == x:
            total += '1'
            result = total
            break
    print(f'#{tc} {result}')
