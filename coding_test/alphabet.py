def solution(word):
    change = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = len(word)
    rule = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1 # 781
    for i in word:
        answer += rule * change[i]
        rule = (rule - 1) // 5
    return answer
