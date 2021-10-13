def solution(price, money, count):
    total = sum([price+(price*i) for i in range(count)])
    if total-money > 0:
        return total-money
    else:        
        return 0
    
