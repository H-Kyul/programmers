# 실패 코드 1 - 테스트 케이스 11번 실패

def solution(citations):
    hc = 0
    for i in range(len(citations),0,-1):
        hc = len([hc+1 for c in citations if c >= i])
        if hc == i:
            return hc
        
    return 0
    
