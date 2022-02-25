#퇴사
n = int(input())
array = []
for _ in range(n):
  t, p = map(int, input().split())
  array.append((t,p))
array = [(0,0)] + list(reversed(array))
d = [0]*(n+1)

for i in range(1, n+1):
  if array[i][0] > i:
    d[i] = d[i-1]
  else:
    d[i] = max(d[i-array[i][0]]+array[i][1], d[i-1])

print(d[n])
