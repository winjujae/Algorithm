# hw3 돌다리 건너가기
def count_ways_to_cross_stones(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    dp = [0] * (n + 1)

    # 초기값 설정
    dp[0] = 1  # 0번째 돌다리는 이미 건넌 상태로 처리
    dp[1] = 1  # 1번째 돌다리는 한 칸을 통해 도달 가능
    dp[2] = 2  # 2번째 돌다리는 한 칸 또는 두 칸을 통해 도달 가능
    dp[3] = 4  # 3번째 돌다리는 한 칸, 두 칸, 또는 세 칸을 통해 도달 가능

    MOD = 1904101441
    
    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD
    
    if dp[n] >= 1904101441 :
        dp[n] % 1904101441
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    ways = count_ways_to_cross_stones(n)
    print(ways)