def solution(n, info):
    answer = [0 for _ in range(11)]
    score_ls = [0 for _ in range(11)]


    def compare_score(ryan, appeach):
        ryan_score, appeach_score = 0, 0

        for i in range(11):
            if ryan[i] == appeach[i] == 0:
                continue

            if ryan[i] > appeach[i]:
                ryan_score += 10 - i
            else:
                appeach_score += 10 - i

        return ryan_score - appeach_score


    def shoot(idx, rest_score):
        nonlocal max_diff, answer
        if idx == 11:
            result = compare_score(score_ls, info)
            if max_diff < result:
                answer = score_ls[:]
                max_diff = result

            elif max_diff == result:
                answer = max(answer, score_ls, key=lambda x: x[::-1])[:]

            else:
                pass

        else:
            score = 0
            if idx == 10:
                score = rest_score
            score_ls[idx] = score
            shoot(idx + 1, rest_score)

            info_score = info[idx]
            if info_score + 1 <= rest_score:
                score_ls[idx] = info_score + 1
                shoot(idx + 1, rest_score - (info_score + 1))
            score_ls[idx] = 0


    max_diff = 0
    shoot(0, n)

    if max_diff:
        return answer
    else:
        return [-1]