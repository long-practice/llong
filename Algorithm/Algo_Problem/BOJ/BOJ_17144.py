from collections import deque
import sys
input = sys.stdin.readline

R, C, T = map(int, input().rstrip().split())
room = [list(map(int, input().rstrip().split())) for _ in range(R)]

cleaner, dust = [], deque([])

for r in range(R):
    for c in range(C):
        if not room[r][c]:
            continue
        elif room[r][c] == -1:
            cleaner.append((r, c))
        else:
            dust.append((r, c))

rail = [[] for _ in range(2)]
for i, cle in enumerate(cleaner):
    cr, cc = cle
    for col in range(1, C):
        rail[i].append((cr, col))

    if i:
        for row in range(cr + 1, R):
            rail[i].append((row, C - 1))
    else:
        for row in range(cr - 1, -1, -1):
            rail[i].append((row, C - 1))

    for col in range(C - 2, -1, -1):
        rail[i].append((row, col))

    if i:
        for row in range(R - 2, cr, -1):
            rail[i].append((row, 0))
    else:
        for row in range(1, cr):
            rail[i].append((row, 0))


def update_room():
    for k, v in diff.items():
        kr, kc = k
        room[kr][kc] += v


def run_cleaner():
    for ra in rail:
        dust_in_rail = deque([room[dr][dc] for dr, dc in ra])
        dust_in_rail.appendleft(0)
        dust_in_rail.pop()

        for i in range(len(ra)):
            rr, rc = ra[i]
            room[rr][rc] = dust_in_rail[i]

def construct_q():
    answer = 0
    for r in range(R):
        for c in range(C):
            if room[r][c] > 4:
                dust.append((r, c))
            answer += room[r][c]
    return answer + 2

answer, time = 0, 0
while time < T:
    diff = {}
    while dust:
        curr_r, curr_c = dust.popleft()

        for nr, nc in [(curr_r - 1, curr_c), (curr_r + 1, curr_c), (curr_r, curr_c - 1), (curr_r, curr_c + 1)]:
            if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                diff[(nr, nc)] = diff.get((nr, nc), 0) + room[curr_r][curr_c] // 5
                diff[(curr_r, curr_c)] = diff.get((curr_r, curr_c), 0) - room[curr_r][curr_c] // 5

    update_room()
    run_cleaner()
    answer = construct_q()
    time += 1

print(answer)