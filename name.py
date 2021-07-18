k_list = int(input())
k = []
for i in range(k_list):
    lists = [int(c) for c in input().split()]
    k.extend(lists)
k.sort()
print(*k, end=' ')