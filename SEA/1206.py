#[S/W 문제해결 기본] 1일차 - View
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    array = [[0]*n for _ in range(256)]
    heights = list(map(int, input().split()))
    for i in range(len(heights)):
        height = heights[i]
        for j in range(height):
            array[j][i] = 1
    count = 0
    for i in range(2, n-2):
        for j in range(heights[i]):
            if array[j][i-1]==0 and array[j][i-2]==0 and array[j][i+1]==0 and array[j][i+2]==0:
                count += 1
    print("#"+str(test_case), count)
    
'''
#다른 사람 풀이(2차원 배열 이용하지 않는 간단한 방식)
t = 10
answer = []
for i in range(t):
  n = int(input())
  height = list(map(int, input().split()))
  result = 0
  for j in range(2, n-2):
    left = height[j] - max(height[j-1], height[j-2])
    right = height[j] - max(height[j+1], height[j+2])
    if left > 0 and right > 0:
      result += min(left, right)
  answer.append(result)
for i in range(t):
  print("#%d %d" %(i+1, answer[i]))
'''
