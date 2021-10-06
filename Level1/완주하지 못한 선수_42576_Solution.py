def solution(participant, completion):
    from itertools import zip_longest    
    participant.sort(); completion.sort()
    for a,b in zip_longest(participant,completion,fillvalue=None):
        if a!=b:
            return a
