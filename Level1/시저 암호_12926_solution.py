def solution(s, n):
    answer = []
    code = list('abcdefghijklmnopqrstuvwxyz')
    for k in s:
        if k.isupper():
            i = code.index(k.lower())
            answer.append(code[(i+n)%26].upper())
        elif k == ' ':
            answer.append(k)
        else:
            i = code.index(k)
            answer.append(code[(i+n)%26])
    return ''.join(answer)
