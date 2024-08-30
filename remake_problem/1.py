def ten(arr):
    num_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    ten_list = []
    for i in range(1,16,2):
       if arr[i] in num_dict and arr[i+1] in num_dict:
           x = num_dict[arr[i]] * 16
           y = num_dict[arr[i+1]]
           ten_list.append(x + y)
       elif arr[i] not in num_dict and arr[i+1] not in num_dict:
           x = int(arr[i]) * 16
           y = int(arr[i+1])
           ten_list.append(x + y)
       elif arr[i] in num_dict and arr[i+1] not in num_dict:
           x = num_dict[arr[i]] * 16
           y = int(arr[i+1])
           ten_list.append(x + y)
       elif arr[i] not in num_dict and arr[i+1] in num_dict:
           x = int(arr[i]) * 16
           y = num_dict[arr[i+1]]
           ten_list.append(x+y)
    return ten_list
def final(arr):
    ten_array = ten(array)
    final_list = []
    for i in range(8):
        final_list.append(ten_array[i] - arr[i])
    return final_list
def inorder():
    pass

T = int(input())
for tc in range(1,T+1):
    array = list(map(str, input()))
    N = int(array[0])
    salt = []
    num = []
    for i in range(1,9):
        salt.append(N*i)
        num.append(i)
    list_1 = final(salt)
    final_l = []
    for i in range(8):
        final_l.append(list_1[i] % 10)
    print(final_l)

