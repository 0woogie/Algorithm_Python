#곱하기 혹은 더하기
s = input()
sum = int(s[0])

for i in range(1, len(s)):
  num = int(s[i])
  if num <= 1 or sum <= 1:
    sum += num
  else:
    sum *= num

print(sum)

'''
#solution_2
s = input()
data = [int(i) for i in s]
result = 0

for x in data:
  if result<=1 or x<=1:
    result += x
  else:
    result *= x

print(result)
'''
