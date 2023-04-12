#S = input()
#x=0
#for i in range(0,len(S)):
#    x+=10**(i)
#print(x)

#diff = x-int(S)
#cnt1=0 #0개수
#cnt2=0 #1개수
#if len(diff) != len(S):
    
#    if S[0] == 1:
#--------------------

S=input()
cnt0=0 # 전부 0으로 바꾸는 경우
cnt1=0 # 전부 1로 바꾸는 경우

#첫번째 원소에 대해서 처리
if S[0] == "1":
    cnt0+=1
else:
    cnt1+=1

#두번째 원소부터 모든 원소를 확인
for i in range(len(S)-1):
    if S[i]!=S[i+1]:
        #다음수에서 1로 바뀌는 경우
        if S[i+1] == '1':
            cnt0 += 1
        #다음수에서 0으로 바뀌는 경우
        else:
            cnt1+=1

print(min(cnt0, cnt1))