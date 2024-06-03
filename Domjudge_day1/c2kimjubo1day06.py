# 우선순위 큐 구현
import heapq

t = int(input())
for _ in range(t):
    hq = []
    ans = []
    n = int(input())
    queries = list(map(int, input().split()))
    for q in queries :
        if q > 0 :
            heapq.heappush(hq,q)
        else :
            ans.append(heapq.heappop(hq))
    print(*ans)
