#럭키 스트레이트
n = input()
sum_a = 0
sum_b = 0

for i in range(len(n)//2):
  sum_a += int(n[i])
for i in range(len(n)//2, len(n)):
  sum_b += int(n[i])

if sum_a == sum_b:
  print("LUCKY")
else:
  print("READY")
