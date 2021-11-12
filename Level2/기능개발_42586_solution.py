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
