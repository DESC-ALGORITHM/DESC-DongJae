n = int(input())
score=[]
stair = [0 for _ in range(n)]
for i in range(n):
    score.append(int(input()))

stair[0] = score[0]

for i in range(1,n):
    if i == 1:
        stair[1] = stair[0] + score[1]
    elif i == 2:
        stair[i] = max(stair[0]+score[2], score[1]+score[2])
    else:
        stair[i] = max(score[i-1]+score[i]+stair[i-3], stair[i-2]+score[i])

print(stair[n-1])