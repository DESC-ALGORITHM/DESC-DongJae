import sys

N = int(sys.stdin.readline())
alpha = [] # 단어 저장
alpha_dict = {} # 알파벳 수 저장
num = []

for i in range(N):
    alpha.append(sys.stdin.readline().rstrip())
for i in range(N):
    for j in range(len(alpha[i])): # 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict: # 이미 있으면
            alpha_dict[alpha[i][j]] += 10 **(len(alpha[i])-j-1)
        else:
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)
# value 만 추가
for val in alpha_dict.values():
    num.append(val)
# 내림차순 정렬
num.sort(reverse=True) 
pows = 9
res = 0
for i in num:
    res += pows * i
    pows -= 1
print(res)
    