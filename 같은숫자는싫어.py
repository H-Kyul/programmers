def solution(arr)
    new_arr = []
    for num in arr
        if num not in new_arr
            new_arr.append(num)
        else
            if num != new_arr[-1]
                new_arr.append(num)
    return new_arr