def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x:x[n])
    return strings
    
    
    
'''
문제조건: 
(1) 인덱스 n번째 글자를 기준으로 오름차순 정렬
(2) n번째 글자가 동일할 경우 사전 순 정렬

문제풀이 과정
STEP1. 사전 순 정렬
STEP2. n번째 기준 정렬
'''
