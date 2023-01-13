# import sys
# try:
#     score = int(input('Enter score: '))
#     if score < 0 : sys.exit()
#     if score >= 95 : grade ='A+'
#     elif score >= 90 : grade = 'A-'
#     elif score >= 85 : grade = 'B+'
#     elif score >= 80 : grade = 'B-'
#     elif score >= 75 : grade = 'C+'
#     elif score >= 70 : grade = 'C-'
#     elif score >= 65 : grade = 'D+'
#     elif score >= 60 : grade = 'D-'
#     else: grade = 'F'
# except:
#     print('Please enter the number or more than 0 only.')
# else:
#     print(f'Your grade is {grade}.\n')
# finally:
#     print(f'Everyone! Well done. See you next.')

try:
    num = int(input('Enter the numbers here: '))
    odd = f'{num} is the odd.'
    even = f'{num} is the even.'    
except:
    print('Please, Enter the numbers only')
else:
    print(even) if not num % 2 else print(odd)
finally:
    print('Thank for all.')