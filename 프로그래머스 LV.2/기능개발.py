import math
def solution(progresses, speeds):
    answer = []
    span = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    
    num,start, com,idx, cnt=span[0],0, 1, 1, 1
    span_list = span[:]
    while len(span_list)>1:
        if num < span_list[com]:
            span_list = span[idx:]
            num = span_list[0]
            answer.append(cnt)
            cnt = 1
        elif num == span_list[com]:
            span_list = span[idx:]
            cnt += 1
        else:
            span_list = span[idx:]
            cnt+=1
        idx+=1
    answer.append(cnt)
    return answer
