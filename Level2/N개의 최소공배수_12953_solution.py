# 최종 답안
def solution(arr):
    from functools import reduce
    maxLcm = reduce(lambda x,y:x*y,arr) # 최대값은 N개의 수를 모두 곱한 값
    maxNum = max(arr)
    findLcm = 0
    
    while findLcm <= maxLcm:
        findLcm += maxNum
        cnt = 0
        for num in arr:
            if findLcm % num == 0:
                cnt += 1
        if cnt == len(arr):
            return findLcm

'''
풀이 방법 변경> 가장 큰 값의 배수 중, 다른 나머지 숫자들이 0으로 나누어 떨어지는 값
'''


# 실패 코드
def solution(arr):
     from functools import reduce
    
     divisor = min(arr)
     while divisor > 1:
        cnt = 0
        for num in arr:
            if num % divisor == 0:
                cnt+=1
        if cnt == len(arr):
            break
        else:
            divisor -= 1
    if divisor == 1:
        return reduce(lambda x,y:x*y,arr)
    else:
        return reduce(lambda x,y:x*y,arr)//(divisor**(len(arr)-1))
