# 하노이 탑
def Hanoi(n, start, mid, end): # n개의 원판을 start 에서 end 로 옮김
    if n == 0:
        return 
    
    Hanoi(n-1, start, end, mid) # n-1 개 원판을 start 에서 mid 로 옮김
    print(start, '->', end) # 남은 1개를 start 에서 end 로 옮김
    Hanoi(n-1, mid, start, end) # mid 로 옮긴 
    
t = int(input())
for _ in range(t):
    n = int(input())
    Hanoi(n, 'A', 'B', 'C')