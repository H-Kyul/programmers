def solution(numbers, hand):
    result = ''
    l,r = 10,12
    
    for num in numbers:
        if num == 0:
            num = 11
        if num in [1,4,7]:
            l = num
            result += 'L'
        elif num in [3,6,9]:
            r = num
            result += 'R'
        else:
            dL1 = abs(num-l) 
            dR1 = abs(num-r)
            
            # 실제 거리차이
            dL = dL1//3 + dL1%3 
            dR = dR1//3 + dR1%3
            
            if dL > dR:
                r = num
                result += 'R'
            elif dL < dR:
                l = num
                result += 'L'
            else: # 거리가 같다면
                if hand == 'right':
                    r = num
                    result += 'R'
                else:
                    l = num
                    result += 'L'
    return result
