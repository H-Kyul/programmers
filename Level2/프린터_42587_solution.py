# 풀이 2 : heap 자료구조 풀이

def solution(priorities, loc):
    import heapq
    cnt = 0
    heap = []
        
    for item in priorities:
        heapq.heappush(heap, -item)

    while heap:
        for i in range(len(priorities)):
            if priorities[i] == -heap[0]:
                heapq.heappop(heap)
                cnt += 1
                if i == loc:
                    return cnt

            
                

# 풀이 1 : queue 

def solution(priorities, loc):
    from collections import deque
    
    order = list(range(len(priorities)))
    pd = deque(priorities)
    od = deque(order)
    cnt = 0
    while True: 
        if len(pd) == 1:
            cnt += 1
            break
        
        p,o,top_pri = pd[0], od[0], max(pd)
        pd.popleft()
        od.popleft()

        if p != top_pri:
            pd.append(p)
            od.append(o)
        else:
            cnt += 1
            if o == loc:
                break

    return cnt
    
    
    '''
    변수 설명
    - order : 프린터에 출력 전, 요청받은 순서
    - cnt : 출력된 문서 개수 count
    문제풀이 과정
    - STEP1 : 프린터에 대기 중인 문서가 1개라면 > cnt + 1 추가하고 반복문 종료
    - STEP2 : 여러 개의 대기 문서
        - STEP 2-1 : 1번 대기 문서가 중요도 1순위가 아니라면 > 대기열 가장 뒤로 이동(popleft,append)
        - STEP 2-2 : 1번 대기 문서가 중요도 1순위 > 내가 요청한 문서가 출력될 때까지 출력,카운트 반복(popleft, cnt+=1)
              요청한 문서가 출력될 차례면, 반복 종료
    - STEP3 : cnt(출력된 순서) 반환               
    '''
