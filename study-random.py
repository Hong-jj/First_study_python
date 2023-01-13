# python 기본 라이브러리중 하나로 임의의 값을 생성 할 수 있는 기능을 가진다.

'''
from random import random,randint,randrange
from random import *



#랜덤 함수

random.random() 
# 랜덤 함수는 0.0 ~ 1.0 사이의 실수(float)를 반환합니다, 정확한 범위는 1.0을 포함하지 않는 범위이다
# (0.0 <= x < 1.0)

print((random()))


#0.0 ~ 10.0 미만 (정수의 형태로 반환)

from random import *
print((random()*10))

#0 ~ 100 미만

from random import *
print((random()*100))

# randrange 함수는 매개변수 1개 버전, 2개버전이 존재
# randrange(a,b)는 a <= x < b 의 범위 내에서의 랜덤한 정수(int)를 반환
# b는 포함하지 않는 범위이다.

# 0과 65536 사이의 랜덤 수 출력
from random import *
print(randrange(0,65536))

# 0과 10 사이의 랜덤 정수를 출력
from random import *
print(randrange(0,11))

# -20과 20사이의 랜덤 정수를 출력
from random import *
print(randrange(-20,21))

# randint 함수는 인자로 들어온 a,b 사이의 랜덤한 정수(int)를 반환
# 반환하는 x는 a,b를 포함한 범위이다 (a<= N <=b)

from random import *
print(randint(1,100))


# random.uniform 함수는 인자로 들어온 a~B 사이의 실수(float)를 반환한다.
# uniform 함수의 범위는 a <= x <=b 

from random import *
print(f'uniform: {uniform(1.0,36.5)}')

# 1부터 10사이의 임의의 짝수
from random import *
print(f'짝수: {uniform(0,10,2)}')

# 최대 99까지 홀수 값만 임의로 생성하는 randrange 함수
from random import randrange
print(f'짝수: {uniform(1,100,2)}')

# 1~50미만



# random.shuffle(seq)


from random import *
a1 = [1,2,3,4,5,6,7,8]
shuffle(a1)
print(a1)


# random.sample(seq or set, N)

from random import *
print(sample(random(1,47),6))

'''

#[예제]
from random import *
# 1. random.random()
x1 = random()
print(f'1. random.random() => {x1}')
 
# 2. random.uniform(a,b)
x2 = uniform(0, 1)
print(f'2-1. random.uniform(0,1) => {x2}')
 
x3 = uniform(10, 20)
print(f'2-2. random.uniform(10,20) => {x3}')
 
# 3. random.randint(a, b)
x4 = randint(100, 200)  # 100~200
print(f'3. random.randint(100,200) => {x4}')
 
# 4. random.randrange(a, b) / random.randrange(b)
x5 = randrange(100, 200)  # 100~199
print(f'4-1. random.randrange(100,200) => {x5}')
 
x6 = randrange(200)  # 0~199
print(f'4-2. random.randrange(200) => {x6}')
 
# 5. random.choice(seq)
fruits = ('apple','pear','pineapple')
print(f'5. random.choice => {choice(fruits)}')
 
# 6. random.sample(seq or set, N)
x8 = sample([1, 2, 3, 4, 5], 3)
print(f'6-1. random.sample([1,2,3,4,5], 3) => {x8}')
 
sample(range(1, 47), 6)
#1 이상 47 미만의 6개 값을 리스트 형식으로 반환 (중복 없음)
#시퀀스 자료형을 인자로 전달받아 임의의 값(난수)을 필요한 개수만큼 리스트(list)로 반환특정 영역의 숫자를 중복 없이 리턴하기 때문에 로또 번호 생성에 사용할 수 있다.
 
x9 = sample(range(1,47),6)
print(f'6-2. random.sample(range(1,47), 6) => {x9}')
 
x10 = sample('aaaa', 3)  # 실제 문자가 같은지는 상관없음, index가 unique.
print(f'6-3. random.sample(aaaa, 3) => {x10}')
 
# 7. random.shuffle(list)
arr1 = [1,2,3,4,5,6,7,8,9,10]
print(f'7-1. random.shuffle([1~10]) before => {arr1}')
shuffle(arr1)
print(f'7-1. random.shuffle([1~10]) after  => {arr1}')




