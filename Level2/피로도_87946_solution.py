# 최종 답안
def solution(k, d):
    from itertools import permutations
    maxdg = 0
    for dlist in permutations(d,len(d)):
        cur = k
        answer = 0
        for dungeon in dlist:
            if cur >= dungeon[0]:
                cur -= dungeon[1]
                answer += 1
        maxdg = max(maxdg,answer)
    return maxdg


'''
*아래 실패 이유: 범위 지정 오류(문제 이해 오류)
for dlist in permutations(d,3)  변경> for dlist in permutations(d,len(d))
테스트케이스에 한정해서 문제 풀다 생긴 실수, 던전 최대 개수는 1~8개

*변수 설명:
- maxdg : 최대한 돌 수 있는 던전 개수
- dlist(for 문) : 순열을 이용해 던전을 다양한 순서로 탐험
- cur : 각 케이스 별 최초 체력(피로도)
- answer : 각 케이스 별 최대 던전 탐험 수


*이후 수정해볼만한 것:
- DFS시도
'''




# 실패 코드2 (실행 통과, 히든 7개 성공)

def solution(k, d):
    from itertools import permutations
    maxdg = 0
    for dlist in permutations(d,3):
        
        cur = k
        answer = 0
        print('새로운던전시작',dlist,'현재체력',cur)
        for dungeon in dlist:
            if cur >= dungeon[0]:
                cur -= dungeon[1]
                answer += 1
        if answer > maxdg:
            maxdg = answer
        print('이번탐험던전수',answer)
        print('최대탐험수',maxdg,'남은체력',cur)
        print()
    return maxdg

# 실패 코드1 (실행 통과, 히든 3개 성공)

def solution(k, dungeons):
    answer = 0
    
    dg2 = [d[0]-d[1] for d in dungeons]
    dg1 = [d[1] for d in dungeons]
    dg_dict = sorted(dict(zip(dg2,dg1)).items(),reverse=True)
    for req,con in dg_dict:
        # req,con : 입장조건,소모조건
        if k >= req:
            k -= con
            answer += 1
    return answer
