# 최종 : 필요한 부분(자르는 부분)만 계산 
def solution(n, left, right):
    arr = [max(divmod(x,n))+1 for x in range (left,right+1)]
    
    return arr




# 실패코드2 : 시간초과 (문제점? 아마 전체 배열을 구하고 잘랐기 때문)
def solution(n, left, right):
    arr = [max(divmod(x,n))+1 for x in range (n*n)]
    
    return arr[left:right+1]


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
