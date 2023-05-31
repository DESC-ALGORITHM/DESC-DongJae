N, M, K = map(int, input().split())
X = [[0] * M for _ in range(N)]

for i in range(K):
    r, c = map(int, input().split())
    X[r-1][c-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col):
    count = 1  
    stack = [(row, col)]  

    while stack:
        x, y = stack.pop()  
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M or X[nx][ny] == 0:
                continue

            count += 1 
            stack.append((nx, ny))

            X[nx][ny] = 0  
    return count

max = 0
for i in range(N):
    for j in range(M):
        if X[i][j] == 1:
            size = dfs(i, j)
            if size > max:
                max = size

print(max)
