# 답안

def solution(prices):
    l = len(prices)
    seconds = []
    cnt= 0
    for i in range(l):
        cmp1 = prices[i]    
        for j in range(i+1,l):
            cmp2 = prices[j]
            if cmp2 < cmp1: # 새로운 시점 가격이 더 낮으면(하락)
                cnt+=1
                break
            else:
                cnt+=1
        seconds.append(cnt)
        cnt = 0 # reset cnt
    return seconds
