#스타트링크
from collections import deque

F, S, G, U, D = map(int, input().split())
array = [0 for _ in range(F+1)]
visited = [0 for _ in range(F+1)]
dx = [U, -D]

q = deque([S])
visited[S] = 1
while q:
  x = q.popleft()
  for i in range(2):
    nx = x + dx[i]
    if 0<nx<=F and visited[nx] == 0:
      array[nx] = array[x] + 1
      visited[nx] = 1
      q.append(nx)

if S == G:
  print(array[S])
elif array[G] != 0:
  print(array[G])
else:
  print("use the stairs")
  
'''
코드리뷰에서 참고한 블로그 링크
https://letalearns.tistory.com/43
https://pacific-ocean.tistory.com/387
핵심은 BFS, 유사한 문제 - BOJ 1697번 숨바꼭질
'''
