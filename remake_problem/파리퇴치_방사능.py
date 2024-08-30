'''
N = 행과 열의 길이
M = 파리채의 행과 열의 길이
arr1 = NXN 배열
arr2 = 방사능 걸린 파리의 행과 열 인덱스 리스트
'''
def bug_remove(N,M,arr1,arr2):
    dr = [-1,1,1,-1]
    dc = [1,1,-1,-1]
    max_v = 0
    max_idx = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            idx_list= []
            for r in range(M):
                for c in range(M):
                    sum += arr1[i+r][j+c]
                    idx_list.append((i+r,j+c))
                if sum > max_v:
                    max_v = sum
    return max_v,max_idx






T = int(input())
for tc in range(1,T+1):
    N,M,B = map(int,input().split())
    B_list =[]
    for _ in range(B):
        r,c = map(int,input().split())
        B_list.append((r,c))
    array = [list(map(int,input().split())) for _ in range(N)]
    answer = bug_remove(N,M,array,B_list)
    print(answer)