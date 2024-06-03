# 큐 구현
import collections

t = int(input())
for _ in range(t):
    queue = collections.deque([])
    ans = []
    n = int(input())
    queries = list(map(int, input().split()))
    for q in queries :
        if q > 0 :
            queue.append(q)
        else :
            ans.append(queue.popleft())
    print(*ans)
