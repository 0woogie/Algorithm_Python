#병든 나이트
n, m = map(int, input().split())

if n==1:
    print(1)
elif n==2 and m<=6:
    print((m+1)//2)
elif n==2 and m>=7:
    print(4)
elif m<=4:
    print(m)
elif m==5:
    print(4)
else:
    print(m-2)
