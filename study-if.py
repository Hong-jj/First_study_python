# IF문
# 조건문 - if문

# 조건절에 0, False값 이외의 값이 있으면 참 코드의 실행을 제어하기 위한 제어문 중 하나
# 조건식에 따라 코드의 실행을 제어한다
# if문에서 조건식의 결과는 항상 Ture,False로 판단한다
#조건식의 결과(True,False에) 따라 코드의 실행을 제어

'''
#$사용형식(sysntax)

if 조건식:
     실행코드1
else
     실행코드2 
'''

#주의 사항 



#if...elif...else
# if조건식에 만족하지 않는 경우 또 다른 조건식을 평가하여 코드를 분기하기위한 방법으로 사용
# elif는 반복적으로 사용가능하며 else는 생략 가능하다

'''
var1 = 1+2j    #숫자 + 문자형태를 가진 타입은 Complex 타입이다

if (type(var1) == int):
    print("Type of the variable is Integer")
elif (type(var1) == float):
    print("Type of the variable is Float")
elif (type(var1) == complex):
    print("Type of the variable is Complex")
elif (type(var1) == bool):
    print("Type of the variable is Bool")
elif (type(var1) == str):
    print("Type of the variable is String")
elif (type(var1) == tuple):
    print("Type of the variable is Tuple")
elif (type(var1) == dict):
    print("Type of the variable is Dictionaries")
elif (type(var1) == list):
    print("Type of the variable is List")
else:
    print("Type of the variable is Unknown")
    
    
    
    
    
from random import randint
if not randint(0, 1):
    print('실행 코드 1')
    print('실행 코드 2')
else:
    print('조건식이 참이 아닌 경우 실행 1')
    print('조건식이 참이 아닌 경우 실행 2')
    
    
if 10%2==0:
    print("짝수")
else:
    print("홀수")
    

from random import randint
a = randint(0,100)
if 0 < a < 50:
    print(f'Your position {a} is 50% under')
else:
    print(f'Your position {a} is 50% upper')
    

    
from random import random
num = int(random() * 26) + 65
 
if chr(num) in 'ABCDEFGHIJK':
    print('num은 ABCDEFGHIJK 중 하나의 ASCII Code 값 이다.')
    
       
rain = int(input('현재 강수 확률(%) :'))
 
if rain >= 75:
    print('우산을 들고 나간다')
else:
    print('그냥 나간다')
    
'''
    
#Q1    
#10 ~ 99 까지 임의의 값 2개를 생성하고 홀/짝을 비교하였을때 2개의
#값이 전부 홀수 또는 짝수이면, 2개의 정수 값을 더하고,
#2개의 값이 홀-짝 또는 짝-홀이면, 2개의 정수 값을 곱하시오.

from random import *

num1=randint(10,99)
num2=randint(10,99)

if num1&num2 %2 ==0:
    result=num1+num2
else:
    result=num1*num2
    
print(result)
    

#Q2
#10 ~ 99 까지 임의의 값 2개를 생성하여 더하기 문제를 만들고 
#만들어진 문제를 사용자가 답을 적어서 맞으면 정답, 틀리면 오답을 출력도 하시오.

num1=randint(10,99)
num2=randint(10,99)
sum=num1+num2

answer=int(input(str(num1) + '+' + str(num2)+ '?'))

if answer == sum:
    print("정답입니다.")
else:
    print("오답입니다.")

 
 #Q3
#사용자로부터 수학, 국어, 영어 점수를 입력 받고 3 과목에 대한
# 평균을 구한 뒤 평균 점수와 점수별 등급을 출력하는 코드를 작성하시오.
# 점수별 등급은 다음과 같습니다. 
# 수 : 100 이하 ~ 90 이상
# 우 : 90 미만 ~ 80 이상
# 미 : 80 미만 ~ 70 이상
# 양 : 70 미만 ~ 60 이상
# 가 : 60 미만 ~ 0 이상

kor=int(input("국어 점수 입력:"))
eng=int(input("영어 점수 입력:"))
mat=int(input("수학 점수 입력:"))
avg=(kor+eng+mat) /3.0


if(90<=int(avg)<=100):
    print("수")
elif(80<=int(avg)<90):
    print("우")
elif(70<=int(avg)<80):
    print("미")
elif(60<=int(avg)<70):
    print("양")
else:
    print("가")
    

#Q4
# 사용자가 입력한 체중과 키를 통해 비만도를 구하고 구해진 비만도 값으로 
# 저체중( ~ 100 미만), 정상(100 ~ 110 미만), 
# 과체중(110 ~ 120 미만) 비만(120 ~ 130 미만), 
# 고도비만(130 ~ )
# 을 구분하여 출력 하시오.


tall = int(input(" 키 : "))
weight = int(input(" 체중 : "))
weight1 = int((tall - 100) * 0.9)
result = int((weight / weight1)*100)


if (100 > result):
    print("저체중")
elif (110 > result >= 100):
    print("정상")
elif (120 > result >= 110):
    print("과체중")
elif (130 > result >= 120):
    print("비만")
else :
    print("고도비만")




#Q5
# 윤년을 구하는 코드를 작성 하시오.
# 1) 4의 배수에 해당하는 년도는 윤년이다. 그 외에는 평년
# 2) 4, 100의 배수에 모두 해당하는 경우 평년이다. 그 외에는 윤년
# 3) 4, 100, 400의 배수에 모두 해당하는 경우 윤년이다. 그 외에는 평년
# 입력 예제                 출력 예제
#     년도 : 2018           2018년은 평년 입니다.
#     년도 : 2020           2020년은 윤년 입니다.

Year = int(input('year? '))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print('윤년')
else :
    print('평년')




#Q6
# 정보처리기사 과목은 데이터베이스, 전자 계산기 구조, 운영 체제, 소프트웨어 공학, 데이터 통신이 있다. 
# 각 과목의 점수를 입력받아 합격 불합격을 알려주는 프로그램을 만드시오.
# - 정보처리기사는 한 과목 점수가 40점 미만이면 과락으로 불합격 된다.
# - 정보처리기사는 모든 과목의 평균이 60점 이상이어야 합격으로 처리 된 다.

a = int(input('데이터베이스? '))
b = int(input('전자 계산기 구조? '))
c = int(input('운영 체제? '))
d = int(input('소프트웨어 공학? '))
e = int(input('데이터 통신? '))

score = [a,b,c,d,e]
score_min = min(score)

if 40 > score_min :
    print (score_min)
    print("40 cut")
elif ((a+b+c+d+e)/5) >= 60 :
    print('합격')
else :
    print("불합격")


#Q7
#게임만들기
# 1] 허수아비(scarecrow) 게임
# 허수아비는 기본 체력을 100을 가진다.
# 게임자는 100보다 큰 공격포인트를 가지면 이긴다.
# 100보다 10이내로 공격 포인트를 얻으면 ‘아쉽다는’ 메세지 출력
# 그 외는 허수아비의 체력이 어느 정도 남았는지와 더 힘내세요 라는 메세지 출력
# 코드
# =100

hp = 100

while hp >= 1:
    damage = randint(0,100)
    hp = hp - damage
    if hp > 10:
        print('아쉬워요. 더 힘내세요!')
        print('데미지: ',damage)
        print('남은 체력 :',hp)
    elif hp > 0 :
        print('거의 다 됐어요!')
        print('남은 체력 :',hp)
        print('데미지: ',damage)
    else:
        print("사냥 성공!")
        print('남은 체력 :',hp)
        print('데미지: ',damage)






 