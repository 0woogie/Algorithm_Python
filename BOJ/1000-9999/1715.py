#카드 정렬하기
import heapq
import sys
input = sys.stdin.readline

n = int(input())

h = []
for _ in range(n):
  heapq.heappush(h, int(input()))

result = 0
while len(h)!=1:
  a = heapq.heappop(h)
  b = heapq.heappop(h)
  tmp = a + b
  result += tmp
  heapq.heappush(h, tmp)

print(result)
