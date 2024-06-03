# 최단 경로 구하기
import heapq

for t in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)] # 인접 리스트 정의
    for _ in range(M):
        u, v, c = map(int, input().split()) # 출발 정점, 도착 정점, 가중치 입력
        graph[u].append([v, c]) # 입력받은 정보를 인접리스트에 반영
    
    visit = [False]*N # 정점 방문 여부를 저장하는 리스트
    dist = [-1]*N # 0번 정점으로부터의 거리를 저장하는 리스트
    hq = [] # 우선순위 큐에 사용할 리스트 초기화
    heapq.heappush(hq, (0, 0)) # 0번 정점에서 0번 정점까지의 거리는 0 , 0번 정점부터 시작(순서 주의)
    
    while len(hq) > 0:
        d, u = heapq.heappop(hq)
        
        if visit[u] == False: # 현재 정점이 아직 방문되지 않았다면 진행
            visit[u] = True
            dist[u] = d
            
            for i in graph[u]:
                if visit[i[0]] == False:
                    heapq.heappush(hq, [d+i[1], i[0]])               
    print(dist[-1]) # 목표 정점까지의 거리를 출력(도달하지 못할 시 -1 출력)