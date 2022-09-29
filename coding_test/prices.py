def solution(price):
    answer = []
    
    for i in range(len(price)):
        cnt = 0
        for j in range(i+1, len(price)):
            cnt += 1
            if price[i] > price[j]:
                break;
        answer.append(cnt)
    return answer