'''
입력 -
숫자 N, 숫자 K
'''

'''
해결 방법 -
1. N이 K로 나누어 떨어질 때, K로 나누어 줌.
2. 그렇지 않으면 -1
'''

N, K = map(int, input().split())

c = 0

while True:
    if N < K:
        break
    else:
        if N % K == 0:
            N //= K
            c += 1
        else:
            N -= 1
            c += 1
        
print(c)