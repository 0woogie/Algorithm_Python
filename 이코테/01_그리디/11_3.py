#문자열 뒤집기
s = input()
a = int(s[0])
count = 1

for i in range(1, len(s)):
  b = int(s[i])
  if a!=b:
    count += 1
    a = b

result = count//2
print(result)
