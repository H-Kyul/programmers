
# 제출 --------- 모든 경우의 수 다 계산 후 return (최대 시간 테스트 25 : 3.63ms, 더 줄일 방법?) 
def solution(s):
    answer = 0
    minlen = len(s)
    ll = []
    
    for t in range(1,500+1):
        ll = [s[i:i+t] for i in range(0,len(s),t)]
        cnt = 1
        for j in range(1,len(ll)):
            if ll[j] == ll[j-1]:
                cnt += 1
                ll[j-1] = str(cnt)
                if cnt>=3:
                    ll[j-2] = ''
                
            else:
                cnt = 1
                
        if minlen > len(''.join(ll)):
            minlen = len(''.join(ll))

    return minlen
