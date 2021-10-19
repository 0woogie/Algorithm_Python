#문자열 재정렬
s = input()
result = []
sum = 0

for a in s:
  if a.isdigit():
    sum += int(a)
  else:
    result.append(a)

result.sort()
if sum!=0:
  result.append(str(sum))

print(''.join(result))
