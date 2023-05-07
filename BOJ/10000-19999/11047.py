#동전 0
n, k = map(int, input().split())
coins = []
for _ in range(n):
  coins.append(int(input()))
count = 0
for coin in reversed(coins):
  count += k//coin
  k %= coin
print(count)
