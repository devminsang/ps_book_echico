'''
첫째 줄 - 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K
둘째 줄 - N개의 자연수

ex) N = 5, M = 8, K = 3
[2, 4, 5, 4, 6]
-> 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46

ex) N = 5, M = 7, K = 2
[3, 4, 3, 4, 3]
-> 4 + 4 + 4 + 4 + 4 + 4 + 4 = 28
'''

'''
해결 방법
1. 내림차순으로 정렬을 한다.
2. 두 수를 반복하며 더해준다.
    2-1. result와 count 변수를 둔다.
    2-2. count가 K와 같지 않으면, 가장 큰 값을 result에 더해준다.
    2-3. count가 K와 같으면, 두 번째로 큰 값을 result에 더한 후 count를 초기화한다.
'''

import time

N, M, K = list(map(int, input().split()))
N_list = list(map(int, input().split()))

N_list.sort(reverse=True)

result = 0
count = 1

start = time.time()

for _ in range(M):
    if count != K:
        result += N_list[0]
        count += 1
    else:
        result += N_list[1]
        count = 0
        
print(result)

end = time.time()

print(end - start)