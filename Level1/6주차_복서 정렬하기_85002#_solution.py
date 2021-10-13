# 최종 풀이
def solution(weights, head2head):
    player = []
    for i,WL in enumerate(head2head): # WL:WIN/LOSE
        cnt = 0
        playcnt = len([x for x in WL if x!='N'])
        if playcnt == 0:
            winrate = 0
        else:
            winrate = len([x for x in WL if x=='W'])/playcnt*100 # 승률
            # 이긴 횟수는 다음과 같이 수정 가능
            # winrate = WL.count('W')/playcnt*100 # 승률

        w = weights[i] # w: weight
        for j in range(len(weights)):
            if (w < weights[j]) & (WL[j] == 'W'):
                cnt +=1
        player.append((i+1,w,winrate,cnt))
                
    player = sorted(player,key=lambda x:(x[2],x[3],x[1],-x[0]),reverse=True)
    answer = [x[0] for x in player]
    return answer


'''
리스트 형태가 아닌 요소로 직접 넣어주고 3건 모두 성공해 제출 -> 실패
이유: 승률 계산에 오류가 있었음. *모두가 무전적일 경우*를 고려하지 않음. -> 수정후 풀이 성공
'''



# 첫번째 풀이
def solution(weights, head2head):
    answer = []
    winrate = []
    wincount = []
    cnt = [0 for x in weights]
    boxer = list(range(1,len(weights)+1)) # 선수 번호    
    p = len(boxer) # 사람 수
    for i,WL in enumerate(head2head): # WL:WIN/LOSE , w: weight
        winrate.append(len([x for x in WL if x=='W'])/(p-1)*100) # 승률
        w = weights[i]
        for j in range(len(weights)):
            if (w < weights[j]) & (WL[j] == 'W'):
                cnt[i] +=1
                # cnt+=1
    print('전적',head2head)
    print('무게',weights)
    print('승률',winrate)
    print('무거운사람 이긴횟수',cnt)
    import pandas as pd
    df = pd.DataFrame({'선수번호':boxer,'전적':head2head,'무게':weights,
                      '승률':winrate,'무거운사람 이긴횟수':cnt})
    
    df.sort_values(['승률','무거운사람 이긴횟수','무게','선수번호'],ascending=[False,False,False,True],inplace=True)
    print(df)
    answer = df.선수번호.to_list()
    return answer
    
    


# 두번째 풀이 중....
ppl = []
pp.append([boxer,weights,winrate,cnt])
print(pp)
ppl.append((boxer,weights,winrate,cnt))
ppl = sorted(ppl,key=lambda x:(x[2]),reverse=True)
    
'''
문제점: 
    [[[1, 2, 3, 4], [50, 82, 75, 120], [33.33333333333333, 33.33333333333333, 66.66666666666666, 66.66666666666666], [1, 0, 2, 0]]]
[([1, 2, 3, 4], [50, 82, 75, 120], [33.33333333333333, 33.33333333333333, 66.66666666666666, 66.66666666666666], [1, 0, 2, 0])]
'''
