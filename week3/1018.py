# 체스판 다시 칠하기

N,M = map(int, input().split())
arr=[]
cntArr=[]
for i in range(N):
    arr.append(input())
    
for j in range(N-7):
    for k in range(M-7):
        sol1=0
        sol2=0
        for x in range(j, j+8):
            for y in range(k, k+8):
                if (x+y)%2==0:
                    if arr[x][y]!='W':
                        sol1+=1
                    if arr[x][y]!='B':
                        sol2+=1
                else:
                    if arr[x][y]!='W':
                        sol2+=1
                    if arr[x][y]!='B':
                        sol1+=1
                    
        cntArr.append(min(sol1, sol2))
res=min(cntArr)
print(res)
                        