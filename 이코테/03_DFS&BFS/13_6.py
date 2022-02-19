#감시 피하기
n = int(input())

graph = []
for _ in range(n):
  graph.append(input().split())

t = []
for i in range(n):
  for j in range(n):
    if graph[i][j]=='T':
      t.append((i,j))

result = 0

def observe(x, y):
  #상
  for i in range(1, x+1):
    if graph[x-i][y]=='O':
      break
    elif graph[x-i][y]=='S':
      return True
  #하
  for i in range(x+1, n):
    if graph[i][y]=='O':
      break
    elif graph[i][y]=='S':
      return True
  #좌
  for i in range(1, y+1):
    if graph[x][y-i]=='O':
      break
    elif graph[x][y-i]=='S':
      return True
  #우
  for i in range(y+1, n):
    if graph[x][i]=='O':
      break
    elif graph[x][i]=='S':
      return True
  #감시에 끝까지 안걸렸다면
  return False

def mfs(count):
  global result
  if count==3: #장애물 3개가 설치되면
    for x, y in t:
      if observe(x, y):
        result += 1
    if result==0:
      print("YES")
      exit(0)
    else:
      result = 0
    return
  for i in range(n):
    for j in range(n):
      if graph[i][j]=='X':
        graph[i][j] = 'O'
        count += 1
        mfs(count)
        graph[i][j] = 'X'
        count -= 1

mfs(0)
print("NO")
