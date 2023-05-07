#회의실 배정
import sys
input = sys.stdin.readline

n = int(input())
tables = []
for _ in range(n):
  a, b = map(int, input().split())
  tables.append((a, b))
tables.sort(key = lambda x : (x[1], x[0]))

count = 0
endline = 0
for a, b in tables:
  if a>=endline:
    endline = b
    count += 1
print(count)

'''
회의 시간표를 정렬할 때, 회의가 끝나는 시간(x[1])뿐만 아니라 회의가 시작하는 시간(x[0])도 고려해야 한다.
예를 들어, 회의 a의 시작/종료시간이 (3,4)이고 회의 b의 시작/종료시간이 (4,4)라고 하자.
회의가 (3,4) -> (4,4) 순으로 정렬된다면 회의 a, b 모두 회의실을 사용할 수 있지만,
회의가 (4,4) -> (3,4) 순으로 정렬된다면 회의 a는 회의실을 이용할 수 없게 된다.
따라서 시작시간과 종료시간이 같은 회의가 있기 때문에, 정렬 시 회의가 시작하는 시간(x[0])도 고려해야 한다.
'''
