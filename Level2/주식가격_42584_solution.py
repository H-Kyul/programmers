# 답안 , 스택큐 문제인데 사용하지 않음. 다시 풀어보기.

def solution(prices):
    l = len(prices)
    seconds = []
    for i in range(l):
        cnt= 0
        cmp1 = prices[i]    
        for j in range(i+1,l):
            cmp2 = prices[j]
            if cmp2 < cmp1: # 새로운 시점 가격이 더 낮으면(하락)
                cnt+=1
                break
            else:
                cnt+=1
        seconds.append(cnt)
    return seconds
