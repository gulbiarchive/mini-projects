# 중복되지 않는 랜덤 숫자 세 개 생성하기
# 0 ~ 9까지의 숫자 리스트에서 세 개를 랜덤하게 추출
# 그것이 바로 컴퓨터가 낸 문제
import random

numbers = list(range(0, 10))
print(numbers)

three_numbers = random.sample(numbers, 3)
three_numbers.sort()
print(f'맞춰야할 숫자: {three_numbers}')
                