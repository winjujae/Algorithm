# BFS
from collections import deque

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    
    List = [[] for _ in range(N)]
    
    for i in range(M):
        u, v = map(int, input().split())
        List[u].append(v)
        
    for i in range(N):
        List[i].sort()
    
    Check = [False] * N # 방문 했는지 안 했는지 확인
    Queue = deque([0]) # 큐 초기화

    while len(Queue)> 0:
        v = Queue.popleft() # 큐에서 나오는 v
        if Check[v] == True: # v가 이 시점에 방문했다면
            continue
            
        Check[v] = True 
        print(v, end=' ')
        
        for i in List[v]: # v와 연결된 모든 정점 중
            if Check[i] == False: # 아직 가지 않은 i 가 있다면
                Queue.append(i) # 큐에 push
    print('')