n, goal = map(int,input().split())
lst = list()

for i in range(n):
    s, e, p = map(int,input().split())
    if e <= goal:
        lst.append([s,e,p])
        
position=[i for i in range(goal+1)]

for j in range(goal+1):
    if j !=0:
        position[j]=min(position[j],position[j-1]+1)
        
    for i in lst:
        if i[0] == j:
            position[i[1]] = min(position[i[1]],position[i[0]]+i[2])
            
print(position[goal])