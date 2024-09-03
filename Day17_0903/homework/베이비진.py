def run():
    cnt_1 = 1
    cnt_2 = 1
    result = 0
    N = len(player_1)
    for i in range(N-1):
        if player_1[i]+1 == player_1[i+1]:
            cnt_1 += 1
            if cnt_1 == 3:
                result = 1
                break
        else:
            cnt_1 = 1
    for i in range(N-1):
        if player_2[i]+1 == player_2[i+1]:
            cnt_2 += 1
            if cnt_2 == 3:
                result = 2
                break
        else:
            cnt_2 = 1


    return result



def triplet():
    pass




T = int(input())
for tc in range(1,T+1):
    array = list(map(int,input().split()))
    player_1 = []
    player_2 = []
    for i in range(len(array)):
        if i % 2 == 0:
            player_1.append(array[i])
        else:
            player_2.append(array[i])