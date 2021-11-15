# 답안 2 : 약간의 수정(가능한 조합을 리스트에 묶어 넣기)
def solution(brown, yellow):
    import math
    area = brown + yellow
    s = []
    for i in range(3,int(math.sqrt(area))+1):
        if area % i == 0:
            s.append([area//i,i])
    for ab in s:
        a, b = ab[0],ab[1]
        if (a-2) * (b-2) == yellow:
            return ab
        
'''
변수 설명
- area : 전체 타일 개수
- s : 가로,세로로 가능한 조합 리스트
- a,b : 가로,세로

* 첫번째 약수 구하는 for문 3부터 시작: 
 > brown이 테두리가 되려면 3부터 가능(세로는 3 이상이어야 함)

'''


        
        
        
# 답안 1
def solution(brown, yellow):
    import math
    area = brown + yellow
    s = []
    for i in range(3,int(math.sqrt(area))+1):
        if area % i == 0:
            s.append(i)
            s.append(area//i)
    s.sort()
    
    for i in range(len(s)):
        a,b = s[i],s[len(s)-1-i]
        if (a-2) * (b-2) == yellow:
            return [b,a]
 

