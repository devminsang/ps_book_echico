'''
입력 -
첫째 줄 - 행 N, 열 M
둘째 줄 - 각 카드에 적힌 수
'''

'''
해결 방법
1. 2차원 리스트로 저장하여, 각 행의 최소값을 구한 후, 최대 값을 구하기
2. 행을 입력 받을 때, 최소 값을 구하여 이를 리스트에 저장한 후 최대 값을 구하기
'''
num_list = []

row, column = map(int, input().split())

for _ in range(row):
    min_num_row = num_list.append(min(list(map(int, input().split()))))

print(max(num_list))