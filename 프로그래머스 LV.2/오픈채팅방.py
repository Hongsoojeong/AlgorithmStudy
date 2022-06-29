def solution(record):
    answer = []
    # 채팅방 exit -> 새 닉네임 enter (문구가 출력됨)
    # in 채팅방 -> 닉변 -> 기존 데이터 닉네임도 전부 변경
    # 중복 닉네임 허용
    # 최종적으로 방을 개설한 사람이 보게되는 메세지 기준
    command = [record[i].split()[0] for i in range(len(record))]
    user_data={}
    
    for i in range(len(record)):
        if len(record[i].split()) ==3:
            user, nick = record[i].split()[1],record[i].split()[2]
            user_data[user]=nick
    
    for n in range(len(command)):
        user = record[n].split()[1]
        if command[n] == 'Enter':
            answer.append(f"{user_data[user]}님이 들어왔습니다.")
        elif command[n] == 'Leave':
            answer.append(f"{user_data[user]}님이 나갔습니다.")
            
    return answer
