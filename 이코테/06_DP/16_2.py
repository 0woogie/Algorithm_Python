#정수 삼각형
n = int(input())
d = [[0]*n for _ in range(n)]

for i in range(n):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    d[i][j] = temp[j]

for i in range(1, n):
  for j in range(i+1):
    if j==0:
      d[i][j] += d[i-1][j]
    else:
      d[i][j] += max(d[i-1][j-1], d[i-1][j])

print(max(d[n-1]))
