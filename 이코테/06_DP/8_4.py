#효율적인 화폐 구성
n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(input()))

d = [10001]*(m+1)

d[0] = 0
for i in range(n):
  for j in range(array[i], m+1):
    if d[j-array[i]]!=10001:
      d[j] = min(d[j], d[j-array[i]]+1)

if d[m]==10001:
  print(-1)
else:
  print(d[m])

'''
#다시 풀어봤을 때 내 풀이
INF = int(1e9)
n, m = map(int, input().split())
money = []
for _ in range(n):
  money.append(int(input()))
d = [INF]*(m+1)
d[0] = 0
for i in range(1, m+1):
  for x in money:
    if i-x<0:
      continue
    elif d[i-x]!=INF:
      d[i] = min(d[i], d[i-x]+1)
if d[m]==INF:
  print(-1)
else:
  print(d[m])
'''
