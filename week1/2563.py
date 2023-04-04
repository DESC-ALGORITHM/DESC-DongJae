N = int(input())
arr = [[0 for _ in range(100)] for _ in range(100)]
res = 0
for _ in range(N):
    X, Y = map(int, input().split())
    for x in range(X, X+10):
        for y in range(Y, Y+10):
            if arr[x][y] == 0:
                arr[x][y] = 1
                res += 1
print(res)