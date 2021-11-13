def solution(scoville, K):
    import heapq
    answer = 0
    heap = []
    
    for item in scoville:
        heapq.heappush(heap,item)
    
    while True:
        if heap[0] >= K:
            return answer
        else:
            if len(heap) == 1:
                return -1
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            heapq.heappush(heap,s1+s2*2)
            answer += 1
            

