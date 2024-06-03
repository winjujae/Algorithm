# 세금 징수 1
t = int(input())

for i in range(t):
    coins = [50000, 10000, 5000, 1000, 500, 100]
    tax = int(input())
    ans = []
    for coin in coins:
        ans.append(tax // coin)
        tax -= coin * (tax//coin)
    print(sum(ans))
