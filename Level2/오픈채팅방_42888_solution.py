def solution(record):
    user = dict()
    answer = []
    
    # 유저 닉네임 업데이트
    record = [x.split(' ') for x in record]
    for message in record:
        if message[0] != 'Leave':
            user[message[1]] = message[2]
    
    # 출력메시지
    for message in record: 
        if message[0] == 'Enter':
            answer.append(f'{user.get(message[1])}님이 들어왔습니다.')
        elif message[0] == 'Leave':
            answer.append(f'{user.get(message[1])}님이 나갔습니다.')
    return answer
