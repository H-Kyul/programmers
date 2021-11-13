def solution(n):
    answer = 0
    cnt = bin(n).count('1')
    while True:
        num = n + 1
        if bin(num).count('1') == cnt:
            return num
        else:
            n = num
            continue

'''
변수 설명:
- cnt : 2진수 변환한 n의 1의 개수

문제해결 과정:
- STEP1 : 숫자 증가하며, 2진수 변환 후 1의 개수가 cnt와 같은지 비교
- STEP2 : n보다 크고, 1의 개수가 일치하면 해당 숫자 반환, 반복문 종료
'''
