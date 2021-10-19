#왕실의 나이트
location = input()
row = int(location[1])
col = ord(location[0]) - ord('a') + 1
count = 0

mrow = [-2, -1, 1, 2, 2, 1, -1, -2]
mcol = [-1, -2, -2, -1, 1, 2, 2, 1]

for i in range(len(mrow)):
  nrow = row + mrow[i]
  ncol = col + mcol[i]
  if 1<=nrow<=8 and 1<=ncol<=8:
    count += 1

print(count)
