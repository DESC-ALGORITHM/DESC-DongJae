import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if m[x][y] < m[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]
 
M, N = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]

print(dfs(M-1, N-1))