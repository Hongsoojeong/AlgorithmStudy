def solution(n, lost, reserve):

    new_reserve = list(set(reserve) - set (lost))
    new_lost =list(set(lost) - set(reserve))
    
    new_reserve.sort()
    new_lost.sort()
    
    for r in new_reserve:
        if r-1 in new_lost:
            new_lost.remove(r-1)
        elif r+1 in new_lost:
            new_lost.remove(r+1)

    answer = n  - len(new_lost)
    return answer
