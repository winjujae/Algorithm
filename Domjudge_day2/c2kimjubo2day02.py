# 인접 리스트
t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    
    List = [[] for _ in range(N)]
    
    for i in range(M):
        u, v = map(int, input().split())
        List[u].append(v)
        List[v].append(u)

    
    for i in range(N):
        List[i].sort()
        print(*List[i])