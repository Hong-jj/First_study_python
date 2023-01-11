print(('서식','문자',100,5/2));
print("%s %s %d %.2f" %('서식','문자',100,5/2));
print("{} {} {} {}" .format('서식','문자',100,5/2));
print('8진수 10의 값:%o' %(10));
print('16진수 10의값:%x' %(10));
print('16진수(대문자) 10의 값:%X' %(10));

print('10의 값 {:b}'.format(10));
print('10의 값 {:o}'.format(10));
print('10의 값 {:x}'.format(10));
print('10의 값 {:X}'.format(10));

print('%s %s %s ' %('name','age','gender'));
print('%10s %10s %10s ' %('name','age','gender'));
print('%-10s %-10s %-10s ' %('name','age','gender'));

#파이썬에서 정렬의 기준은 좌측을 기준으로 설정한다
print('{:10} {:10} {:10}' .format('name', 'age', 'gender'));
print('{:>10} {:>10} {:>10}' .format('name', 'age', 'gender'));
print('{:^10} {:^10} {:^10}' .format('name', 'age', 'gender'));

print('{:,} {:,}' .format(1000,10000));   # 1000의 단위로 끊어서 출력



#Named Placeholder  - 변수에 값을 지정하고 순서를 마음대로 출력?
print('{gender} {name} {age}' .format(name='Kevin', age= 33 , gender='Male'));

#Get-item  
print('{p[gender]} {p[name]} {p[age]}' .format(p={'name':'Kevin', 'age': 33 , 'gender':'Male'}));

#above Python 3.6 : f-string
print(f'({"Kevin"} {33} {"Male"})');








