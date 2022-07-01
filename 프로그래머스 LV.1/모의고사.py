def solution(answers):
    answer = []
    cases = [ [1,2,3,4,5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] ]

    size = len(answers)
    OMR_1, OMR_2, OMR_3 = [], [], []
    for i, case in enumerate (cases):
        OMR = []
        if size > len(case): # 여기서 런타임 에러가 걸림
            for j in range(len(answers)):
                OMR.append(case[j%len(case)])
        elif size == len(case):
            OMR = case[:]
        elif size < len(case) :
            OMR = case[0:size]
        if i+1 == 1:
            OMR_1 = OMR
        elif i+1 == 2:
            OMR_2 = OMR
        else:
            OMR_3 = OMR

    score_1,score_2, score_3 = 0,0,0
    
    for i in range(len(answers)):
        if answers[i] == OMR_1[i]:
            score_1 +=1
        if answers[i] == OMR_2[i]:
            score_2 +=1
        if answers[i] == OMR_3[i]:
            score_3 +=1
    scores=list()
    scores.append(score_1)
    scores.append(score_2)
    scores.append(score_3)
    
    max_score = max(scores)
    
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i+1)
    if len(answer) == 0:
        answer=[1,2,3]
    return answer
