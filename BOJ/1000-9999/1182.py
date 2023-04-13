#부분수열의 합
from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
  for case in combinations(array, i):
    if sum(case)==s:
      count += 1
print(count)
