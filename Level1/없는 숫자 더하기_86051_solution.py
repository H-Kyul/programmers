def solution(numbers):
    numlist = set(range(10))
    diff = numlist.difference(set(numbers))
    return sum(diff)
