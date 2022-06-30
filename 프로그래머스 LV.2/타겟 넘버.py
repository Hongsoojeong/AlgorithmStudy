answer = 0
def DFS(depth, idx, total, target, numbers):
    global answer
    if depth == idx: # 마지막으로 계산된 값이랑 target 값과 비교
        if total == target: # 각 원소들의 합
            answer +=1 # 맞으면 count해야하니까
            return
        else:
            return 
    DFS(depth, idx+1, total+numbers[idx], target, numbers) #더하거나
    DFS(depth, idx+1, total-numbers[idx], target, numbers) #빼거나

def solution(numbers, target):
    # 타겟 넘버를 만들도록 하는 방법의 수
    DFS(len(numbers),0,0,target,numbers)
    return answer
