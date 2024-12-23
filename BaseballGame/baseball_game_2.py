# 중복되지 않는 랜덤 숫자 세 개 생성하기
# 0 ~ 9까지의 숫자 리스트에서 세 개를 랜덤하게 추출
# 그것이 바로 컴퓨터가 낸 문제
import random

numbers = list(range(0, 10))
print(numbers)

three_numbers = random.sample(numbers, 3)
three_numbers.sort()
print(f'맞춰야할 숫자: {three_numbers}')

'''
제시한 숫자에 대해 스트라이크, 볼 판정

자리와 숫자가 같은 경우에는 스트라이크 개수가 +1
숫자만 같을 경우 볼 개수가 +1
'''

n1, n2, n3 = map(int, input('0 - 9 사이 숫자 3개 입력(중복 안 됨): ').split())

strike = 0
ball = 0

if n1 == three_numbers[0]:
    strike += 1
if n2 == three_numbers[1]:
    strike += 1
if n3 == three_numbers[2]:
    strike += 1

# n1과 three_number[0]이 같으면 자리, 숫자 다 같기 때문에 볼이 안 됨
# 그러므로 이 경우 제외하고 나머지 작성
if n1 == three_numbers[1] or n1 == three_numbers[2]:
    ball += 1
if n2 == three_numbers[0] or n2 == three_numbers[2]:
    ball += 1
if n3 == three_numbers[0] or n3 == three_numbers[1]:
    ball += 1

print(f'strke : {strike}, ball: {ball}')