# 무거운 용액 - 조교님
for t in range(int(input())):
    N, C = map(int, input().split())
    liquidlist = []
    
    for i in range(N):
        w, v = map(int, input().split())
        liquidlist.append((w/v, w, v)) # 밀도, 무게, 부피 
    liquidlist.sort(reverse=True)
    maxg = 0

    for i in range(N):
        if C >= liquidlist[i][2]: # 채우고자 하는 용액보다 크다면 다 넣을 수 있다
            maxg += liquidlist[i][1] # i번째 용액이 가지고 있는 전체 무게 
            C -= liquidlist[i][2] # liquidlist[i][2]만큼 넣었으니 C에서 빼줌 
        else:
            maxg += C*(liquidlist[i][0])# 밀도*일정밀도 
            break
            
    print(int(maxg))