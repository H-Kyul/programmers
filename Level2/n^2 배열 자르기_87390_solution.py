# 실패 코드1 : 시간초과 (1,4~8만 성공)
def solution(n, left, right):
    from functools import reduce
    arr = [['*']*n for _ in range(n) ]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i<=j:
                arr[j-1][i-1]=j
            else:
                arr[j-1][i-1]=i
    # arr = reduce(lambda x,y:x+y,arr)
    arr = [x for ele in arr for x in ele]  # reduce보단 빠름
    return arr[left:right+1]
