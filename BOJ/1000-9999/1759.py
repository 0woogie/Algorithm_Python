#암호 만들기
from itertools import combinations

l, c = map(int, input().split())
data = list(input().split())
mo = []
ja = []
for x in data:
  if x in ['a','e','i','o','u']:
    mo.append(x)
  else:
    ja.append(x)

total = []
for n in range(1, len(mo)+1): #모음 선택 개수는 n개
  if len(ja)<(l-n) or (l-n)<2: #자음은 l-n개, len(ja)<(l-n)이면 수행 불가능!
    continue
  else:
    for mo_case in combinations(mo, n):
      mo_list = list(mo_case)
      for ja_case in combinations(ja, l-n):
        result = mo_list + list(ja_case)
        result.sort()
        total.append("".join(result))

total.sort()
for x in total:
  print(x)
  
'''
단순히 입력받은 C개의 문자 중에서 L개 뽑은 뒤 자음/모음 개수 충족 여부 확인하는 방법도 있다.
혹은 combinations 함수를 이용하지 않고 백트래킹으로 접근할 수도 있다.
'''
