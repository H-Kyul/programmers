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
