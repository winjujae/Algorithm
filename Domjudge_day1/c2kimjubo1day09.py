def binary(input_list, item, high, low):
    while low <= high:
        mid = (high + low) // 2
        
        if input_list[mid] == item:
            return mid
        elif input_list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

t = int(input())
for _ in range(t):
    input_list = list(map(int, input().split()))
    items = list(map(int, input().split()))
    answer = []
    
    for item in items:
        result = binary(input_list, item, len(input_list)-1, 0)
        answer.append(result)
    
    print(*answer)
