#DFS 활용
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 8)

def dfs(graph, visited, v, result):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            result[i] = v
            dfs(graph, visited, i, result)


input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

result = defaultdict(int)
dfs(arr, defaultdict(bool), 1, result)
for i in range(2, n + 1):
    print(result[i])