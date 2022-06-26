'''
반복되는 수열 정의
6, 6, 6, 5, 6, 6, 6, 5
-> 6, 6, 6, 5 -> (K + 1) 반복

M을 (K + 1)로 나눈 몫이 수열이 반복되는 횟수
여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수

M이 (K + 1)로 나누어 떨어지지 않는 경우, M을 (K + 1)로 나눈 나머지만큼 가장 큰 수가 더해짐.

가장 큰 수가 더해지는 횟수 -
int(M / (K + 1)) * K + M % (K + 1)
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)