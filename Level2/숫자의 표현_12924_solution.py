# 최종 답안

def solution(n):
    cnt = 0
    for i in range(1,n+1): # 1~n까지 숫자
        chk_1 = 0    # 연속된 숫자 합 계산
        chk_2 = n    # 앞으로 더할 수 있는 숫자의 합
        for j in range(i,n+1): # i~n까지 숫자
            if chk_1 < n: # 다시 돌려보니 이 조건은 빼도 됨. 아래에서 조건을 걸었기 때문에
                chk_1 += j
                chk_2 -= j
                if chk_1 == n: # 지금까지의 합이 n이라면 count, 반복문 종료
                    cnt += 1
                    break
                elif chk_2 < j: # n에 도달하지 못했고, 앞으로 남은 값이 현재 더한 값보다 작다면, 반복문 종료 
                    break
    return cnt
    
    


# 제출 1. 정확성 70, 효율성 0(시간초과)
def solution(n):
    sumlist = [0 for _ in range(1,n+1)]   
    for i in range(1,n+1):
        for j in range(i):
            if sumlist[j] < n:
                sumlist[j] += i
    return sumlist.count(n)
