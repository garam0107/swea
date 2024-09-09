'''
1 <= N <= 4
2 <= W <= 12
2 <= H <= 15
'''
import sys
import copy
sys.stdin = open('sample_input (4).txt','r')
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def brick():

T = int(input())
for tc in range(1,T+1):
    N,W,H = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(H)]

