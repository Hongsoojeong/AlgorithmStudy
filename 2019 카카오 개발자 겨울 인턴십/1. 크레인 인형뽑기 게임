def solution(board, moves):
    basket = []
    answer = 0
    for i in moves:
        for j in range(0,len(board[i-1])):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
    if len(basket)>=2:
        while True:
            same_doll= False
            for n in range(0,len(basket)-1):
                if basket[n]==basket[n+1]:
                    del basket[n]
                    del basket[n]
                    answer+=2
                    same_doll=True
                    break
            if not same_doll:
                break
    return answer
