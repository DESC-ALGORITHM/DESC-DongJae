N, M = map(int, input().split()) 
N_list = list(map(int, input().split())) 

bottom, top = 0, max(N_list) 

while bottom <= top: 
    p = (bottom+top) // 2 
    count1 = 0 
    for tree in N_list: 
        if tree >= p:
            count1 += tree - p
    if count1 >= M:
        bottom = p + 1 
    else:
        top = p - 1
    
print(top)