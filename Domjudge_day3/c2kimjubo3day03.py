# 피보나치 2
t = int(input())

for _ in range(t):
    n = int(input())
    
    fibo = [0] * (n+1)
    
    for i in range(n+1):
        if i in [1, 2]:
            fibo[i] = 1
        else:
            fibo[i] = fibo[i-1] + fibo[i-2]
            
    print(fibo[n])