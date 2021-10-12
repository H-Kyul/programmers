'''
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''

def solution(numbers):
    from itertools import combinations
    answer = set() # 결과 중복 X
    for a,b in combinations(numbers,2):
        answer.add(a+b)
    return sorted(answer,reverse=False) # 배열 오름차순, answer는 set이나, sorted 정렬 후 list형으로 반환됨
