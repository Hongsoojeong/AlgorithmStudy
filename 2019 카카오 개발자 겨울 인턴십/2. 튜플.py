def solution(s):
    answer = []
    s.strip('{')
    s.strip('}')

    if '},' in s :
        s=s.split('},')
    else:
        s=s.split()
        
    for n in range(0,len(s)):
        if '{' in s[n]:
            s[n]=s[n].strip('{')
        if '}' in s[n]:
            s[n]=s[n].strip('}')
            
    for i in range(0,len(s)):
        s[i]=s[i].split(',')
        for j in range(0,len(s[i])):
            s[i][j]=int(s[i][j])
    
    s.sort(key=len)
    
    answer.append(s[0][0])
    for k in range(1,len(s)):
        for j in range(0,len(s[k])):
            if not s[k][j] in answer:
                answer.append(s[k][j])
    return answer
