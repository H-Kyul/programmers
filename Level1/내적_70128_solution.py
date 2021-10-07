def solution(a, b):
    import numpy as np  # numpy 라이브러리 활용
    a = np.array(a)
    b = np.array(b)
    answer = np.dot(a,b).tolist()
    return answer
