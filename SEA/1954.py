#달팽이 숫자
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    array = [[0]*n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # n*n 배열 만든 뒤 d = [R,D,L,U] 순서로 n^2 만큼의 수 채우기
    direction = 0
    x, y = 0, 0
    array[0][0] = 1
    for i in range(2, n*n+1):
        #벽에 맞으면 방향 바꾸면서 진행
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx<0 or nx>=n or ny<0 or ny>=n or array[nx][ny]!=0:
            direction = (direction+1)%4
            nx = x + dx[direction]
            ny = y + dy[direction]
        x = nx
        y = ny
        array[x][y] = i

    print("#"+str(test_case))
    for i in range(n):
        for j in range(n):
            print(array[i][j], end=' ')
        print()
