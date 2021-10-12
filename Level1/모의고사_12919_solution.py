def solution(answers):
    bestscore = []
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]                 # 점수 초기화
    for i in range(len(answers)):   # 채점, 정답일경우 점수 부여
        if answers[i] == man1[i%5]:
            score[0] += 1
        if answers[i] == man2[i%8]:
            score[1] += 1
        if answers[i] == man3[i%10]:
            score[2] += 1
            
    maxscore = sorted(score,reverse=True)[0]  # 각 수포자 점수 중 최고점수 확인
    for i in range(len(score)): # 최대정답자 뽑기
        if score[i] == maxscore:
            bestscore.append(i+1)
    return bestscore
