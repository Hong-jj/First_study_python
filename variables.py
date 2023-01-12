#변수
#- 데이터를 저장 할 수 잇는 메모리 공간
# 작명 - 숫자로 시작하는 작명 불가능 , 대소문자 구별 / 공백 불가
# 예약어 사용 불가(if,for,while....)

# a= 10;
# b= 10;

# print(a,b);

# a,b= 10,20;
# print(a,b);

'''
a,b,c =40, 'A',10.11
print(a,b,c);
print(a+c);
print(type(a),type(b),type(c));

'''

'''
 a='10.0';

 print(float(a));

 b=10;
 print(float(b));

a,b=10,10.0;
print(str(a),str(b));

'''

# 두 변수의 맞교환

#a,b = 10,20;
#a =b;

#print(a,b);


'''
#Q1
Linux 의 수업료가 500,000원이고 Windows 수업료는  400,000원이다. 
9월 수강생이 Linux를 30명 수강하고 Windows는  20명 수강한다. 
월 수업료 총액을 계산하는 프로그램을 작성하세요.
#Q1-1
14번 문제에서 구한 수업료 총액에서  Linux과 Windows의 수업료가 
각각 5%, 10% Discount한 경우에 손실액을 구하는 프로그램을 작성하세요.

#Q2
우리나라는 섭씨 온도를 사용하는 반면 미국과 유럽은 화씨 온도를 주로 사용합니다. 
화씨 온도(F)를 섭씨 온도(C)로 변환할 때는 다음과 같은 공식을 사용합니다. 
이 공식을 사용해 화씨 온도가 50일 때의 섭씨 온도를 계산해 보세요.
C = (F-32)/1.8

Q3
화면에 "Linux"를 10번 출력하는 프로그램을 작성하세요.

Q4
다음 형식과 같이 이름, 생년월일, 주민등록번호를 출력하는 프로그램을 작성해 보세요. 
이름: 파이썬 생년월일: 2014년 12월 12일 주민등록번호: 20141212-1623210

Q5
s라는 변수에 'Linux is not Unix'라는 문자열이 바인딩돼 있다고 했을 때 
문자열의 슬라이싱 기능과 연결하기를 이용해 s의 값을 'Unix is not Linux'으로 변경해 
보세요.

Q6
x라는 변수에 'abcdef'라는 문자열이 바인딩돼 있다고 했을 때 x의 값을 'bcdefa'로 
변경해 보세요.
'''


#Q1

#수업료 
li = 500000;    
win = 400000;

# 각 과목의 학생 수 
listu = 30;
winstu = 20;

total = (li*listu))+(win*winstu)

# 할인 적용
discount= (li*listu*0.05)+(win*winstu*0.1)
total = total-discount

print(total);

#Q2
Ftem=50;

Ctem=(Ftem-32)/1.8

print(Ctem);


#Q3
for i in range(10):
    print("Linux")

  
#Q4
name=str(input('이름을 입력해주세요. \n: '))
birth=str(input('생년월일을 입력해주세요. 예시: 2014년 12월 12일 \n: '))
regidentN=str(input('주민등록번호를 입력해주세요. \n 예시: 20141212-1623210 \n: '))

print('이름: {}\n 생년월일: {}\n 주민등록번호: {}'.format(name,birth,regidentN))
  
#Q5

#1번 방법
s="Unix is not Linux";

s=s.replace("Linux","Unix")
s=s.replace("Unix","Linux",1)
print(s)

#2번 방법
s='Linux is not Unix'
s=s[13:]+' is not '+s[:5]
print(s)

#Q6
x = 'abcdef'
x = x[1:]+x[0]
print(x)

























