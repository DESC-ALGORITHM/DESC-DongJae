import sys
k=int(input())

arr=list()
for _ in range(k):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
arr.sort()

res=0
for i in arr:
    res=max(res, i[0]*k)
    k-=1
    if k==0:
        break
    
print(res)