from collections import deque
 
com = int(input())
vertex = int(input())
 
array = [[] for _ in range(com+1)]
result = 0
visited = [False] * (com+1)
 
for i in range(vertex):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x)
 
 
def bfs(i):
    global result
    queue = deque([i])
    visited[i] = True
    while queue:
        v = queue.popleft()
        for i in array[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result += 1
 
 
bfs(1)
print(result)