# 굉장히 비효율적인 함수
# 시간복잡도 2^n

def Fibo(n):
    if n <= 2:
        return 1
    
    return Fibo(n-1) + Fibo(n-2)

t = int(input())
for _ in range(t):
    n = int(input())
    print(Fibo(n))