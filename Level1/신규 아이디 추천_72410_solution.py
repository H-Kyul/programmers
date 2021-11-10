def solution(new_id):
    new_id = new_id.lower() # 1단계
    new_id = ''.join([x for x in new_id if x.isalnum() or x in ['-','_','.']]) # 2단계
            
    while True: # 3단계
        if '..' in new_id:
            new_id = new_id.replace('..','.')
        else:
            break
    
    new_id = new_id.lstrip('.').rstrip('.') # 4단계
    if new_id == '': # 5단계
        new_id = 'a'
    if len(new_id) > 15: # 6단계
        new_id = new_id[:15].rstrip('.')
    
    while len(new_id) < 3: # 7단계
        new_id += new_id[-1]
    return new_id
