def binarySearch(li, n):
    s, e = 0, len(li)-1
    while s <= e:
        m = (s + e) // 2 
        if li[m] == n:
            return li[s:e+1].count(n)
        if n > li[m]:
            s = m + 1
        else:
            e = m - 1
    return 0

N = int(input())
li1 = sorted(map(int, input().split()))
M = int(input())
li2 = list(map(int, input().split()))

d = {}
for n in li1:
    if n not in d:
        d[n] = binarySearch(li1, n)
        
print(' '.join(str(d[m]) if m in d else '0' for m in li2))