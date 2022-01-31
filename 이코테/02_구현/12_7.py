#치킨 배달
from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
  city.append(list(map(int, input().split())))

house = []
chicken = []

#집, 치킨집 파악해서 리스트에 저장
for i in range(n):
  for j in range(n):
    if city[i][j]==1:
      house.append((i, j))
    elif city[i][j]==2:
      chicken.append((i, j))
      
#모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
cases = list(combinations(chicken, m))

final_result = 10000
for case in cases:
  case_result = 0
  #각 집마다의 치킨 거리를 구해서 도시의 치킨 거리(case_result)를 구함
  for hx, hy in house:
    distance = 10000
    for cx, cy in case:
      distance = min(distance, abs(hx-cx)+abs(hy-cy))
    case_result += distance
  #도시의 치킨 거리의 최솟값(final_result)을 구함
  final_result = min(final_result, case_result)
print(final_result)
