#함수 : 빌트인함수 , 사용자정의 함수
#input() : 사용자로부터 값을 입력받아 처리하는 함수
# 입력받은 값의 데이터 타입은 str로 반환

'''
a=int(input("첫번째 숫자를 입력해주세요:"))
b=int(input("두번째 숫자를 입력해주세요:"))

sum = a+b

print("입력받은 두수의 합:" , sum)
'''



'''
Ex3] 사용자로 부터 값을 입력 받아, 평행 사변형의 면적을 구하는 code를 작성하세요.

 
Ex4] 반지름값을 입력 받아 원의 면적을 구하는 code를 작성하세요.

 
Ex8] 화씨온도를 입력받아 섭씨로 변환하는 code를 작성하세요.

 
Ex9] 상품가격을 입력받아 부가세 10% 를 부가한 후의 상품가격을 출력하세요.

 
Ex10] 상품가격, 할인율을 입력받아 최종 상품 가격을 출력하세요.
 
 
Ex11] 상품가격, 할인율입력 받고, 할인이 적용된 상품값에 부가세 10%를 적용한 최종 상품가격을 출력하세요.
 
Ex12] 정수를 입력 받아 제곱근을 출력하세요.
 
 
Ex20] 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 코드를 작성하시오.
     비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
     표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9
     출력 예제 : 홍길동님의 비만도는 112.15% 입니다.

Ex23] 정보처리기사 과목은 데이터베이스, 전자 계산기 구조, 운영 체제, 소프트웨어 공학, 데이터 통신이 있다. 
각 과목의 점수를 입력받아 평균을 구하는 프로그램을 작성 하시오.


Ex23] 직장인의 연봉을 x 라 하고 연봉의 6%는 국민연금으로, 연봉의 9%는 건강보험으로, 연봉의 1%는 고용보험으로, 
연봉의 8%는 퇴직연금으로 계산이 된다고 가정할 때, 월 실수령액은 얼마가 되는지 계산하는 프로그램을 작성하시오. 
가능하면 국민연금, 건강보험, 고용보험, 퇴직연금 금액도 사용자가 알 수 있도록 하시오.

Ex25] 600Kg 제한의 화물용 엘리베이터가 있다. 2개의 물건에 대한 무게를 실수로 입력 받아 
현재 엘리베이터에 적재 할 수 있는 무게를 구하고 출력 하시오.
     입력 양식
         첫 번째 물건의 무게 : 200.5
         두 번째 물건의 무게 : 78.56
출력 양식 : 화물 엘리베이터의 허용 무게 320.94Kg 남았습니다.


Ex27] 현재 원달러 환율이 1,121.3원 일 때 n원을 달러로 환전하는 경우 몇 달러가 되는지 구하는 코드를 작성 하시오.
'''

'''
#Q1
bottom = int(input("밑변의 길이를 입력하세요:"))
high = int(input("높이를 입력하세요:"))

result = bottom*high

print("평행 사변형의 넓이는", result ,"입니다")


#Q2
radius = int(input("원의 반지름 값:"))

cirecle = 3.14*radius**2

print("원의 면적은" , cirecle ,"입니다")


#Q3

Ftem=int(input("화씨온도 입력:"))

Ctem=(Ftem-32)/1.8

print("{}ºF = {}ºC".format(Ftem,Ctem),"입니다")



#Q4
price=int(input("상품의 가격:"))
discount = 0.1
tax = price*0.1

total=price-tax 

print("구매하신 상품의 가격은" , int(total) ,"원 입니다.")



#Q5
price=int(input("삼품의 가격:"))
discount=int(input("상품의 할인률:"))

discountprice = price*(discount/100)
total = price-discountprice

print("구매하신 상품의 가격은",int(total),"이며",int(price),"원 만큼 할인 받았습니다")

#Q6
price=int(input("삼품의 가격:"))
discount=int(input("상품의 할인률:"))
discountprice = price*(discount/100)
tax = price*0.1
total = (price-discountprice)-tax

print("구매하신 상품의 가격은",total,"원 입니다.")



#Q7
import math

num = int(input("정수 입력:"))


#기본 방법1
#square = num**(1/2)

#기본 방법2
square = math.sqrt(num)

print(num,"의 제곱근은",square,"입니다.")




#Q8

name = input("이름 입력:")
len = int(input("키 입력:"))
weight = float(input("체중 입력:"))

weight1 = (len -100)*0.9

condition= weight/(weight1*100)

print(name,"님의 비만도는",int(condition),"%입니다/")




#Q9
db=int(input("데이터베이스 점수 입력:"))
electronic=int(input("전자 계산기 구조 점수 입력:"))
os=int(input("운영체제 점수 입력:"))
sw=int(input("소프트웨어 공학 점수 입력:"))
data=int(input("데이터 통신 점수 입력:"))

avg = (db+electronic+os+sw+data)/5

print("평균 점수는",avg,"입니다.")



#Q10

x=int(input("월급 금액 입력:"))

nationaltax=x*0.06
healthtax=x*0.09
employtax=x*0.01
severancetax=x*0.08

salary = x-(nationaltax+healthtax+employtax+severancetax)

print("매월 실 수령 금액은",salary,"원이며\n 국민연금", nationaltax ,"원\n 건강보험", healthtax ,"원\n 고용보험", employtax ,"원\n 퇴직연금", severancetax, "원\n 입니다.")





#Q11
limit = 600

print("화물 엘리베이터의 허용 무게는",limit,"kg입니다.")

num1=float(input("첫 번째 물건의 무게 입력:"))
num2=float(input("두 번째 물건의 무게 입력:"))


if num1+num2 <= 600:
    weight = limit-(num1+num2)
    print("화물 엘레베이터의 허용 무게가",weight,"kg남았습니다.")
else:
    print("화물 엘리베이터의 허용 무게를 초과했습니다.")
    
    
'''

#Q12

money=int(input("환전할 금액:"))

change=money/1121.3

print("환전한 금액은",change,"원 입니다.")

    





















































