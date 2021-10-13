def solution(x):
    s = sum(list(map(int,list(str(x))))) # 자릿수 합
    answer = x%s==0
    return answer
