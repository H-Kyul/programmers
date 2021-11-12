def solution(p, speeds):
    from collections import deque
    import math
    
    answer= []
    wd = [] # workingDays : 완공까지 작업일 수
    for i in range(len(p)):
        wd.append(math.ceil((100-p[i])/speeds[i]))
    wd = deque(wd)
    cnt = 1     # 완공된 작업 count
    while wd:
        if len(wd) != 1:
            tmp = wd[0]
            for i in range(1,len(wd)):
                if tmp >= wd[i]:
                    cnt += 1
                else:
                    break
        for i in range(cnt):
            wd.popleft()
        answer.append(cnt)
        cnt = 1
    return answer



# 답안 추가 (복잡하지만, 처음에 생각했던 방식), 진도 100% 완성 기준
def solution(progresses, speeds):
    from collections import deque

    answer= []
    p = deque(progresses)
    s = deque(speeds)
    
    while p:
        if len(p) == 1:
            answer.append(1)
            break
        for i in range(len(p)):
            if p[i] <= 100:
                p[i] = min(p[i] + s[i],100)
        if p[0] == 100:
            cnt = 1
            for i in range(1,len(p)):
                if p[0] == p[i]:
                    cnt += 1
                    print(cnt)
                else:
                    break
            for i in range(cnt):
                p.popleft()
                s.popleft()
            answer.append(cnt)
        else:
            pass
    return answer
