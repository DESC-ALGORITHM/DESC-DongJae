import sys
N,M=map(int,sys.stdin.readline().strip().split())

array=[]
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().strip().split())))
    
K=int(sys.stdin.readline().strip())
for _ in range(K):
    answer=0
    i,j,x,y=map(int,sys.stdin.readline().strip().split())
    temp=array[i-1:x]
    for t in temp:
        answer+=sum(t[j-1:y])
    print(answer)