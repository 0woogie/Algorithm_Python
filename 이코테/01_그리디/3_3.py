#숫자 카드 게임
n, m = map(int, input().split())

minArray = []

for i in range(n):
  data = list(map(int, input().split()))
  minNum = min(data)
  minArray.append(minNum)

print(max(minArray))
