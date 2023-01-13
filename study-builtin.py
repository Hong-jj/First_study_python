#파이썬 내장 함수
#함수명(인자1, 인자2, ...)
#인자 : 함수의 기능이 동작 하기 위해서 전달해야하는 값(데이터)
#print() : 문자열, 정수, 실수 값등을 터미널에 출력 하는 함수

#type() : 전달된 객체의 타입을 확인하기 위해 사용합니다
type()

#sum() : 값의 합을 반환하는 함수
#all(mylist) : 리스트에 있는 요소들이 모두 True로 계산될 때만 True를 돌려준다.  (요소를 참 거짓으로 변환하여 계산)
 
#any(mylist) : 리스트에 있는 요소 중 하나라도 True로 계산되는 것이 있으면 True를 돌려준다.
 
#max(mylist) : 리스트에 있는 요소 중에 비교 연산에 의해 가장 큰 것을 반환한다. (모든 요소가 비교 가능해야 함)
 
#sum(mylist) : 리스트에 있는 요소를 더한 값을 돌려준다. (모두 숫자형이어야 가능)

#max() : 가장 큰 값을 반환 하는 함수
print(max(5, 7, 8, 2, 4))

#min() : 가장 작은 값을 반환 하는 함수
print(min(5, 7, 8, 2, 4))

#sum() : 모든 값의 합을 반환 하는 함수
print(sum([5, 7, 8, 2, 4]))

#pow() : 거듭 제곱을 계산하여 반환 하는 함수
print(pow(2, 3))
print(pow(5, 3))

#divmod() : 나누기 결과의 몫, 나머지를 반환 하는 함수
print(5 / 4)
print(divmod(5, 4)) #return 데이타형식은 튜플

#round() : 반올림 함수, 지정된 자리를
#반올림 한 값을 반환 하는 함수
#-3 -2 -1 0. 1 2 3

print(round(2.567, 2))
print(round(2.564, 2))
print(round(123, -1))



#표현식
#0b : 2 진수를 표현하는 식
#0o : 8 진수를 표현하는 식
#0x : 16 진수를 표현하는 식

#bin() : 2 진수 값으로 변환하여 반환하는 함수
print(bin(10))

#16 진수 A를 2 진수로 변환
print(bin(0xA))

#8 진수 10를 2 진수로 변환
print(bin(0o10))

#oct() : 8 진수 값으로 변환하여 반환하는 함수
print(oct(10))

#16 진수 A를 8 진수로 변환
print(oct(0xA))

#2 진수 11100를 8 진수로 변환
print(oct(0b11100))

#hex() : 16 진수 값으로 변환하여 반환하는 함수
print(hex(10))

#8 진수 12를 16 진수로 변환
print(hex(0o12))

#2 진수 11100을 16 진수로 변환
print(hex(0b11100))

#2 진수 11100을 10 진수로 변환
print(0b11100)

#8 진수 12를 10 진수로 변환
print(0o12)

#16 진수 A6을 10 진수로 변환
print(0xA6)

print(hex(0x12 + 0x4A))
print(bin(0b11100 + 0x4A))

print(int('A', base=16))



# dir
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.
# 다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여주는 예이다.

print(dir[1,2,3])
# ['append',count,'extend','index','insert','pop'...]

print(dir[{"1":"a"}])  #딕셔너리 타입





list=[1,2,3,4,5]
for i,v in enumerate(list):
    print(f'index:{i} value:{v}')

# eval
# eval(expression)은 실행 가능한 문자열(1+2, "hi" + "a")을 입력으로 받아
# 문자열을 실행한 결과값을 돌려주는 함수 이다.

print(eval("1+2"))

print(eval(" 'hi' + 'guys'"))
print(eval("divmod(4,3)"))


# id
# id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)를 돌려주는 함수 이다

a=3
print(id(3))

print(id(a))

b=a
print(id(b))



