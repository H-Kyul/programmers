def solution(s):
    return (s.isdigit() == True) & ((len(s) == 4) | (len(s)==6))
