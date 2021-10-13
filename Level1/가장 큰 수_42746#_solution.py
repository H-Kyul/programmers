# 최종

def solution(numbers):      
    if max(numbers) == 0:
        return "0"
    
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x: (x*4)[:4], reverse = True)
    return ''.join(numbers)
    


# 첫번째 답안 -> 실패(시간 매우매우 오래걸려서 실행 중단->시간 초과)
def solution(numbers): 
    from itertools import permutations
    ans = []
    for i in permutations(numbers):
        l = ''.join(list(map(str,i)))
        ans.append(l)

    return max(ans)
