def solution(numbers):
    import math
    from itertools import permutations
    def sosu(num):
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
    
    
    sosulist = set()
    for n in range(1,len(numbers)+1):
        for i in permutations(numbers,n):
            num = int(''.join(i))
            if (num not in sosulist) & (sosu(num)) :
                sosulist.add(num)
    
    return len([x for x in sosulist if x>=2])
