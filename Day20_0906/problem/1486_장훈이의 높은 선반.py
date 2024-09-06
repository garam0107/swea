import sys
sys.stdin = open('input (2).txt','r')

def subset():
    pass


T = int(input())
for tc in range(1,T+1):
    N,height = map(int, input().split())
    array = list(map(int, input().split()))
