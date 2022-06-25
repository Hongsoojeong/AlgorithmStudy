from itertools import permutations
import re

def match(banned, case):
    for i in range(len(case)):
        if len(case[i]) != len(banned[i]):
            return False  
    for k in range(len(banned)):
        for z in range(len(banned[k])):
            if banned[k][z] =='*':
                continue
            if banned[k][z]!=case[k][z]:
                return False
    return True

def solution(user_id, banned_id):
    answer=0
    case = list(permutations(user_id, len(banned_id)))
    all_check=True
    result=[]
    for case in permutations(user_id,len(banned_id)):
        if match(banned_id,case):
            if sorted(case) not in result:
                result.append(sorted(case))
    answer = len(result)
    return answer
