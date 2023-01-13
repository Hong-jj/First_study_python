#String(문자열) 자료형

import sys

#print(sys.getdefaultencoding())

#문자들의 집합

'''
Sequence Type
- 문자들에 대한 순서가 유지 된다.
- Index 번호를 통해 접근 할 수 있다.

Iterable Type
- 반복문에서 문자열의 각 문자에 반복적으로 접근 가능.

immutation Type
- 문자열의 특정 문자를 변경할 수 있다.


'''


'''
s= "abcd"
print(s[0],s[2])
print(s[1:3])


c="abcd"
for x in c:
    print(x)
'''    
    
#Unpacking - 문자열을 각각의 변수로 대입

'''
x,y="58"
print(x,y)
'''

# 문자열 함수
# 2,1 find(value[, start_index]): 문자열에서 value 문자열을 찾아서 해당 문자열의 시작 index값을 반환 한다.
# start_index를 지정하면 해당 위치부터 value 문자열을 찾는다.

'''
string="python programming project"
print(string.find("pro"))
print(string.find("pro",8))
'''

#count(value) : 문자열에서 value문자열을 찾아서 해당 문자열의 갯수를 반환 한다.

'''
string="python programming project"
print(string.count("pro"))
'''

#lower() : 알파벳 문자열을 소문자로 변경 해서 반환 하는 함수 기존 문자열이 변경되지는 않는다.

'''
string="Python Programming Project"
print(string.lower())
print(string)

string=string.lower()
print(string)
'''

#upper() :알파벳 문자열을 대문자로 변경해서 반환 하는 함수 기존 문자열이 변경 되지는 않음.


string="Python Programming Project"
print(string.upper())
print(string)

string=string.upper()
print(string)


#strip([char]) : 문자열의 앞(좌)/뒤(우) 공백을 제거하여 반혼 하는 함수
# 기존 문자열의 공백이 제거되지는 않는다.
# char(문자)를 지정하는 경우 해당 문자를 제거

string= "                 "
print(string+'a')
print(string.strip)
print(string)


# split([value]) : 문자열의 공배글 기준으로 문자열을 분리하여 list자료형으로 반환

string="Python Programming Project"
print(string.split())

string= "C:\\Program Files\\Python36"
print(string.split("\\"))

# replace(old,neew): 기존 문자열에서 old에 해당하는 문자열을 new에 해당하는 
# 문자열로 변경 하여 반환하는 함수

string="Python Programming Project"
print(string.replace("python","java"))

# isnumeric(): 문자열 값이 정수형태의 문자열인지 확인 하는 함수
s1="12345"
s2="abacde"
print(s1.isnumeric(),s2.isnumeric)

#isalpha() : 문자열의 값이 알파벳으로만 구성된 문자열인지 확인 하는 함수

s1="12345"
s2="abacde"
s3="12345abcdedfg"
print(s1.isalpha(),s2.isalpha,s3.isalpha)



# find 예제
st = 'python string'
print(st.find('string'))  # string시작 인덱스 값
                          #인자를 3개를 차지함.
                          #find(문자열,시작위치,끝)
# count 예제
st = 'python string'
print(st.count('t'))  # t문자의 숫자를 반환
 
# lower 예제
st = 'PYTHON STRING'
print(st.lower())     # 'python string'로 소문자로 변경
 
# upper 예제
st = 'python string'
print(st.upper())     # 'PYTHON STRING'로 대문자로 변경
 
# strip 예제
st = '  python string  '
print(st.strip())     # 양쪽에 공백을 제거
 
# lstrip 예제
st = '  python string  '
print(st.lstrip())    # 왼쪽 공백을 제거
 
# rstrip 예제
st = '  python string  '
print(st.rstrip())    # 오른쪽 공백을 제거
 
# replace 예제
st = 'python string'
print(st.replace('string','문자열')) # 'string' => '문자열'로 변경
 
# split 예제
st = 'python string'
print(st.split(' '))
 
values = input('입력 : ').split(' ')  # I am a student
print(values)       # 리스트 자료




#[예제.1]
A = "Have a"
print(A)
B = " Nice Day"
C = A + B
print(C)        # Have a Nice Day
print(C*3)      # Have a Nice Day 세번
A += " Nice Day"# A = A+ " Nice Day"와 같음
print(A)        # Have a Nice Day
 
 
#[예제.2]
str = "python is Easy. Programming 참 쉽죠~~잉!!"
print(str)
print(str.upper())    # python is Easy. Programming 참 쉽죠~
print(str.lower())    # PYTHON IS EASY. PROGRAMMING 참 쉽죠~
#swapcase() 영문 소문자를 대문자로, 대문자를 소문자로 변경
print(str.swapcase()) # PYTHON IS eASY. pROGRAMMING 참 쉽죠~
#title() 단어의 시작은 대문자로 변경
print(str.title())    # Python Is Easy. Programming 참 쉽죠~
 
 
#[문제1] 아래의 문장 주어진 조건에 맞게 변경
 
