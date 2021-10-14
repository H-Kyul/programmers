# 최종

def solution(n):
    answer = ''
    c124 = ['1','2','4'] # 10진수 [1,2,3]
    if n <= 3: 
        return c124[n-1] 
    while(n > 3): 
        q = n // 3
        r = n % 3
        if r == 0:
            r = 3; q-=1   # 15 = 3*5+0 = 3*4+3
        answer = c124[r-1] + answer
        n = q
        if n <= 3:  # while문 조건이 3 초과, 반복문 종료 전 마지막 
            answer = c124[q-1] + answer
    return answer

'''
문제점: 리스트에 요소 추가하고 결론적으로 마지막 요소만 사용, 시간 초과
각 요소들은 아래 규칙을 이미 사용하고 있었기 때문에 그대로 사용하려고 데이터를 쌓은 것이 문제.

고민: 임의 숫자 하나 잡아서 계속 3을 나눠봤더니 규칙 발견.
15 = 3 * 몫5 + 나머지0 => 3 * 몫4 + 나머지3
   = 3 * 몫4(3 * 몫1 + 나머지1) + 나머지 3
   => 몫이 3이하일 땐 [1,2,4], 나머지도 1~3의 숫자 즉, [1,2,4]를 대입

'''




#######################################실패의 흔적들#############################################

# 5차 : 시간은 절반 줄었으나(테스트 14 〉	통과 (87.97ms, 37.6MB)), 여전히 시간 초과
def solution(n):
    
    q = int(n/3) # 몫
    r = n%3 # 나머지
    if r == 0:
        q -= 1; r = 3
        
    c124 = ['1','2','4'] # country124 나라의 숫자, [1,2,3]를 의미
    cnt = 0 # 1,2,4 순환(끝자리수)
    idx = 0 # c124 인덱스    
    for num in range(4,q+1): 
        c124.append(c124[idx]+c124[cnt]) 
        cnt += 1
        if cnt == 3: # 1,2,4 순환이 끝나면 idx +1
            cnt = 0 
            idx += 1 
    if n <= 3:
        return c124[n-1]
    else:
        return c124[q-1]+ c124[r-1]
        
        


# 4차 : 정확성 만점(70) / 효율성 0점(시간초과)  ---- 3차에서 return 조건만 변경

def solution(n):

    def rule(num):
        q = int(num/3) # 몫
        r = num%3 # 나머지
        if r == 0:
            q -= 1; r = 3
        return q, r
    
    c124 = ['1','2','4'] # country124 나라의 숫자, [1,2,3]
    n_q,n_r = rule(n) # n 값의 q,r
    
    if n <= 3:
        return c124[n-1]
    
    for num in range(4,int(n/3)+1): # 124나라에서의 x 값 찾기(x:n의 몫)
        q,r = rule(num)
        c124.append(c124[q-1]+c124[r-1])

    return c124[n_q-1]+ c124[n_r-1]

# 3차 : 정확성 만점(70) / 효율성 0점(시간초과)
def solution(n):
    
    def rule(num):
        q = int(num/3) # 몫
        r = num%3 # 나머지
        if r == 0:
            q -= 1; r = 3
        return q, r
    
    c124 = ['1','2','4'] # country124 나라의 숫자, [1,2,3]
    n_q,n_r = rule(n) # n 값의 q,r
    
    for num in range(4,int(n/3)+1): # 124나라에서의 x 값 찾기(x:n의 몫)
        q,r = rule(num)
        c124.append(c124[q-1]+c124[r-1])

    if n <= 3:
        return c124[n-1]
    else:
        return c124[n_q-1]+ c124[n_r-1]
        


# 2차 : 정확성 만점(70) / 효율성 0점(시간초과)

def solution(n):
    country123 = [1,2,4]
    cnt = 0 # 3단위 체크, 초기값 1,2,4를 가져오기 위함(끝자리수)
    idx = 0 # country123을 순서대로 가져옴

    for num in range(4,n+1):
        
        for cnt in range(3):
            f_num = str(country123[idx]) # 앞자리숫자
            e_num = str(country123[cnt]) # 끝자리숫자
            num_of_124 = f_num + e_num
            country123.append(num_of_124)
            
            if cnt == 2:
                idx += 1
    return str(country123[n-1])
    
    
    
    
    
    
  # 1차 : 정확성 만점(70) / 효율성 0점(시간초과)
def solution(n):
  country123 = [1,2,4]
  cnt = 0 # 3단위 체크, 초기값 1,2,4를 가져오기 위함(끝자리수)
  idx = 0 # country123을 순서대로 가져옴

  for num in range(4,n+1):
      f_num = str(country123[idx]) # 앞자리숫자
      e_num = str(country123[cnt]) # 끝자리숫자
      num_of_124 = f_num + e_num
      country123.append(num_of_124)
      # print('현재숫자:',num,'124나라:',num_of_124,'현재가리키는숫자:',country123[idx])
      cnt += 1

      if cnt == 3: 
          cnt = 0 # 초기화
          idx += 1 # 다음숫자, 3개단위로 숫자 따라감
  return str(country123[n-1])
