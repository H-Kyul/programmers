def solution(arr1, arr2):
    import numpy as np
    arr1,arr2 = np.array(arr1),np.array(arr2)
    answer = np.dot(arr1,arr2).tolist()
    return answer
