from collections import defaultdict

t = int(input())
for _ in range(t):
    K = int(input())
    input_list = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    input_list.sort()  # input_list를 정렬

    count = 0
    input_dict = defaultdict(int)  # 입력 리스트의 값들의 등장 횟수를 저장하는 사전

    for num in input_list:
        input_dict[num] += 1  # 입력 리스트의 값들의 등장 횟수를 세기

    for query in queries:
        for i in range(2 * K + 1):
            count += input_dict[query - K + i]

    print(count)
