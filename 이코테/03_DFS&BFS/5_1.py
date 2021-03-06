#음료수 얼려 먹기
n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  if graph[x][y]==0:
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)

'''
#내 코드 [1]
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

def dfs(i, j):
  if 0<=i<n and 0<=j<m:
    if graph[i][j]==0:
      graph[i][j] = 1
      dfs(i-1, j)
      dfs(i+1, j)
      dfs(i, j-1)
      dfs(i, j+1)
  
count = 0
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      dfs(i, j)
      count += 1

print(count)

#내 코드 [2]
n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  graph[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<0 or nx>=n or ny<0 or ny>=m:
      continue
    if graph[nx][ny]==0:
      dfs(nx, ny)

count = 0
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      dfs(i, j)
      count += 1

print(count)
'''
