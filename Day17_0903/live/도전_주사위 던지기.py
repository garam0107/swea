arr = [1,2,3,4,5,6]
N = len(arr)
temp =[]
def com(lev,s):
    if lev == 3:
        print(temp)
        return
    for i in range(s,N):
        temp.append(arr[i])
        com(lev+1,i)
        temp.pop()
com(0,0)