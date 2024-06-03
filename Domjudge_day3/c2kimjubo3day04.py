# 세계암기대회
for t in range(int(input())):
    n, m = map(int, input().split())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    # T[i][j] : (0,0)에서 (i,j)에 도달했을 때 잃을 수 있는 최소 점수 
    T = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                T[i][j] = data[i][j] # 시작칸인 경우 : 시작 칸 점수
            # 제일 위쪽
            elif i == 0:
                T[i][j] = T[i][j-1] + data[i][j] # 왼쪽으로부터만 현재칸으로 이동 가능
            # 제일 왼쪽    
            elif j == 0:
                T[i][j] = T[i-1][j] + data[i][j] # 위쪽으로부터만 현재칸으로 이동 가능
            # 그 외 
            else:
                T[i][j] =  min(T[i][j-1], T[i-1][j], T[i-1][j-1]) + data[i][j]
    print(T[n-1][m-1])