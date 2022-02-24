#금광
t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  temp = list(map(int, input().split()))
  count = 0
  array = [[0]*m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      array[i][j] = temp[count]
      count += 1
  d = [[0]*m for _ in range(n)]
  for i in range(n):
    d[i][0] = array[i][0]

  for j in range(1, m):
    for i in range(n):
      if i==0: #재검토해보니 해당 코드의 경우 n=1일 때, 반드시 인덱스 오류가 발생한다. (이코테 답안을 참고하자)
        d[i][j] = max(d[i][j-1], d[i+1][j-1]) + array[i][j]
      elif i==n-1:
        d[i][j] = max(d[i][j-1], d[i-1][j-1]) + array[i][j]
      else:
        d[i][j] = max(d[i-1][j-1], d[i][j-1], d[i+1][j-1]) + array[i][j]

  result = 0
  for i in range(n):
    if d[i][m-1]>result:
      result = d[i][m-1]

  print(result)
