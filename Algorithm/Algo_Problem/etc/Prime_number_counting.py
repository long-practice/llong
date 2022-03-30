# 소수 구하기

# 방법 1.
# 2보다 큰 자연수 중에서 1과 자신 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수가 소수이므로
# 2 ~ N - 1까지의 수를 반복시켜서 나누어 떨어지는 여부를 확인하면 됨
# 그러나 (2, N / 2), (3, N / 3) ... (N / n, N / n)이 서로 대응 되므로 2 ~ N / n까지의 수를 확인하면됨
# 예를 들어 36을 기준으로 했을 때는 2 ~ 6까지의 수 중에서 나누어 떨어지는 수가 있는지 없는지 확인하면 됨

# 방법 2.
# 에라토스테네스의 체 이용
# 2부터 N**0.5 까지의 수들 중 해당 배수들은 소수 목록에서 제외시키고
# 2부터 N까지의 수 중 소수 목록에 있는 수들만 출력하는 방식

N = int(input().rstrip())
is_prime = [True for _ in range(N + 1)]
is_prime[0], is_prime[1] = False, False

for i in range(2, int(N ** 0.5) + 1):
    for j in range(2 * i, N + 1, i):
        is_prime[j] = False

prime_number = [x for x in range(2, N + 1) if is_prime[x]]
print(prime_number)