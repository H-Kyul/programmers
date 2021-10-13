def solution(n):
    answer = sum(map(int,list(str(n))))

    # 또는
    # answer = sum([int(x) for x in str(n)])
    return answer
