# 전위 순회(본인 -> 왼쪾 -> 오른쪽)



def preorder(node):
    if node == 0:
        return
    print(node, end=' ')
    preorder(left[node])
    preorder(right[node])
# 중위 순회(왼 -> 본인 -> 오른쪽)
def midorder(node):
    if node == 0:
        return
    midorder(left[node])
    print(node, end=' ')
    midorder(right[node])

# 후위 순회
def order(node):
    if node == 0:
        return
    order(left[node])
    order(right[node])
    print(node, end=' ')



N = int(input())
# 입력이 반드시 각 노드당 최대 2번 씩만 들어온다고 가정한 코드
array = list(map(int, input().split()))
left = [0] * (N+1)
# ex) left[3] = 2이면 3번 부모의 왼쪽 자식은 2임을 나타낼 수 있음
right = [0] * (N+1)

for i in range(0,len(array),2):
    parent,child = array[i],array[i+1]
    if left[parent] == 0:
        left[parent] = child
    elif right[parent] == 0:
        right[parent] = child
root = 1 # 시작점 1
preorder(root)
print()
midorder(root)
print()
order(root)