# 1로 만들기 2

N = int(input().rstrip())
link = dict()
link[N] = N
i = 0
curr = [N]
if N == 1:
    print(0)
    print(1)
else:
    while not link.get(1, 0):
        i += 1
        curr_next = []
        for n in curr:
            if not n % 3 and not link.get(n // 3, 0):
                link[n // 3] = n
                curr_next.append(n // 3)
            if not n % 2 and not link.get(n // 2, 0):
                link[n // 2] = n
                curr_next.append(n // 2)
            if not link.get(n - 1, 0):
                link[n - 1] = n
                curr_next.append(n - 1)
        curr = curr_next[:]

    answer = [1]
    j = 1
    while link[j] < N:
        answer.append(link[j])
        j = link[j]
    answer = answer + [N]
    print(i)
    print(*answer[::-1])