def solution(user_id, banned_id):
    who_pick = set()
    applied_ban = [False for _ in range(len(user_id))]

    def match(uid, bid):
        if len(uid) != len(bid):
            return False

        for u, b in zip(uid, bid):
            if b != '*' and u != b:
                return False
        return True

    def func(count, pick):
        nonlocal answer

        if count == len(banned_id):
            who_pick.add(pick)
            return

        for idx in range(len(user_id)):
            if applied_ban[idx]:
                continue

            if match(user_id[idx], banned_id[count]):
                applied_ban[idx] = True
                func(count + 1, pick | (1 << idx))
                applied_ban[idx] = False

    func(0, 0)
    answer = len(who_pick)
    return answer
