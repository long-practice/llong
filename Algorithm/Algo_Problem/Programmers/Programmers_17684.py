def solution(msg):
    answer = []
    word_idx = {}
    for i in range(26):
        word_idx[chr(ord('A') + i)] = i + 1

    msg += ' '
    curr, order = 0, 27
    while curr < len(msg) - 1:
        for right in range(len(msg), curr, -1):
            word = msg[curr:right]
            if word in word_idx:
                answer.append(word_idx[word])
                word_idx[word + msg[right]] = order
                order += 1
                curr = right
                break

    return answer