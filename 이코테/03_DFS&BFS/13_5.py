#연산자 끼워 넣기
n = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))
max_n = -1e9
min_n = 1e9

def dfs(numbers, now):
  global max_n, min_n
  for i in range(4):
    if op[i]!=0:
      if i==0:
        result = now + numbers[0]
      elif i==1:
        result = now - numbers[0]
      elif i==2:
        result = now * numbers[0]
      else:
        result = int(now / numbers[0])
      op[i] -= 1
      if len(numbers)==1:
        max_n = max(max_n, result)
        min_n = min(min_n, result)
        op[i] += 1
        return
      dfs(numbers[1:], result)
      op[i] += 1

dfs(numbers[1:], numbers[0])

print(max_n)
print(min_n)
