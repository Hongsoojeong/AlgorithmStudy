def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)
    
def solution(w,h):
    answer = 1
    gcd = GCD(w,h)
    if gcd == 1:
        answer = (w*h)-(w+h-1)
    else :
        answer = (w*h)-(w+h-gcd)
    return answer
