def solution(n, weak, dist):
    answer = len(dist) + 1

    total_weak = len(weak)
    weak.extend([w + n for w in weak])
    working = [False for _ in range(len(dist))]


    def EnterFriend(curr, indexWorker, endPoint):
        nonlocal answer

        move = curr + 1
        while move < endPoint and weak[move] - weak[curr] <= dist[indexWorker]:
            move += 1

        working[indexWorker] = True
        if move == endPoint:
            answer = min(answer, sum(working))
            return

        if sum(working) == len(dist):
            return

        for other_worker_index in range(len(dist)):
            if working[other_worker_index]:
                continue
            EnterFriend(move, other_worker_index, endPoint)
            working[other_worker_index] = False
        return


    for weak_idx in range(total_weak):
        end_point = weak_idx + total_weak
        for worker_idx in range(len(dist)):
            EnterFriend(weak_idx, worker_idx, end_point)
            working[worker_idx] = False

    if answer == len(dist) + 1:
        answer = -1

    return answer