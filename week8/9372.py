import sys
input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())

    print(N-1)