Data = [0,4,1,3,1,2,4,1]


COUNTS = [0] * 5
N = len(Data)
TEMP = [0] * N
# for i in range(0, N):
#     counts[Data[i]] += 1
# 1단계 : Data 원소 별 개수 세기
for x in Data:    # DATA의 원소 x를 가져와서 COUNTS[x]에 개수 기록
    COUNTS[x] += 1
# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1,5):     #COUNTS[1] ~COUNTS[4]까지 누적 개수
    COUNTS[i] += COUNTS[i-1]
# 3단계 Data의 맨 뒤부터 TEMP에 자리 잡기
for i in range(N-1, -1, -1):   #
    COUNTS[Data[i]] -= 1
    TEMP[COUNTS[Data[i]]] = Data[i]

print(TEMP)