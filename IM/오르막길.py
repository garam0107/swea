
def road(array):
    road_list = []
    total_list = []
    road_list.append(array[0])
    for i in range(len(array)-1):
        if array[i] <= array[i+1]:
            road_list.append(array[i+1])
        else:
            total_list.append([(road_list[-1] - road_list[0]) / ])







array = list(map(int, input().split()))