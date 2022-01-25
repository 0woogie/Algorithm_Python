#문자열 재정렬
s = input()
result = []
value = 0

for x in s:
  if x.isdigit():
    value += int(x)
  else:
    result.append(x)

result.sort()
if value!=0:
  result.append(str(value))

print(''.join(result))
