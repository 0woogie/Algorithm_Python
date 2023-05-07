#ATM
n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0
total = 0
for x in array:
  result += x
  total += result
print(total)
