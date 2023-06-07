import collections

def bfs(cur_v, dst_v):
    q = collections.deque()
    
    q.append([cur_v, 0])
    V[cur_v] = 1
    while q:
        cur_v, cnt = q.popleft()
        if cur_v == dst_v:
            return cnt
        for m, a in dr:
            nxt_v = cur_v * m + a
            if 0 <= nxt_v <= 100000 and not V[nxt_v]:
                if m % 2:
                    q.append([nxt_v, cnt + (m % 2)])
                else:
                    q.appendleft([nxt_v, cnt + (m % 2)])
                V[nxt_v] = 1

N, K = map(int, input().split())
dr = [[2, 0], [1, 1], [1, -1]]
V = [0] * 100001

print(bfs(N, K))
