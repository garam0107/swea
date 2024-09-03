# 그리디
'''
1. 각 단계에서 최적해 찾기
2. 단계의 결과들을 합하는 방법 찾기
3. 2번 단계가 맞는지 증명(반례가 있는지 없는지 찾기)
'''


coin_list =[10,50,100,500]
money = 1730
cnt = 0
for i in range(len(coin_list)-1,-1,-1):
    now_cnt = money // coin_list[i]
    cnt += now_cnt
    money -= now_cnt*coin_list[i]

print(cnt)

