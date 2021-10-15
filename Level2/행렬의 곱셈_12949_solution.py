# 최종
def solution(A, B):
        # (m,k) * (k,n) = (m,n) 
    M = len(A)
    K = len(A[0]) # = len(B[])
    N = len(B[0])
    
    answer = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(M):
        for j in range(N):
            for k in range(K):
                answer[i][j] += A[i][k] * B[k][j]
    return answer


# 첫번째 답안. 코딩테스트에서는 numpy 사용 불가할 수 있음
def solution(arr1, arr2):
    import numpy as np
    arr1,arr2 = np.array(arr1),np.array(arr2)
    answer = np.dot(arr1,arr2).tolist()
    return answer
