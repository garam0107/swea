import sys
sys.stdin = open('sample_input (6).txt','r')

T = int(input())

def home(): # 완전탐색이라 시간 복잡도 N**2
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(1,N+2):
                cnt = 0
                for si in range(i-(k-1), i+k):
                    for sj in range(j-(k-1)+abs(si-i), j+k-abs(si-i)):
                        if 0 <= si < N and 0 <= sj < N and array[si][sj]:
                            cnt += 1
                cost = k**2 + (k-1)**2
                if cost <= cnt*M and ans < cnt:
                    ans = cnt
    return ans






for tc in range(1,T+1):
    N,M = map(int,input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    answer = home()
    print(f'#{tc} {answer}')

