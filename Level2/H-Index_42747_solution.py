# 최종 답안

def solution(citations):
    hc = 0
    if max(citations) == 0:
        return 0
    for i in range(len(citations),0,-1):
        hc = len([hc+1 for c in citations if c >= i])
        # *** print(f'{i}번 이상 인용한 논문 {hc}개')
        
        if hc >= i:
            return i
        
''
변수 설명
- i : i번 인용(인용 횟수)
- hc : i번 이용된 논문의 개수
    
실패코드 1 실패한 이유
> 문제 이해 오류
문제 : i번 인용된 논문이 i편 이상 이면 h-index = i 
처음 이해한 내용 : i번 인용된 논문인 i편 이상이고 그 개수가 hc개일 때, h-index = hc

*** : 문제해결 핵심
    
'''
        
        
        
        
# 실패 코드 1 - 테스트 케이스 11번 실패

def solution(citations):
    hc = 0
    for i in range(len(citations),0,-1):
        hc = len([hc+1 for c in citations if c >= i])
        if hc == i:
            return hc
        
    return 0
    
