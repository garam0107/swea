import sys
sys.stdin = open('input.txt', 'r')
def cal(left,right,play):
    if play == '-': return left - right
    elif play == '+': return left + right
    elif play == '*': return left * right
    else: return left /right
def postorder(node):
    pass
    if array[node][1] in calcul:
        left = postorder(array[node][2])
        right = postorder(array[node][3])
        return cal(left,right,array[node][1])
    else:
        return array[node][1]






T = 10
for tc in range(1,T+1):
    N = int(input())
    calcul = ['+','*','/','-']
    # for _ in range(N):
    #     array = list(input().split())
    #     for i in array:
    #         if i in calcul:
    array = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split()))for _ in range(N)]
    # 람다를 활용해서 숫자일때만 int로 변환
    array.insert(0,0)
    answer = postorder(1)
    print(int(answer))


