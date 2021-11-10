def solution(n):
    answer = ''.join(sorted(str(n),reverse=True)) 
    return int(answer)
  
  
  '''
  STEP 1) 입력값을 문자열로 변경 후 정렬(결과는 list)
  STEP 1-2) list를 문자열로 변경
  STEP 2) return : 문자열을 정수형으로 변경
  '''
