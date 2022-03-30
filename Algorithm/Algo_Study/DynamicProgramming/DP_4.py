# 효율적인 화폐 구성

# 해결방안
# 1. Set 자료형 이용
# 화폐의 개수에 따라 만들 수 있는 금액이 어떤 것이 있는지 매 단계마다 금액 집합에 추가
# 해당 집합에 M의 값이 존재하는지 확인
# 만약 있다면 그 때의 화폐 개수는 몇 개인지 확인
# 해당 집합에 있는 값들 중 최소값이 M보다 크다면 -1 반환

# 2. DP 테이블 이용
# 화폐의 금액만큼의 크기를 가진 DP 테이블(리스트) 생성, 각각의 데이터는 INF(충분히 큰 값)로 채워줌
# 각각의 화폐에 대해 필요한 화폐의 개수를 DP 테이블에 저장
# 만약 저장하려고 하는 값이 DP 테이블 내에 있는 값보다 클 경우 저장하지 않음(필요한 최소 개수가 필요하므로)
# DP 테이블의 가장 마지막 원소가 원하는 금액을 만들기 위한 최소 화폐의 개수

# 풀이
N, M = map(int, input().split(' '))

money = []
for _ in range(N):
    money.append(int(input()))

# Set 자료형을 이용한 풀이
# 매 순간 많은 데이터를 포함하는 집합에 계속 많은 연산이 진행되므로
# 가급적 불필요한 데이터(M보다 큰 수)는 집합에서 제외시켜주는 것이 유리
def set_solution():
    answer = 1
    price = set(money)

    while price:
        next_price = set()
        for p in price:
            for m in money:
                if p + m <= M:
                    next_price.add(p + m)
        answer += 1
        price = next_price.copy()

        if M in price:
            return answer
    return -1

# DP 테이블을 이용한 풀이
# 속도가 빠르지만 금액이 큰 만큼 많은 메모리 할당 필요(DP_table 생성)
def DP_table_solution():
    INF = int(1e7) + 1 # 10000001
    # 리스트의 첫 인덱스는 0이므로 DP_table[M]으로 계산하기 위해서 M + 1 크기의 리스트 생성
    DP_table = [INF for _ in range(M + 1)]

    DP_table[0] = 0
    for m in money:
        for i in range(m, M + 1):
            # 저장하려고 하는 값이 DP 테이블 내에 있는 값보다 클 경우 저장하지 않음
            DP_table[i] = min(DP_table[i - m] + 1, DP_table[i])

    return DP_table[-1] if DP_table[-1] != INF else -1

print(set_solution())
print(DP_table_solution())