def solution(n): # 1 : 단순열거, for문+if 중첩으로 시간복잡
    answer = ''

    for i in range(1,n+1):
        if i%2 == 1:
            answer += '수'
        else:
            answer += '박'
    return answer
  
  
  def solution(n): # 2 : 규칙 활용
    return "수박"*(n//2) + "수"*(n%2)
