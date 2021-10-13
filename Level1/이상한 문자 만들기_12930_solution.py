def solution(s):
    answer = ''
    idx = 0
    for a in s:
        if a == ' ': # 공백 -> idx 초기화
            idx = 0
            answer += ' '
        else:
            if idx%2 == 0:
                answer += a.upper() 
            else:
                answer += a.lower()
            idx += 1
        # print(answer)
    return answer
