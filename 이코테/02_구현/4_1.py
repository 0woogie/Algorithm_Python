#상하좌우
n = int(input())
moves = input().split()
x, y = 1, 1

types = ['L', 'R', 'U', 'D']
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

for move in moves:
  for i in range(len(types)): # i = types.index(move)를 이용하는 방법도 있음
    if move == types[i]:
      nx = x + mx[i]
      ny = y + my[i]
  if nx<1 or nx>n or ny<1 or ny>n:
    continue
  x, y = nx, ny

print(x, y)

#맨 처음 구현한 소스코드. 이동타입('L','R','U','D')이 늘어날수록 소스코드가 길어짐, 리스트 활용을 잘 하자.
"""
n = int(input())
move = input().split()
x, y = 1, 1

for m in move:
  if m=='U':
    if x==1:
      continue
    else:
      x -= 1
  elif m=='D':
    if x==n:
      continue
    else:
      x += 1
  elif m=='L':
    if y==1:
      continue
    else:
      y -= 1
  else:
    if y==n:
      continue
    else:
      y += 1

print(x, y)
"""
