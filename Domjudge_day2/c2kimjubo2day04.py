# 재귀 DFS(깊이 우선 탐색)
import sys
sys.setrecursionlimit(1000000) # 재귀 양 짱 많으면 메모리 터지니까 그거 방지

def DFS(v, Link, Check):
    print(v, end=' ')
    Check[v] = True
    for i in List[v]:
        if Check[i] == False:
            DFS(i, Link, Check)
        
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
    
    Check = [False] * N
    DFS(0, List[i], Check)
    print('')