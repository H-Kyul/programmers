# 제출 코드

def solution(str1, str2):
    def makeset(s):
        new_s = [s[i:i+2] for i in range(len(s)-1)] # 두글자씩 끊어 원소 생성
        sets = [x.lower() for x in new_s if x.isalpha()] # 소문자 통일, 영문자 쌍만 유효
        
        return sets

    str1 = sorted(makeset(str1))
    str2 = sorted(makeset(str2))
    union = str1 + str2 # 교집합 구한 후 제거하면 합집합

    intersection = [] # 교집합
    
    for a in str1:
        if a in str2:
            str2.remove(a) 
            intersection.append(a) 
    for a in intersection:
        if a in union:
            union.remove(a) # union = set(A) + set(B) - intersection(A,B)
    if (union == []) & (intersection == []):
        return 65536
    else:
        return int(len(intersection) / len(union) * 65536)
