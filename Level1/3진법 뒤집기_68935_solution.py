def solution(n):
    tmp = '0123456789ABCDEF'
    def convert(num, base) :    # N진수 변환 함수
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base) + tmp[r]
    
        
    base3 = convert(n,3)[::-1]  # 3진 법 표현후 문자열 거꾸로 정렬
    
    answer = int(base3,3) # 10진법 변환
    return answer
