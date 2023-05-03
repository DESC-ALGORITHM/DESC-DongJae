#이 문제는 memorization이 중요
#입력값 받는 부분
N, M = list(map(int,input().split()))
lesson_list = list(map(int, input().split()))
#하한값,상한값 셋팅
#두개의 값을 1과 max값으로 세팅해주면 되지만 문제를 통해 아래의 값으로 해도
#된다는 것을 알 수 있다.
left_val = max(lesson_list)-1 #불가능
right_val = sum(lesson_list) #가능

#반복된 계산을 피하기 위한 memorization
plus_sum = [0] * N
#배열의 누적값을 구한다.
for i in range(N):
    if i ==0:
        plus_sum[i] = lesson_list[i]
    else:
        plus_sum[i] = lesson_list[i] + plus_sum[i-1]

#아래 while문 안의 for문에서 인덱스 -1을 처음에 참조하므로
#0을 넣어준다.
plus_sum.append(0)

while True:
    mid = (left_val+right_val)//2
    start_idx = 0
    cnt = 0
    while True:
        #앞에서부터 돌면서 블루레이 갯수 카운트해주기
        for i in range(0, N+1):
            if plus_sum[start_idx+i-1]-plus_sum[start_idx-1] > mid:
                start_idx = start_idx + i - 1
                cnt += 1
                break
            if start_idx + i == N:
                start_idx = start_idx +i
                cnt += 1
                break
        if start_idx >= N:
            break
    #블루레이 갯수가 원하는 갯수보다 클 때
    if cnt > M:
        left_val = mid
    #작을 때
    else:
        right_val = mid
    
    #rigth_val가 유효값이기 때문에, 1차이나면 바로 break
    if right_val - left_val == 1:
        break
    
print(right_val)