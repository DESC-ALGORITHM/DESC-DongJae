N = int(input())
val = list(map(int, input().split()))

d = [0 for _ in range(N)]
d[N-1] = 1
maxval = 0

for i in range(N-2, -1, -1):
    maxval = 0
    for j in range(N-1, i, -1):
        if val[i] > val[j] and maxval < d[j]:
            maxval = d[j]
    d[i] = maxval + 1
    
print(max(d))