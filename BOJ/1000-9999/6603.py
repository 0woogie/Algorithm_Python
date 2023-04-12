#로또
from itertools import combinations

while True:
  array = list(map(int, input().split()))
  if array[0]==0:
    break
  k = array[0]
  s = array[1:]
  for case in combinations(s, 6):
    print(*case)
  print()
  
'''
print(*컨테이너타입변수) 를 사용하면 컨테이너를 벗겨내고 출력할 수 있다.
ex) print([1, 2, 3]) -> 1 2 3
'''
