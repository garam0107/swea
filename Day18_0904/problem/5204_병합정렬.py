def merge_sort(div_arr):
    global result

    if len(div_arr) <= 1:
        return div_arr
    mid = len(div_arr) // 2
    left = 