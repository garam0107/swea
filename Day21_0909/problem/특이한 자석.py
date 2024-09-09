'''
N극 : 0, S극: 1
시계 방향: 1, 반시계 방향: -1
'''
import sys
sys.stdin = open('sample_input (7).txt','r')
def rotation(n,dir):
    if n ==4:
        if dir == 1:
            if marg[2][2] == marg[3][6]:
                change = marg[3].pop(-1)
                marg[3].insert(0,change)
            else:
                if marg[2][6] == marg[1][2]:
                    change = marg[3].pop(-1)
                    marg[3].insert(0, change)
                    c = marg[2].pop(0)
                    marg[2].insert(-1,c)
                else:
                    if marg[1][6] == marg[0][2]:
                        change = marg[3].pop(-1)
                        marg[3].insert(0, change)
                        c = marg[2].pop(0)
                        marg[2].insert(-1, c)
                        c_2 =



        else:
    else:






T = int(input())
for tc in range(1,T+1):
    K = int(input())
    marg = [list(map(int, input().split())) for _ in range(4)]
    dir = [list(map(int, input().split())) for _ in range(K)]
    for x,y in dir:
        rotation(x,y)


