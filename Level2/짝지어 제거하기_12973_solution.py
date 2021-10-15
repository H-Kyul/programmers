# 다섯번째, 문제점은?? 다시 런타임에러 발생
def solution(s):
    s = list(s)
    templist = list(s)
    
    while(True):
        for a,b in zip(s,s[1:]):
            if a == b:
                templist.remove(a)
                templist.remove(b)
                print(templist)
        
        if s == templist:
            break
        elif templist == []:
            break
        else:
            s = list(templist) 
        
    if templist == []:
        return 1
    else:
        return 0
        


# 네번째, while문 return 삭제, break로 변경, while문 밖에 return 조건
    if new_s != '':
        return 0
    else:
        return 1
        


# 세번째, return 0을 while문 밖으로
# ....   동일 ....
        if s == list(new_s):
            break
# ..... 동일 .....
    return 0
        


# 실패 코드2 : while 반복문 (정확성: 시간초과 / 효율성: ??)
def solution(s):
    
    s = list(s)
    new_s = []
    
    while(True):
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                s[i] = ''
                s[i-1] = ''
        new_s = ''.join(s)
        if s == list(new_s):
            return 0
        elif new_s == '':
            return 1
        else:
            s = list(new_s)
        

        


# 실패 코드 : 재귀 (정확성: 런타임에러 / 효율성: 시간초과)
def solution(s):
    def matching(s):
        list_s = list(s)
        for i in range(1,len(list_s)):
            if list_s[i] == list_s[i-1]:
                list_s[i] = ''
                list_s[i-1] = ''
        new_s = ''.join(list_s)
        if s == new_s:
            return 0
        elif new_s == '':
            return 1
        else:
            return matching(new_s)
        
        
    return matching(s)
