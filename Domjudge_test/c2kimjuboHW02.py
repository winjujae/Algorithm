# hw2 랜선웨어
from collections import deque

def count(n, connections, k):
    graph = [[] for _ in range(n)]
    infected = [False] * n 
    infected[k] = True

    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([k])
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if not infected[neighbor]:
                infected[neighbor] = True
                queue.append(neighbor)

    uninfected_count = infected.count(False)

    return uninfected_count

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    connections = []
    for _ in range(m):
        a, b = map(int, input().split())
        connections.append((a, b))
    uninfected = count(n, connections, k)
    print(uninfected)
