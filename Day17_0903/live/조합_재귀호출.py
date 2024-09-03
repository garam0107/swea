arr = ['A','B','C','D','E']
n = len(arr)
temp =[]
'''
level = 3
Branch = len(arr)
'''
def com(level,start):
    if level == 3:
        print(temp)
        return
    for i in range(start,n):
        temp.append(arr[i])
        com(level+1,i+1) # 다음거 부터 고려하기 위해 스타트 지점에 1을 더해줌
        temp.pop()

com(0,0)