# 실패 코드(실행 통과, 히든 3개 성공)

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
