def solution(num):
    cnt = 0
    while(num != 1):
        if num%2 == 0:
            num = num/2
        else:
            num = num*3 + 1
        cnt += 1

        if cnt > 500:
            return -1
    return cnt
  
  
  '''
  문제풀이 과정
  
  STEP 1-1 : 숫자가 짝수면 2로 나누기
  STEP 1-2 : 숫자가 홀수면 3 곱하고 1 더하기
  STEP 2 : 한 번 작업 시 cnt 1 증가
  STEP 3 : 숫자가 1이 될 때까지 반복,
    단, 500번 반복에도 반복문 벗어나지 못하면 return -1
  STEP 4 : 작업 횟수 cnt 반환
  '''
