'''
숫자 6개 조합 5세트 만들기

로또 한 장을 구매하면 다섯 게임에 참가할 수 있다.
그러므로 6개의 숫자 조합 5개 세트를 한 번에 생성해보자.
'''

import random

numbers = list(range(1, 46))

for i in range(1, 6):
    selected_numbers = random.sample(numbers, 6)
    selected_numbers.sort()
    print(f'{i}번 째 게임: {selected_numbers}')
