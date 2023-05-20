#연구소
import copy
from itertools import combinations

def dfs(x, y):
  graph_[x][y] = 2

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
      continue
    if graph_[nx][ny]!=0:
      continue
    else:
      dfs(nx, ny)

#이동 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

#바이러스와 빈칸 위치 저장
binkan = []
virus = []
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      binkan.append((i,j))
    elif graph[i][j]==2:
      virus.append((i,j))

#3개의 벽이 세워질 수 있는 경우의 수
cases = list(combinations(binkan, 3))

result = 0
for case in cases:
  graph_ = copy.deepcopy(graph)

  for x, y in case: #이번 case에서 세우는 벽 3개
    graph_[x][y] = 1

  #dfs 이용해서 바이러스 전파 시키기
  for x, y in virus:
    dfs(x, y)

  #남은 빈칸 수 계산, 최댓값 갱신
  tmp = 0
  for i in range(n):
    for j in range(m):
      if graph_[i][j]==0:
        tmp += 1
  if tmp > result:
    result = tmp

print(result)

'''
#copy 방식을 쓰지 않은 내 첫 번째 풀이, 좀 더 가독성이 떨어지지만 위의 풀이(4200ms)보다 수행시간이 짧았다(3000ms).
from itertools import combinations

def dfs(x, y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return
  
  if graph[x][y]==0 or graph[x][y]==2:
    graph[x][y] = 3
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
  else:
    return

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

binkan = []
virus = []
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      binkan.append((i,j))
    elif graph[i][j]==2:
      virus.append((i,j))

cases = list(combinations(binkan, 3))

result = 0
for case in cases:
  for x, y in case: #이번 case에서 세우는 벽 3개
    graph[x][y] = 1

  #dfs 이용해서 바이러스 전파 시키기
  #새로 전파되는 바이러스는 3으로 표시, 추후 삭제해야 하므로
  for x, y in virus:
    dfs(x, y)

  #남은 빈칸 수 계산, 최댓값 갱신
  tmp = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j]==0:
        tmp += 1
  if tmp > result:
    result = tmp

  for x, y in case: #실험 끝났으니 세운 벽 허물기
    graph[x][y] = 0

  for x, y in virus: #바이러스도 리셋
    graph[x][y] = 2

  for i in range(n): #빈 칸도 리셋
    for j in range(m):
      if graph[i][j]==3:
        graph[i][j] = 0

print(result)
'''
