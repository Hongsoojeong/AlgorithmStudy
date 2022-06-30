import heapq

def cal(scoville, K):
    return  heapq.heappop(scoville) + heapq.heappop(scoville)*2

def solution(scoville, K):
    answer = 0 
    n=len(scoville)-2
    heapq.heapify(scoville) # 힙 생성
    while True:
        if scoville[0] >=K:
            return answer
        if len(scoville) == 1 :
            if scoville[0]<K:
                return -1
            else:
                return answer
        heapq.heappush(scoville, cal(scoville, K))
        answer+=1
    return answer
