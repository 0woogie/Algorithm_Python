#정수 삼각형
n = int(input())
array = [[0]*n for _ in range(n)]

for i in range(n):
  temp = list(map(int, input().split()))
  for j in range(len(temp)):
    array[i][j] = temp[j]

for i in range(1, n):
  for j in range(i+1):
    if j==0:
      array[i][j] += array[i-1][j]
    else:
      array[i][j] += max(array[i-1][j-1], array[i-1][j])

result = 0
for i in range(n):
  result = max(result, array[n-1][i])
print(result)
