def match(array):
    stack = []
    search_dict = {')':'(', '}':'{'}
    for c in array:
        if c == search_dict.values():
            stack.append(c)
        elif c == search_dict.keys():
            if not stack or stack[-1] != search_dict[c]:
                return False
            stack.pop()

    return not stack


T = int(input())
for tc in range(1,T+1):
    array = input()
    if match(array):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')