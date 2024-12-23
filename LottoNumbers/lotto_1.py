import random

numbers = list(range(1, 46))
print(numbers)

'''
random 라이브러리의 sample 함수를 사용하여
1부터 45까지의 숫자 리스트에서 6개의 숫자를 무작위로 선택
'''

'''
sample() 함수
: 주어진 시퀀스에서 중복되지 않는 임의의 샘플 선택

형식 : random.sample(population, k)
population : 샘플을 추출할 대상
k : 추출한 샘플의 개수
결론 : population에서 무작위로 선택된 k개의 요소를 포함한 새로운 리스트 반환
'''
selected_numbers = random.sample(numbers, 6)
print(selected_numbers)

selected_numbers.sort()
print(selected_numbers)