#"NevEr-eVer 100glVe Up" [변경전]
#"Never-Ever 100Glve Up" [변경후]
st = "NevEr-eVer 100glVe Up"
print(st.title())
 
#Have a nice day 문자열에서 다음 알아오기
#'a', 'day', 'dak'의 갯수
st2 = 'Have a nice day'
print(st2)
print(st2.count('a'))
print(st2.count('day'))
print(st2.count('dak'))
 
 
#[문제2] "It is a fun python class" 문자열의 길이,
# 문자 'a'의 개수, 's'의 개수를 출력하세요.
str = "It is a fun python class"
cnt = cnt_a = cnt_s = 0
for i in str:
    cnt += 1
    if i == 'a':
        cnt_a += 1
    elif i == 's':
        cnt_s += 1
print("문자열의 길이:",cnt)
print("문자 'a'의 개수: ",cnt_a)
print("문자 's'의 개수: ",cnt_s)
 
#or  함수를 이용한 방법
print("======= 함수를 이용한 방법 =======")
print("문자열의 길이:",len(str))
print("문자 'a'의 개수: ",str.count('a'))
print("문자 's'의 개수: ",str.count('s'))
 
#[문제3] "Have a nice day" 문자열을 가지고 다음을 처리하세요.
# - 각각 find와 index를 사용하여 'day'문자의 위치를 찾으세요.
# - 각각 find와 index를 이용하여 'kkk'문자의 위치를 확인하세요
# - find를 사용하여 첫번째, 두번째, 세번째, 네번째 'a'의 위치를
#   출력하세요.
 
str3 = "Have a nice day"
print("Find('day') :",str3.find("day"))
print("index('day') :",str3.index("day"))
print("Find('kkk') :",str3.find("kkk"))    #값이 없으면 -1
#print("index('kkk') :",str3.index("kkk"))  #값이 없으면 Error
 
idx=str3.find('a')
print("find : 첫번째 a의 위치=",idx)
idx=str3.find('a',(idx+1))
print("find : 두번째 a의 위치=",idx)
idx=str3.find('a',(idx+1))
print("find : 세번째 a의 위치=",idx)
idx=str3.find('a',(idx+1))
print("find : 네번째 a의 위치=",idx)
 
#[ Quiz ] : List 정의 하여 첨자 위치 저장
#a의 총 개수와 첨자의 위치를 출력 하시오
#st = 'Have a nice day Have a nice day Have a nice day'
#결과
#a 개수 : 9
#첨자 : [1, 5, 13, 17, 21, 29, 33, 37, 45]
 
st ='Have a nice day Have a nice day Have a nice day'
cnt = 0
ls = []
while True:
    cnt = st.find("a",cnt)
    if cnt != -1:
        ls.append(cnt)
        cnt += 1
    else:
        break
print("a 개수 : ",st.count("a"))
print("첨자 : ",ls)
 
st = " 파 이 썬 "
print("*{}*".format(st))         # * 파 이 썬 * 이 출력
print("*{}*".format(st.strip())) # *파 이 썬*
 
st2 = "파이썬파"
print(st2)                       # 파이썬파
print(st2.strip("파"))           # 이썬
print(st2.lstrip("파"))          # 이썬파
print(st2.rstrip("파"))          # 파이썬
 
st3 = "---파이썬---"
print(st3)                       # ---파이썬---
print(st3.strip("-"))            # 파이썬
print(st3.lstrip("-"))           # 파이썬---
print(st3.rstrip("-"))           # ---파이썬
 
 
st = "2015/04/04"
print(st)
print(st.replace("/","."))
print(st.replace("2015","2019"))
print(st.replace(st[0:4],"2019"))
 
 
st = "Never Ever Give Up"
a = st.split()
print(st)
print(a,type(a))
 
st2 = "하나:둘:셋"
st3 = "1,2,3"
b = st2.split(":")
c = st3.split(",")
print(b,type(b))
print(c,type(c))
 
 
 
 
 
st4 = "하나둘셋넷다섯"
d = st4.split()
print(d,type(d))
 
st = "Never\nEver\nGive\nUp"
print(st.splitlines())  # 개행을 기준으로 문자열을 나눈다.
 
 
# """ """:여러 줄의 문자열을 표시할 경우 사용
st2 = """Never Ever Give UP
Never Ever Give UP
Never Ever Give UP
Never Ever Give UP"""
print(st2)
a = st2.splitlines()
print(a,type(a))


































    
    
    


