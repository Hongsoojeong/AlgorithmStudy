def solution(s):
    answer = len(s) # 제일 큰 단위는 길이의 절반크기일 것
    for step in range(1, len(s)//2 +1):
        compressed = "" # 압축된 문자열
        prev = s[0:step] # 문자열은 제일 앞부터 정해진 길이만큼 자르기
        cnt = 1
        for j in range(step, len(s), step):
            if prev == s[j: j+ step] :
                cnt+=1
            else: # 단위 덩어리랑 떨어질 때
                #compressed += str(cnt) + prev if cnt >= 2 else prev
                if cnt >= 2 :
                    compressed +=str(cnt) + prev 
                else:
                    compressed += prev
                prev = s[j:j+step]
                cnt=1
        if cnt >=2: #마지막 문자 고려하려고?
            compressed += str(cnt) + prev
        else:
            compressed += prev
        prev = s[j:j+step]
        cnt=1
        answer = min (answer, len(compressed)) # 제일 작은 문자열로 갱신
    return answer
