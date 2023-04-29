from itertools import accumulate


def solution(n, t, m, timetable):
    ans, answer = 0, ''
    minutes = [0 for _ in range(1440)]

    for time in timetable:
        hour, minu = map(int, time.split(':'))
        minutes[hour * 60 + minu] += 1
    minutes = list(accumulate(minutes))

    gone = 0
    for i in range(541 + (n - 1) * t):
        if minutes[i] - gone < m * n - max(0, (i - 540 + (t - 1)) // t) * m:
            ans = i
        if i >= 540 and not (i - 540) % t:
            gone += min(minutes[i] - gone, m)

    return str(ans // 60).zfill(2) + ':' + str(ans % 60).zfill(2)