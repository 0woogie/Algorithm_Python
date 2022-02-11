#국영수
import sys
input = sys.stdin.readline

n = int(input())

students = []
for _ in range(n):
  name, kor, eng, mat = input().split()
  students.append((name, int(kor), int(eng), int(mat)))

students.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))

for student in students:
  print(student[0])
