def solution(participant, completion):
    hashTable = {}
    answer = participant[:]
    for n in range(len(participant)):
        hashTable[participant[n]] = -1
    for i in range(len(participant)):
        hashTable[participant[i]] += 1
        
    for j in range(len(completion)):
        hashTable[completion[j]] -=1
    for h in range(len(participant)):
        if hashTable[participant[h]] >=0:
            return participant[h]
