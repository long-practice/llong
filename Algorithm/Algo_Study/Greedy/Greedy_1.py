# 거스름돈 문제
# n: 금액 / count: 동전 개수
n = int(input())
count = 0

# 큰 단위의 화폐부터 차례로 확인
# 500원, 100원, 50원, 10원
coin = [500, 100, 50, 10]

# 차례대로 큰 화폐부터 거슬러주기
for c in coin:
    count += n // c
    n %= c

print(count)