def sosu(num):
    import math
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True # 소수임

def solution(nums):
    from itertools import combinations
    result = 0
    for com in combinations(nums,3):
        nums_sum = sum(com)
        if sosu(nums_sum) == True:
            result+=1
    return result
