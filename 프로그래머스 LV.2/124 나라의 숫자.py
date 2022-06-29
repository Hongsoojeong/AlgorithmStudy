def solution(n):
    answer = ''
    enum = [1,2,4]
    while True:
        if n == 0:
            break
        back = (n-1)%3
        answer =  str(enum[back]) + answer
        n=(n-1)//3
    return answer
