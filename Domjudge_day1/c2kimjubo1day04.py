# 스택 구현
t = int(input())

for i in range(t):
    stack = []
    ans = []
    n = int(input())
    queries = list(map(int, input().split()))
    for q in queries :
        if q > 0 :
            stack.append(q)
        else :
            ans.append(stack.pop())
    print(*ans)