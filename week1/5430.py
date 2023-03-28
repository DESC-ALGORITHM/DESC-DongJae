import sys
from collections import deque

def main():
    inputTestCase = int(sys.stdin.readline())
    
    for i in range(inputTestCase):
        inputCommand = sys.stdin.readline().replace('\n','') # R = REVERSE , D = DELETE
        inputSize = int(sys.stdin.readline())
        if inputSize > 0 :
            inputData = deque(map(int,sys.stdin.readline().replace('[','').replace(']','').split(',')))
        else:
            inputData = sys.stdin.readline().replace('[','').replace(']','').replace('\n','')

        result = '['
        isError = False
        isReverse = False # D의 경우를 생각해서 초기값은 false
        for k in range(len(inputCommand)):
            if inputSize == 0 and inputCommand[0] == 'D': 
                isError = True
                break
            if len(inputCommand) == 0 or len(inputData) == 0: break
            temp = len(inputCommand.lstrip('R')) #맨 앞부터 차례대로 R이있으면 삭제 후 길이 리턴
            temp = len(inputCommand)-temp # 총 길이 - 수정된길이 = R의 개수 없으면 당연히 0 temp가 1 이상이면 있다는 뜻
            if temp > 0: # R이 있느냐? - 있으면 홀이냐 짝이냐?
                # RRRDDDRRR 4 [1,2,3,4] -> [1]
                if temp % 2 == 1: # 홀이면 한번 뒤집혀야함
                    if isReverse:
                        isReverse = False
                    else:
                        isReverse = True # 실제론 뒤집지 않음.
                inputCommand = inputCommand.lstrip('R')
            if len(inputCommand) < 1:
                break
            if isReverse: # [1,2,3,4]에서 뒤집힌 채로 D가 들어온다면 4를 지워야함
                # 위에서 R이 무조건 걸러지니, 오는 명령어는 무조건 D
                inputData.pop()
            else: # 뒤집지 않은채로 삭제 -> 맨앞삭제 -> popleft
                inputData.popleft()
            inputCommand = inputCommand[1:]
        if len(inputCommand) > 0:
            if inputCommand.count('D'):
                isError = True
        if isReverse:
            for k in range(len(inputData)-1,-1,-1):
                result+='{0:}'.format(inputData[k])
                if k != 0:
                    result+=','
        else:
            for k in range(len(inputData)):
                result+='{0:}'.format(inputData[k])
                if len(inputData)-1 != k:
                    result+=','
                    
        result+=']'
        if not isError:
            print(result)
        else:
            print('error')
        
            


main()
#3

# D 0 [] 

# R 0 []

# R 0 []