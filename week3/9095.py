T = int(input())
res=[]
def dfs(num, sum):
    global cnt
    #더한 값이 구하는 값보다 클때
    if num < sum:
        return
    #더한값 = 구한값 이면 개수 추가
    if num == sum:
        cnt+=1   
        return
    for i in range(1,4):
        sum += i
        #dfs 재귀적 수행
        dfs(num, sum)
        sum -= i
    
for i in range(T):
    num = int(input())
    cnt=0
    dfs(num,0)
    res.append(cnt)

for ans in res:
    print(ans)