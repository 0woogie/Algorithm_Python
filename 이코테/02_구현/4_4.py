#게임 개발
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

game_map = []
for _ in range(n):
  game_map.append(list(map(int, input().split())))
  
count = 1
while True:
  checker = 0
  for i in range(4):
    if direction==0:
      direction = 4
    direction -= 1 #왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]
    if game_map[nx][ny] == 0: #회전한 이후 정면에 가보지 않은 칸 존재
      game_map[x][y] = 2 #현재 위치 방문처리
      x = nx
      y = ny
      count += 1
      checker += 1
      break
  if checker==0: #네 방향 모두 갈 수 없는 경우
    nx = x - dx[direction]
    ny = y - dy[direction]
    if game_map[nx][ny]==1: #뒤가 바다로 막혀있는 경우
      break
    else: #뒤에 이미 가본 땅이 있는 경우
      game_map[x][y] = 2 #현재 위치 방문처리
      x = nx
      y = ny

print(count)

'''
#책 답안 예시를 보면 방문한 위치를 저장하기 위한 별도의 리스트 d를 관리하는 방식을 취하고 있다.
#나의 답안의 경우 바다를 1, 미방문 육지를 0, 방문한 육지를 2로 처리하여 코드의 가독성이 떨어지기 때문에 답안 예시의 방식을 숙지하자.
'''
