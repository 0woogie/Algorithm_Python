#뱀
from collections import deque

n = int(input())
space = [[0]*(n+1) for _ in range(n+1)] #맵 정보

k = int(input())
#맵 정보(사과 있는 곳은 2로 표시)
for _ in range(k):
  a, b = map(int, input().split())
  space[a][b] = 2

queue = deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

l = int(input())
turn_time = []
for _ in range(l):
  s, c = input().split()
  turn_time.append((int(s), c))

#초기 세팅
x, y = 1, 1
space[x][y] = 1 #뱀이 존재하는 위치는 2로 표시
queue.append((x,y)) #뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
d = 0 #처음에는 동쪽을 보고 있음
count = 0 #시작한 뒤에 지난 초(second) 기록
index = 0

while True:

  if index<l and count == turn_time[index][0]:
    if turn_time[index][1]=='D':
      d = (d+1) % 4
    else:
      d = (d-1) % 4
    index += 1

  nx = x + dx[d]
  ny = y + dy[d]
  count += 1
  if nx<=0 or nx>n or ny<=0 or ny>n: #벽에 부딪히면 끝
    break
  elif space[nx][ny]==1: #자기자신의 몸과 부딪히면 끝
    break
  elif space[nx][ny]==2: #사과가 있으면 꼬리 유지
    x, y = nx, ny
    space[x][y] = 1
    queue.append((x,y))
  else: #space[nx][ny]==0, 사과가 없으면 꼬리 삭제
    x, y = nx, ny
    space[x][y] = 1
    queue.append((x,y))
    tail_x, tail_y = queue.popleft()
    space[tail_x][tail_y] = 0

print(count)
