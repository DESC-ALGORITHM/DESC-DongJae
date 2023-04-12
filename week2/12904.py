S = list(input())
T = list(input())
res = 0
while T:
    if S == T:
        res = 1
        break
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
print(res)