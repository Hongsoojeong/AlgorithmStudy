def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    # 최소 건너는 횟수는 1회.
    # ct는 stones의 원소에 mid를 뺐을 때 0이 나오는 횟수
    while left <= right:
        ct=0
        mid = (left + right) //2
        for stone in stones:
            if (stone-mid)<=0:
                ct+=1 
            else:
                ct=0  #0이 연속적으로 나오지않으면 다시 초기화
            if ct>=k:
                break
        if ct < k:
            left = mid + 1
        else:
            answer = mid
            right = mid -1
    return answer
