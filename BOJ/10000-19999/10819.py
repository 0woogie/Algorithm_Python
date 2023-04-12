#차이를 최대로
from itertools import permutations

n = int(input())
array = list(map(int, input().split()))
result = 0

cases = list(permutations(array, n))
for case in cases:
  total = 0
  for i in range(len(case)-1):
    total += abs(case[i] - case[i+1])
  result = max(result, total)

print(result)

'''
1. permutations 직접 구현
2. 백트래킹
위 두 방식으로도 풀어보자..
'''
